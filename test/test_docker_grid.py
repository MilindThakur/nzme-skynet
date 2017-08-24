import pytest
from nzme_skynet.core.app import appbuilder

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"


@pytest.fixture(scope='module', params=["chrome", "firefox"])
def driver_setup(request):
    cap = {
        "browserName": request.param,
        "platformName":"",
        "platform": 'LINUX',
        "version": '',
        "javascriptEnabled": True
    }
    try:
        app = appbuilder.build_docker_browser(DOCKER_SELENIUM_URL, cap, TEST_URL)
        yield app
    except Exception:
        raise
    app.quit()


def test_browser_setup(driver_setup):
    assert driver_setup.baseurl == TEST_URL
    assert (TEST_URL in driver_setup.get_current_url()) is True

