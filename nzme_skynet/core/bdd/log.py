# coding=utf-8
# coding=utf-8
import os
from setupparser import Config
import logging.config
from datetime import datetime

class Logger(object):

    @staticmethod
    def configure_logging():
        if not os.path.exists(Config.LOG):
            os.mkdir(Config.LOG)

        logging.config.fileConfig('log.ini', defaults={'logdir': Config.LOG,
                                                       'datetime': str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f'))})

    @staticmethod
    def create_test_folder(id):
        id = id.replace(' ', '_')
        report_dir = '{}/{}'.format(Config.LOG, id)

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
