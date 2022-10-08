from BaseApp import BasePage
from YandexPages import YandexSeacrhLocators, SearchHelper
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def test_yandex_search_tensor_two(browser):
    yandex_search = SearchHelper(browser)
    yandex_search.go_to_site()
    elements_bar = yandex_search.check_navigation_bar()
    print(elements_bar)
    assert 'Картинки' in elements_bar

    link_images_bar = yandex_search.find_element(YandexSeacrhLocators.LOCATOR_IMAGES)
    yandex_search.click_on_locator(link_images_bar)
    assert link_images_bar

    one_category_images_bar = yandex_search.go_to_site()

    time.sleep(3)
