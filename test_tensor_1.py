from YandexPages import YandexSeacrhLocators, SearchHelper
from selenium.webdriver import Keys
import time

def test_yandex_search_tensor_one(browser):
    yandex_search = SearchHelper(browser)
    assert yandex_search
    yandex_search.go_to_site()
    yandex_search.enter_word("Тензор")
    suggest = yandex_search.check_saggest()
    print(suggest)
    assert "тензор" in suggest
    yandex_search.enter_word(Keys.ENTER)
    links = yandex_search.check_all_link()
    print(links)

    '''тест не пройдет если 1 ссылка будет не tensor.ru'''
    assert links[0] == 'tensor.ru'
    link1 = yandex_search.find_element(YandexSeacrhLocators.LOCATOR_LINK_ONE_TENSOR)
    yandex_search.click_on_locator(link1)

    time.sleep(2)






