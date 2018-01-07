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

        behave_log_capture = None
        # Saving behave log capture as it is wiped when loading log.ini
        for handler in logging.Logger.root.handlers:
                if 'behave' in handler.__module__:
                    behave_log_capture = logging.Logger.root.handlers[0]

        logging.config.fileConfig('log.ini', defaults={'logdir': Config.LOG,
                                                       'datetime': str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f'))})

        # Adding behave log capture back into the handlers
        if behave_log_capture is not None:
            logging.Logger.root.handlers.append(behave_log_capture)
            for handler in logging.Logger.root.handlers:
                if 'behave' in handler.__module__:
                    handler.level = logging.Logger.root.level

    @staticmethod
    def create_test_folder(id):
        id = id.replace(' ', '_')
        report_dir = '{}/{}'.format(Config.LOG, id)

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
