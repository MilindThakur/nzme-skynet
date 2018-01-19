# coding=utf-8
import os
# from nzme_skynet.core.bdd.setupparser import Config
import logging.config
from datetime import datetime
import logging
import sys


class Logger(object):

    log = os.path.abspath('logs')

    @staticmethod
    def configure_logging():
        rl = logging.getLogger('')
        current_handlers = [n.name for n in rl.handlers]
        # Add custom handler for framework debugging using behave runner
        if not ['skynet_fh', 'skynet_sh'] in current_handlers:
            lf = '%(asctime)s [%(levelname)5s] [%(name)s]  %(message)s'
            rl.addHandler(Logger._file_handler(lf, rl.level))
            rl.addHandler(Logger._console_handler(lf, rl.level))

            for handler in rl.handlers:
                handler.addFilter(FilerOutSeleniumLogger())

    @staticmethod
    def create_test_folder(id):
        id = id.replace(' ', '_')
        report_dir = '{}/{}'.format(Logger.log, id)

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

    @staticmethod
    def _file_handler(log_format, logging_level):
        if not os.path.exists(Logger.log):
            os.mkdir(Logger.log)

        fh = logging.FileHandler(
            filename="{}/{}.txt".format(Logger.log, datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')), mode='w')
        fh.formatter = logging.Formatter(log_format)
        fh.setLevel(logging_level)
        fh.name = 'skynet_fh'
        return fh

    @staticmethod
    def _console_handler(log_format, logging_level):
        sh = logging.StreamHandler(stream=sys.stdout)
        sh.formatter = logging.Formatter(log_format)
        sh.setLevel(logging_level)
        sh.name = 'skynet_sh'
        return sh


class FilerOutSeleniumLogger(logging.Filter):
    def filter(self, record):
        return not'selenium' in record.name
