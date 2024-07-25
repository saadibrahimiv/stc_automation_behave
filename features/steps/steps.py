from behave import given, when, then
from features.support.page_objects import SubscriptionPage
from utils.logger import setup_logger
from utils.config import load_config
from utils.browser_factory import get_browser_instance

logger = setup_logger()
config = load_config()
print(load_config)

def initialize_browser(browser_name):
    driver = get_browser_instance(browser_name, config)
    return driver

@given('I navigate to the STC TV subscription page')
def step_impl(context):
    context.browsers = config['browsers'].keys() 
    context.pages = {}
    context.drivers = {}

    for browser in context.browsers:
        context.drivers[browser] = initialize_browser(browser)
        context.pages[browser] = SubscriptionPage(context.drivers[browser])
        context.pages[browser].navigate_to_page(config['default']['base_url'])
        logger.info(f"Navigated to STC TV subscription page using {browser} browser")

@when('I change the country to "{country}" and language to "{language}"')
def step_impl(context, country, language):
    for browser in context.browsers:
        context.pages[browser].change_country_and_language(country, language)
        logger.info(f"Changed country to {country} and language to {language} using {browser} browser")

@then('I should see the following subscription packages')
def step_impl(context):
    for browser in context.browsers:
        for row in context.table:
            package_type = row['Type']
            expected_price = row['Price']
            expected_currency = row['Currency']

            package_elements = context.pages[browser].get_subscription_packages()
            price_elements = context.pages[browser].get_price_elements()

            for package_element, price_element in zip(package_elements, price_elements):
                details = {
                    "type": context.pages[browser].get_package_title(package_element),
                    "price": context.pages[browser].get_package_price(price_element),
                    "currency": context.pages[browser].get_package_currency(price_element)
                }
                if details["type"] == package_type:
                    assert details["price"] == expected_price, f"Expected price for {package_type} is {expected_price} but got {details['price']} using {browser} browser"
                    assert details["currency"] == expected_currency, f"Expected currency for {package_type} is {expected_currency} but got {details['currency']} using {browser} browser"
                    logger.info(f"Validated package {package_type} with price {expected_price} and currency {expected_currency} using {browser} browser")

    for browser in context.browsers:
        context.drivers[browser].quit()


# from behave import given, when, then
# from features.support.page_objects import SubscriptionPage
# from utils.logger import setup_logger
# from utils.config import load_config
# from utils.browser_factory import get_browser_instance

# logger = setup_logger()
# config = load_config()
# print(config)


# def initialize_browser(browser_name):
#     driver = get_browser_instance(browser_name, config)
#     return driver

# @given('I navigate to the STC TV subscription page')
# def step_impl(context):
#     default_config = config['default']
#     context.driver = get_browser_instance(default_config['browser'], config)
#     context.page = SubscriptionPage(context.driver)
#     context.page.navigate_to_page(default_config['base_url'])
#     logger.info("Navigated to STC TV subscription page")

# @when('I change the country to "{country}" and language to "{language}"')
# def step_impl(context, country, language):
#     context.page.change_country_and_language(country, language)
#     context.country = country
#     context.language = language
#     logger.info(f"Changed country to {country} and language to {language}")

# @then('I should see the following subscription packages')
# def step_impl(context):
#     for row in context.table:
#         package_type = row['Type']
#         expected_price = row['Price']
#         expected_currency = row['Currency']
        
#         package_elements = context.page.get_subscription_packages()
#         price_elements = context.page.get_price_elements()

#         for package_element, price_element in zip(package_elements, price_elements):
#             details = {
#                 "type": context.page.get_package_title(package_element),
#                 "price": context.page.get_package_price(price_element),
#                 "currency": context.page.get_package_currency(price_element)
#             }

#             if details["type"] == package_type:
#                 assert details["price"] == expected_price, f"Expected price for {package_type} is {expected_price} but got {details['price']}"
#                 assert details["currency"] == expected_currency, f"Expected currency for {package_type} is {expected_currency} but got {details['currency']}"
#                 logger.info(f"Validated package {package_type} with price {expected_price} and currency {expected_currency}")

#     context.driver.quit()