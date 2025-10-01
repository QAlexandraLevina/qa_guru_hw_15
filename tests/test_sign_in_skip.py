import pytest
from selene import browser, be



def test_desktop_skip(setup_browser):
    if setup_browser != "Desktop":
        pytest.skip("Пропуск тестов для мобильной версии сайта")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.visible).click()


def test_mobile_skip(setup_browser):
    if setup_browser != "Mobile":
        pytest.skip("Пропуск тестов для десктопной версии сайта")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link.HeaderMenu-button.js-prevent-focus-on-mobile-nav").should(be.visible).click()