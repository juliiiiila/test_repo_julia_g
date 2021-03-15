class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = 'https://vk.com/'

    def open_base_page(self):
        self.driver.get(self.base_page)
