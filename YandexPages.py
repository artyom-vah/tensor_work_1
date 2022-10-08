from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class YandexSeacrhLocators:
    #локаторы для 1го теста (test_yandex_search_tensor_one):
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CLASS_NAME, "input__control.mini-suggest__input")
    LOCATOR_YANDEX_SAGGEST = (By.CSS_SELECTOR, '.mini-suggest__item')
    LOCATOR_YANDEX_LINKS = (By.CLASS_NAME, 'Path.Organic-Path')
    LOCATOR_LINK_ONE_TENSOR = (By.CLASS_NAME, 'Path.Organic-Path.Organic-Path_verified')

    #локаторы для 2го теста(test_yandex_search_tensor_two):
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_IMAGES = (By.CLASS_NAME, 'navigation__item.navigation__item_name_images')

    LOCATOR_IMG_BAR_ONE = (By.CLASS_NAME, 'PopularRequestList-Shadow')


    # LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")

class SearchHelper(BasePage):


    def enter_word(self, word):
        '''ищет элемент строки поиска, кликает
        и вводит в поиск необходимое слово'''
        search_field = self.find_element(
            YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    # def click_on_the_search_button(self):
    #     '''ищет элемент кнопки поиска и кликает на неё'''
    #     return self.find_element(
    #         YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        '''ищет элементы навигации и получает атрибут text.
        Создает список и фильтрует по условию'''
        all_list = self.find_elements(
            YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_saggest(self):
        '''Ищет таблицу с подсказками (suggest)'''
        list = self.find_elements(
            YandexSeacrhLocators.LOCATOR_YANDEX_SAGGEST, time=2)
        sag_list = [x.text for x in list if len(x.text) > 0]
        return sag_list

    def check_all_link(self):
        '''Ищет линки на странице'''
        list = self.find_elements(
            YandexSeacrhLocators.LOCATOR_YANDEX_LINKS, time=2)
        sag_list = [x.text for x in list if len(x.text) > 0]
        return sag_list

    def click_images(self):
        '''кликает на "картинки" в баре яндекса'''
        return self.find_element(
            YandexSeacrhLocators.LOCATOR_IMAGES, time=2).click()

