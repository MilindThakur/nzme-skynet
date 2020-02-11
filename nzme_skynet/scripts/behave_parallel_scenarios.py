# -*- coding: UTF-8 -*-

"""
based on from github "https://gist.github.com/s1ider/f13c2f163282dbec7a61"
Customized for parallel scenarios
"""

from multiprocessing import Pool
from subprocess import Popen, PIPE
from subprocess import call
import logging
import argparse
import json
import sys
from functools import partial
from datetime import datetime


logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)-8s %(asctime)s] %(message)s")
logger = logging.getLogger(__name__)

delimiter = "_BEHAVE_PARALLEL_BDD_"

start_time = datetime.now()


def parse_arguments():
    """
    Parses commandline arguments
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        'Run behave in parallel mode for scenarios')
    parser.add_argument('--processes', '-p', type=int,
                        help='Maximum number of processes. Default = 5', default=5)
    parser.add_argument(
        '--tags', '-t', help='specify behave tags to run', action='append')
    parser.add_argument('--define', '-D', action='append', help='Define user-specific data for the config.userdata '
                                                                'dictionary. Example: -D foo=bar to store it in '
                                                                'config.userdata["foo"].')
    args = parser.parse_args()
    return args


def _run_feature(feature_scenario, tags=None, userdata=None):
    """
    Runs features/scenarios
    :param feature_scenario: Feature/scenario that should be run
    :type feature_scenario: str
    :param tags: Specific tags to run
    :type tags: str
    :param userdata: user specific data
    :type userdata: str
    :return: Feature/scenario and status
    """
    execution_elements = feature_scenario.split(delimiter)
    logger.info("Processing feature: {} ".format(execution_elements[0]))
    if not userdata:
        params = "-t {0} --no-capture".format(' -t '.join(tags))
    else:
        params = "-t {0} -D {1} --no-capture".format(
            ' -t '.join(tags), ' -D '.join(userdata))
    cmd = "behave -i {0} -n '{1}' -f allure_behave.formatter:AllureFormatter -o allure-results --no-summary -k --junit --junit-directory reports -f plain {2}".format(
        execution_elements[0], execution_elements[1], params)
    r = call(cmd, shell=True)
    status = 'PASSED' if r == 0 else 'FAILED'
    logger.info(
        "{0:50}: {1} --> {2}".format(execution_elements[0], execution_elements[1], status))
    return execution_elements[0], execution_elements[1], status


def main():
    """
    Runner
    """
    args = parse_arguments()
    pool = Pool(args.processes)
    if args.tags:
        cmd = 'behave -d --no-junit --f json --no-summary --no-skipped -t {}'.format(
            ' -t '.join(args.tags))
    else:
        cmd = 'behave -d --no-junit --f json --no-summary --no-skipped'

    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()
    try:
        j = json.loads(out.decode())
    except ValueError:
        j = []
    # Identify all the feature files that have the tags
    features = [e['location'][:-2] for e in j]

    features_scenarios = []
    for scenario_elements in j:
        # Check if a feature file is reported with no matching scenario, if so skip it
        if 'elements' in scenario_elements:
            for i in scenario_elements['elements']:
                if i['keyword'].upper() in ["scenario".upper(), "scenario outline".upper()]:
                    # Build a list of filepaths for valid scenarios
                    features_scenarios.append(scenario_elements['location'][:-2] + delimiter
                                              + i['name'])

    logger.info("Found {} features".format(len(features)))
    logger.info("Found {} scenarios".format(len(features_scenarios)))

    if args.processes > len(features):
        logger.info("You have defined {} and will execute only necessary {} parallel process ".format(args.processes,
                                                                                                      len(features)))
    else:
        logger.info("Will execute {} parallel process".format(args.processes))

    run_feature = partial(_run_feature, tags=args.tags, userdata=args.define)
    logger.info(
        "--------------------------------------------------------------------------")
    output = 0
    failed_tests = passed_tests = []
    # https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-p
    for feature, scenario, status in pool.map_async(run_feature, features_scenarios).get(9999):
        if status == 'PASSED':
            passed_tests.append((feature, scenario, status))
        else:
            failed_tests.append((feature, scenario, status))

    #
    failed_tests_including_rerun = list(set(failed_tests) - set(passed_tests))
    # if output == 0:
    #     failed_tests.append((feature, scenario, status))
    #     if status == "FAILED":
    #         output = 1
    #     else:
    #         output = 2

    logger.info(
        "--------------------------------------------------------------------------")
    end_time = datetime.now()

    if failed_tests_including_rerun:
        output = 1
        for failed_test in failed_tests_including_rerun:
            logger.info(
                "{0:50}: {1} --> {2}".format(failed_test[0], failed_test[1], failed_test[2]))

    # if failed_tests:
    #     for failed_test in failed_tests:
    #         logger.info(
    #             "{0:50}: {1} --> {2}".format(failed_test[0], failed_test[1], failed_test[2]))

    logger.info("Duration: {}".format(format(end_time - start_time)))
    logger.info("Test Status: {0}".format(str(output)))

    sys.exit(output)
