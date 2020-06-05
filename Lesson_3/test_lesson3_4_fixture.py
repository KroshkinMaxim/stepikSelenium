import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, page):
    link = f"{page}"
    browser.get(link)
    browser.implicitly_wait(12)
    input1 = browser.find_element_by_xpath('//textarea[@placeholder="Напишите ваш ответ здесь..."]')
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    output = browser.find_element_by_xpath("//pre[@class='smart-hints__hint']").text
    assert output == "Correct!" , f"Actual {output}"
