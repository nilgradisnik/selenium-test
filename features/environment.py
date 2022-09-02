from behave import fixture, use_fixture

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@fixture
def browser_firefox(context):
    context.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    yield context.browser

    context.browser.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
