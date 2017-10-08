# -*- coding: utf-8 -*-

from nzme_skynet.core.driver.enums.runenv import RunEnv
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
import logging
from nzme_skynet.core.driver.driverbuilder import DriverBuilder


class DriverFactory(object):

    def __init__(self):
        self._registered_driver_name = None
        self._run_env = RunEnv.LOCAL  # Run locally by default
        self._registered_driver = None
        self.logger = logging.getLogger(__name__)

    def register_driver(self, driver_name):
        if self._run_env == RunEnv.LOCAL:
            return self.register_local_driver(driver_name)
        elif self._run_env == RunEnv.REMOTE:
            return self.register_remote_driver(driver_name)
        raise Exception("Unknown driver type")

    def register_local_driver(self, driver_type, driver_options=None):
        try:
            builder = DriverBuilder(driver_type, driver_options, local=True)
            self._registered_driver = builder.build()
            self._registered_driver_name = driver_type
            self.logger.debug("Successfully registered local driver {0}".format(driver_type))
            return self._registered_driver
        except Exception:
            raise Exception("Unknown driver type")

    def register_remote_driver(self, driver_type, driver_options=None):
        try:
            builder = DriverBuilder(driver_type, driver_options, local=False)
            self._registered_driver = builder.build()
            self._registered_driver_name = driver_type
            self.logger.debug("Successfully registered remote driver {0}".format(driver_type))
            return self._registered_driver
        except Exception:
            raise Exception("Unknown driver")

    def get_driver(self):
        try:
            if self._registered_driver_name:
                return self.get_driver_by_name(self._registered_driver_name)
            # Register Chrome driver by default.
            self.register_driver(DriverTypes.CHROME)
            return self.get_driver_by_name('chrome')
        except Exception:
            raise Exception("Failed to get WebDriver")

    def get_driver_by_name(self, driver_name):
        if driver_name not in self._registered_driver_name:
            raise Exception("Cannot find Driver with name {0}".format(driver_name))
        try:
            if driver_name in self._registered_driver_name and self._registered_driver:
                return self._registered_driver
        except Exception:
            raise Exception("Driver {0} not registered".format(driver_name))

    def set_run_env(self, local=True):
        if local:
            self.logger.debug("Setting test env to local")
            self._run_env = RunEnv.LOCAL
        else:
            self.logger.debug("Setting test env to remote")
            self._run_env = RunEnv.REMOTE
