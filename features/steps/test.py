from behave import *

@given('load the page')
def step_impl(context):
    context.browser.visit("https://www.selenium.dev/selenium/web/web-form.html")

    assert context.browser.title == "Web form"

@when('submit a form')
def step_impl(context):
    input = context.browser.find_by_name("my-text")
    input.fill("Selenium test!")

    button = context.browser.find_by_css("button")
    button.click()

@then('expect success')
def step_impl(context):
    message = context.browser.find_by_id("message")

    assert message.text == "Received!"
