import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://demo.opencart.com/admin")
    page.wait_for_event('load')
    page.get_by_placeholder("Username").fill("demo")
    page.get_by_placeholder("Password").fill("demo")
    page.get_by_role("button").click()
    page.wait_for_timeout(3000)
    expect(page.get_by_role("heading", name = "Dashboard")).to_be_visible()