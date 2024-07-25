from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.price_elements = By.CLASS_NAME, "price"

    def navigate_to_page(self, url):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "plan-title")))

    def change_country_and_language(self, country, language):
        url = f"https://subscribe.stctv.com/{country.lower()}-{language.lower()}"
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "plan-title")))

    def get_subscription_packages(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".plan-title")

    def get_package_title(self, package_element):
        try:
            return package_element.text.strip()
        except Exception as e:
            self.logger.error("Failed to get package title", exc_info=True)
            raise e

    def get_price_elements(self):
        try:
            return self.driver.find_elements(*self.price_elements)
        except Exception as e:
            self.logger.error("Failed to get price elements", exc_info=True)
            raise e

    def get_package_price(self, price_element):
        try:
            return price_element.find_element(By.TAG_NAME, "b").text
        except Exception as e:
            self.logger.error("Failed to get package price", exc_info=True)
            raise e

    def get_package_currency(self, price_element):
        try:
            return price_element.find_element(By.TAG_NAME, "i").text.split("/")[0]
        except Exception as e:
            self.logger.error("Failed to get package currency", exc_info=True)
            raise e
        

        
    # def get_package_details(self, package_element):
    #     price_element = package_element.find_element(By.XPATH, "../following-sibling::div//b")
    #     currency_element = package_element.find_element(By.XPATH, "../following-sibling::div//i")
    #     return {
    #         "type": package_element.text.strip(),
    #         "price": price_element.text.strip(),
    #         "currency": currency_element.text.split("/")[0].strip()
    #     }
