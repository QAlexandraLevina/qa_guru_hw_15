import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1440, 900), (1366, 768), (360, 800), (390, 844), (375, 812), (393, 873)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1000:
        yield "Desktop"
    else:
        yield "Mobile"

    browser.quit()


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1440, 900), (1366, 768)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(360, 800), (390, 844), (375, 812), (393, 873)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()