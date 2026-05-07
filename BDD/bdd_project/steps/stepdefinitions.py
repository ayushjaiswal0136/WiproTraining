import time

from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given(u'buyer is on the OLX homepage')
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get("https://www.olx.in/")
    time.sleep(2)

@when(u'buyer types product in searchbar')
def step_impl(context):
    searchbar = context.driver.find_element(By.XPATH, "//input[@data-aut-id='searchBox']")
    searchbar.send_keys("Cars")
    time.sleep(2)

    list_click = context.driver.find_element(By.XPATH, "//li[@data-aut-id='searchSuggestionItem']")
    list_click.click()
    time.sleep(1)

@then(u'search results should be displayed')
def step_impl(context):
    assert context.driver.title.__contains__("Cars") and context.driver.url.__contains__("cars"), 'search failed!'

    heading = context.driver.find_element(By.CSS_SELECTOR, "#main_content > div > div > section > div > div > h1")
    assert heading.text.__contains__("Cars"), 'Search Failed'