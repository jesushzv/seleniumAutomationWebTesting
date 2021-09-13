import string
import re

from selenium.webdriver.remote.webdriver import WebDriver

class BookingFilters():
    def __init__(self,driver):
        # type: (WebDriver) -> None
        self.driver = driver
        self.hotel_list = self.driver.find_elements_by_css_selector(
            'div[data-et-click="customGoal:NAREFBINEIfBccOHT:2"]'
        )

    def best_score(self):
        hotel_id = ''
        max_score = 0

        for hotel in self.hotel_list:
            score = hotel.get_attribute("data-score")
            id = hotel.get_attribute("data-hotelid")
            if score > max_score:
                max_score = score
                hotel_id=id

        best_hotel = self.driver.find_element_by_css_selector(
            'div[data-hotelid="%s"]' % hotel_id
        )
        best_hotel_name = best_hotel.find_element_by_class_name("sr-hotel__name").text
        print('The best hotel is:', best_hotel_name, " with a score of:", max_score)

    def cheapest_hotel(self):

        hotels = {}

        for hotel in self.hotel_list:
            price = hotel.find_element_by_class_name("prco-valign-middle-helper").text
            price  = re.sub('\D','',price)
            name = hotel.find_element_by_class_name("sr-hotel__name").text
            hotels[name] = price

        lowest = min(hotels,key=hotels.get)

        print('The cheapest hotel is: ', lowest, ' going for: ', hotels[lowest])



