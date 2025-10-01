import pytest
from selene import browser, be


@pytest.mark.parametrize("setup_browser", [(1920, 1080), (1600, 900)], indirect=True)
def test_indirect_desktop(setup_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.visible).click()


@pytest.mark.parametrize("setup_browser", [(375, 812), (393, 873)], indirect=True)
def test_indirect_mobile(setup_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link.HeaderMenu-button.js-prevent-focus-on-mobile-nav").should(be.visible).click()