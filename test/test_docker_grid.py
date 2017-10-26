import pytest

from nzme_skynet.core.driver.driverregistry import DriverRegistry

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"


@pytest.fixture(scope='module', params=["chrome", "firefox"])
def driver_setup(request):
    DriverRegistry.register_driver(driver_type=request.param, local=False)
    driver = DriverRegistry.get_driver()
    yield driver
    DriverRegistry.deregister_driver()


def test_browser_setup(driver_setup):
    driver_setup.goto_url(TEST_URL, absolute=True)
    assert (TEST_URL in driver_setup.current_url) is True
