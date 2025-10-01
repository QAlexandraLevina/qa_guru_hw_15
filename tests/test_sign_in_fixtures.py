from selene import browser, be


def test_desktop_fixtures(desktop_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.visible).click()


def test_mobile_fixtures(mobile_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link.HeaderMenu-button.js-prevent-focus-on-mobile-nav").should(be.visible).click()