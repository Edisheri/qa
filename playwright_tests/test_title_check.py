import pytest
from playwright.sync_api import sync_playwright

EXPECTED_TITLE = "Fast and reliable end-to-end testing for modern web apps | Playwright"

@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_playwright_title(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        assert page.title() == EXPECTED_TITLE, f"Заголовок не совпадает в {browser_type}"
        browser.close()