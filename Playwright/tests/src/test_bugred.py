import re
from config import *
from playwright.sync_api import Page, expect

def test_registration_page(page: Page):
    page.goto("http://users.bugred.ru")
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name='name']").fill(login)
    page.locator("input[name='email']").fill(email)
    page.locator("tbody").filter(has_text="Имя Email").locator("input[name='password']").fill(password)
    page.get_by_role("button", name="Зарегистрироваться").click()

def test_autorization_page(page: Page):
    page.goto("http://users.bugred.ru")
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name='login']").fill(email)
    page.locator("tbody").filter(has_text="Email Пароль Авторизоваться").locator("input[name='password']").fill(password)
    page.get_by_role("button", name="Авторизоваться").click()
    expect(page.get_by_role("link", name = "Компании")).to_be_visible()
    page.wait_for_load_state('domcontentloaded')
    page.get_by_placeholder("Введите email или имя").fill("0@gmail.com")
    page.get_by_role("button", name="Найти").click()
    page.get_by_role("row", name="@gmail.com kate Посмотреть").get_by_role("link").click()
    expect(page.get_by_role("cell", name="@gmail.com")).to_be_visible()


    #pytest -k test_bugred --headed
