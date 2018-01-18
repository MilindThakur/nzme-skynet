# coding=utf-8
import os
from setupparser import Config
import logging.config
from datetime import datetime
import logging
import sys

logger = logging.getLogger(__name__)
class Logger(object):

    # @staticmethod
    # def configure_logging():
    #     if not os.path.exists(Config.LOG):
    #         os.mkdir(Config.LOG)
    #
    #     behave_log_capture = None
    #     # Saving behave log capture as it is wiped when loading log.ini
    #     for handler in logging.Logger.root.handlers:
    #             if 'behave' in handler.__module__:
    #                 behave_log_capture = logging.Logger.root.handlers[0]
    #
    #
    #     logging.config.fileConfig('log.ini', defaults={'logdir': Config.LOG, 'datetime': str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f'))})
    #     # logging.config.dictConfig()
    #
    #     # Adding behave log capture back into the handlers
    #     if behave_log_capture is not None:
    #         logging.Logger.root.handlers.append(behave_log_capture)
    #         for handler in logging.Logger.root.handlers:
    #             if 'behave' in handler.__module__:
    #                 handler.level = logging.Logger.root.level

    @staticmethod
    def configure_logging():
        if not os.path.exists(Config.LOG):
            os.mkdir(Config.LOG)

        # Adding our handlers to the rool logger
        rl = logging.getLogger('')
        lf = '%(asctime)s [%(levelname)5s] [%(name)s]  %(message)s'
        rl.addHandler(Logger.file_handler(lf, rl.level))
        rl.addHandler(Logger.console_handler(lf, rl.level))

        #Adding filters to Root logger and handlers
        rl.addFilter(rl.addFilter(filer_out_selenium_logger))
        for handler in rl.handlers:
            handler.addFilter(filer_out_selenium_logger())

    @staticmethod
    def create_test_folder(id):
        id = id.replace(' ', '_')
        report_dir = '{}/{}'.format(Config.LOG, id)

        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

    @staticmethod
    def file_handler(log_format, logging_level):
        # filename, mode = 'a', encoding = None, delay = 0):
        # '%(logdir)s' + os.sep + r'test_log_%(datetime)s.txt
        fh = logging.FileHandler(filename="{}/{}.txt".format(Config.LOG, datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')), mode='w')
        fh.formatter = logging.Formatter(log_format)
        fh.setLevel(logging_level)
        return fh
    
    @staticmethod
    def console_handler(log_format, logging_level):
        # formatter = ConsoleFormatter
        # args = (sys.stdout,)
        sh = logging.StreamHandler(stream=sys.stdout)
        sh.formatter = logging.Formatter(log_format)
        sh.setLevel(logging_level)
        return sh


class filer_out_selenium_logger(logging.Filter):
    def filter(self, record):
        return not 'selenium' in record.name
