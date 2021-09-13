from selenium import webdriver
import booking.constants as const
from selenium.webdriver.support.select import Select
from booking.booking_filters import BookingFilters

class Booking(webdriver.Chrome):
    def __init__(self,driver_path = const.CHROMEDRIVER_PATH ,stop= False):
        super(Booking,self).__init__(executable_path=driver_path)
        self.driver_path = driver_path
        self.stop = stop
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stop:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency = 'USD'):
       currency_button = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
       currency_button.click()
       e = self.find_element_by_css_selector(
           'a[data-modal-header-async-url-param="changed_currency=1;selected_currency=%s"]' % (currency)
       )
       e.click()

    def search_destiny(self,destiny = 'Barcelona'):
        input = self.find_element_by_id('ss')
        input.clear()
        input.send_keys(destiny)

        option = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        option.click()

    def checkin_and_checkout(self,checkin = "2021-09-10",checkout="2021-10-10"):
        checkin = self.find_element_by_css_selector(
            'td[data-date="%s"]' % checkin
        )
        checkin.click()
        checkout = self.find_element_by_css_selector(
            'td[data-date="%s"]' % checkout
        )
        checkout.click()

    def guests(self,adults=5,children=2,child_ages=[9,10],rooms=2):
        click = self.find_element_by_css_selector(
            'div[data-component="search/group/group-with-modal"]'
        )
        click.click()

        ##Set number of adults to 1
        less_adults = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        while self.find_element_by_id("group_adults").get_attribute("value") != "1":
            less_adults.click()

        ##Increase adults
        more_adults = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(adults-1):
            more_adults.click()

        ##Increase children
        more_children = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Children"]'
        )
        for i,val in enumerate(child_ages):
            more_children.click()
            select_item = self.find_element_by_css_selector(
                'select[data-group-child-age="%s"]' % i
            )
            select_object = Select(select_item)
            select_object.select_by_value("%s" % val)

        #Rooms
        more_rooms = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )

        for i in range(rooms-1):
            more_rooms.click()

    def search(self):
       search =  self.find_element_by_css_selector(
            'button[data-sb-id="main"]'
        )
       search.click()

    def apply_filters(self):
        filter = BookingFilters(driver=self)
        filter.best_score()
        filter.cheapest_hotel()