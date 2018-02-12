# coding=utf-8
import os
import logging.config
from datetime import datetime
import logging
import sys
from behave.log_capture import LoggingCapture


class Logger(object):

    log = os.path.abspath('logs')
    behave = False

    @staticmethod
    def configure_logging():
        # Get the root logger
        rl = logging.getLogger('')

        for log_handler in rl.handlers:
            lf = '%(asctime)s [%(levelname)5s] [%(name)s]  %(message)s'
            # Set the file and console handler for behave tests
            # The behave log level is read from behave.ini or overridden at cli
            if isinstance(log_handler, LoggingCapture):
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


# Filter out the selenium level logs, retain only the tests and FW level logs
# TODO: expose selenium logging in a separate log file
class FilerOutSeleniumLogger(logging.Filter):
    def filter(self, record):
        return not'selenium' in record.name
