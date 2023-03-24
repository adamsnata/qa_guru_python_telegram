import pytest
from allure_commons.types import Severity
from selene.support.shared import browser
import allure


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'xenia.r')
@allure.feature('Login')
@allure.link('https://github.com', name='Testing')
def test_passed_1():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


def test_passed_2():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


def test_passed_3():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


def test_passed_4():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


@pytest.mark.skip(reason='Ждет апдейт по фронту')
def test_skipped_1():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


@pytest.mark.skip(reason='Неактуален для прогона')
def test_skipped_2():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


@pytest.mark.skip(reason='Требуется доработать')
def test_skipped_3():
    browser.open('https://demoqa.com/automation-practice-form')
    pass


def test_failed_1():
    browser.open('https://demoqa.com/automation-practice-form')
    assert 1 == 0


def test_failed_2():
    browser.open('https://demoqa.com/automation-practice-form')
    assert 1 == 3
