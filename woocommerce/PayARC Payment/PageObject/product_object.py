from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from PageObject.product_locator import ProductLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime

class ProductPage:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(10)

    def shopbutton(self):
        self.driver.find_element(*ProductLocators.SHOP_BUTTON).click()
        time.sleep(10)

    def shopproduct(self):
        element = self.driver.find_element(*ProductLocators.SHOP_PRODUCT_TEXT)
        actual_text = element.text
        expected_text = "Shop"
        assert actual_text == expected_text, f"Text mismatch: Found '{actual_text}', expected '{expected_text}'"
        print("Assertion passed: Text is 'Shop'")
        time.sleep(3)

    def add_to_cart(self):
        assert self.driver.find_element(*ProductLocators.PRODUCTS_NAME).is_displayed(), "Product name not visible"
        assert self.driver.find_element(*ProductLocators.PRODUCTS_PRICE).is_displayed(), "Product price not visible"
        self.driver.find_element(*ProductLocators.ADD_TO_CART_BUTTON).click()

    def carticon(self):
        self.driver.find_element(*ProductLocators.CART_ICON).click()

    def get_product_name(self):
        product_name_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductLocators.PRODUCT_NAME)
        )
        return product_name_element.text.strip()

    def get_product_quantity(self):
        quantity_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductLocators.PRODUCT_QUANTITY)
        )
        return quantity_element.get_attribute("value").strip()

    def get_product_price(self):
        price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ProductLocators.PRODUCT_PRICE)
        )
        return price_element.text.strip()

    def checkoutbutton(self):
        self.driver.find_element(*ProductLocators.CHECKOUT_BUTTON).click()

    def checkoutpage(self):
        element = self.driver.find_element(*ProductLocators.CHECKOUT_PAGE_TEXT)
        actual_text = element.text
        expected_text = "WooCommerce"
        assert actual_text == expected_text, f"Text mismatch: Found '{actual_text}', expected '{expected_text}'"
        print("Assertion passed: Text is 'WooCommerce'")


    def fill_billing_details(self, first_name, last_name, country_region, street_address, town_city, postcode, phone,email_address):
        # Fill First Name
        self.driver.find_element(*ProductLocators.BILLING_FIRST_NAME).clear()
        self.driver.find_element(*ProductLocators.BILLING_FIRST_NAME).send_keys(first_name)

        self.driver.find_element(*ProductLocators.BILLING_LAST_NAME).clear()
        self.driver.find_element(*ProductLocators.BILLING_LAST_NAME).send_keys(last_name)

        country_dropdown = Select(self.driver.find_element(*ProductLocators.BILLING_COUNTRY))
        country_dropdown.select_by_visible_text(country_region)

        self.driver.find_element(*ProductLocators.BILLING_ADDRESS_1).clear()
        self.driver.find_element(*ProductLocators.BILLING_ADDRESS_1).send_keys(street_address)

        self.driver.find_element(*ProductLocators.BILLING_CITY).clear()
        self.driver.find_element(*ProductLocators.BILLING_CITY).send_keys(town_city)

        self.driver.find_element(*ProductLocators.BILLING_POSTCODE).clear()
        self.driver.find_element(*ProductLocators.BILLING_POSTCODE).send_keys(postcode)
        self.driver.find_element(*ProductLocators.BILLING_PHONE).send_keys(phone)
        self.driver.find_element(*ProductLocators.BILLING_EMAIL).clear()
        self.driver.find_element(*ProductLocators.BILLING_EMAIL).send_keys(email_address)


    def get_order_details(self):
        product_name = self.driver.find_element(*ProductLocators.Order_PRODUCT_NAME).text.strip()
        subtotal = self.driver.find_element(*ProductLocators.SUBTOTAL).text.strip()
        shipping = self.driver.find_element(*ProductLocators.SHIPPING).text.strip()
        total = self.driver.find_element(*ProductLocators.TOTAL).text.strip()

        return {
            "Product Name": product_name,
            "Subtotal": subtotal,
            "Shipping": shipping,
            "Total": total,
        }

    def get_payment_methods(self):

        payment_methods_elements = self.driver.find_elements(*ProductLocators.PAYMENT_METHODS)
        return [method.text.strip() for method in payment_methods_elements]

    def payarc_checkout(self):
        radio_button = self.driver.find_element(*ProductLocators.PAYARC_PAYMENT_METHOD)
        if not radio_button.is_selected():
            radio_button.click()
        time.sleep(6)

    def continue_payment(self):
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*ProductLocators.PLACE_ORDER_BUTTON)
        )

        # Wait until the button is clickable
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*ProductLocators.PLACE_ORDERS_BUTTON)
        )

        place_order_button.click()
        time.sleep(120)


    def fill_payment_details(self, card_number, expiration_date, cvc_cvv, first_name, last_name, address_line1, address_line2, city, state, zip_code, email_address):
        try:

            print("Locating iframe...")
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*ProductLocators.PAYMENT_IFRAME)
            )
            self.driver.switch_to.frame(iframe)
            print("Switched to payment iframe.")

            # Fill Card Number
            card_number_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*ProductLocators.CARD_NUMBER_FIELD)
            )
            card_number_field.send_keys(card_number)

            # Fill Expiration Date
            expiration_date_field = self.driver.find_element(*ProductLocators.EXPIRATION_DATE_FIELD)
            expiration_date_field.clear()
            expiration_date_field.send_keys(expiration_date)

            # Fill CVC/CVV
            cvc_cvv_field = self.driver.find_element(*ProductLocators.CVC_CVV_FIELD)
            cvc_cvv_field.clear()
            cvc_cvv_field.send_keys(cvc_cvv)

            # Fill First Name
            first_name_field = self.driver.find_element(*ProductLocators.FIRST_NAME_FIELD)
            first_name_field.clear()
            first_name_field.send_keys(first_name)

            # Fill Last Name
            last_name_field = self.driver.find_element(*ProductLocators.LAST_NAME_FIELD)
            last_name_field.clear()
            last_name_field.send_keys(last_name)

            # Fill Address Line 1
            address_line1_field = self.driver.find_element(*ProductLocators.ADDRESS_LINE1_FIELD)
            address_line1_field.clear()
            address_line1_field.send_keys(address_line1)

            # Fill Address Line 2
            address_line2_field = self.driver.find_element(*ProductLocators.ADDRESS_LINE2_FIELD)
            address_line2_field.clear()
            address_line2_field.send_keys(address_line2)

            # Fill City
            city_field = self.driver.find_element(*ProductLocators.CITY_FIELD)
            city_field.clear()
            city_field.send_keys(city)

            wait = WebDriverWait(self.driver, 20)
            state_dropdown = wait.until(
                EC.element_to_be_clickable(*ProductLocators.Status_FIELD)
            )
            state_dropdown.click()
            state_locator = (ProductLocators.STATE_DROPDOWN[0], ProductLocators.STATE_DROPDOWN[1].format(state))
            state_option = wait.until(
                EC.element_to_be_clickable(state_locator)
            )
            state_option.click()

            # Fill ZIP Code
            zip_code_field = self.driver.find_element(*ProductLocators.STATE_OPTION)
            zip_code_field.clear()
            zip_code_field.send_keys(zip_code)

            # Fill Email Address
            email_field = self.driver.find_element(*ProductLocators.ZIP_CODE_FIELD)
            email_field.clear()
            email_field.send_keys(email_address)

            print("Payment details filled successfully.")

        except TimeoutException as te:
            print("TimeoutException: Unable to locate an element. Please verify the locators.")
            raise te
        except NoSuchElementException as nse:
            print("NoSuchElementException: Element not found. Please verify the iframe or element locators.")
            raise nse
        finally:
            # Always switch back to the main content
            self.driver.switch_to.default_content()
            print("Switched back to the main content.")


    def click_button(self):
        self.driver.find_element(*ProductLocators.PAY_BUTTON).click()






