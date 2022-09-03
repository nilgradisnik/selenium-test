from behave import fixture, use_fixture
from splinter import Browser

@fixture
def browser(context):
    context.browser = Browser('firefox')

    yield context.browser

    context.browser.quit()

def before_all(context):
    use_fixture(browser, context)
