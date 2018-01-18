# coding=utf-8
import os
from setupparser import Config
import logging.config
from datetime import datetime
import logging
import sys

logger = logging.getLogger(__name__)


class Logger(object):
    @staticmethod
    def configure_logging():
        if not os.path.exists(Config.LOG):
            os.mkdir(Config.LOG)

        rl = logging.getLogger('')
        lf = '%(asctime)s [%(levelname)5s] [%(name)s]  %(message)s'
        rl.addHandler(Logger.file_handler(lf, rl.level))
        rl.addHandler(Logger.console_handler(lf, rl.level))

        for handler in rl.handlers:
            handler.addFilter(FilerOutSeleniumLogger())

    @staticmethod
    def create_test_folder(id):
        id = id.replace(' ', '_')
        report_dir = '{}/{}'.format(Config.LOG, id)

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

    @staticmethod
    def file_handler(log_format, logging_level):
        fh = logging.FileHandler(
            filename="{}/{}.txt".format(Config.LOG, datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')), mode='w')
        fh.formatter = logging.Formatter(log_format)
        fh.setLevel(logging_level)
        return fh

    @staticmethod
    def console_handler(log_format, logging_level):
        sh = logging.StreamHandler(stream=sys.stdout)
        sh.formatter = logging.Formatter(log_format)
        sh.setLevel(logging_level)
        return sh


class FilerOutSeleniumLogger(logging.Filter):
    def filter(self, record):
        return not'selenium' in record.name
