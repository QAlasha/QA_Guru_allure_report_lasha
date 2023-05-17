import allure
from allure_commons.types import Severity
from selene import browser, be, by


def test_github():
    browser.open('https://github.com')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#81')).should(be.visible)


def test_github_dynamic_steps():
    with allure.step('Open base page'):
        browser.open('https://github.com')

    with allure.step('Search repository'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Go to the repository link'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open tab Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Check availability Issue is number 81'):
        browser.element(by.partial_text('#81')).should(be.visible)


def test_github_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#81')


@allure.step('Open base page')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Search repository {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Go to the repository link {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open tab Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Check availability Issue {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)


def test_github_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Task is repository')
    allure.dynamic.story('log in to create a task')
    allure.dynamic.link('https://github.com', name='Testing')


@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Victor')
@allure.feature('Task')
@allure.story('An authorized user can create a task in the repository')
@allure.link('https://github.com', name='Testing')
def test_github_decorator_lables():
    pass
    ...
