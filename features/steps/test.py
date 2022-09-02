from behave import *
from selenium.webdriver.common.by import By

@given('load the page')
def step_impl(context):
    context.browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    assert context.browser.title == "Web form"

@when('submit a form')
def step_impl(context):
    input = context.browser.find_element(by=By.NAME, value="my-text")
    input.send_keys("Selenium test!")

    submit_button = context.browser.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

@then('expect success')
def step_impl(context):
    message = context.browser.find_element(by=By.ID, value="message")

    assert message.text == "Received!"
