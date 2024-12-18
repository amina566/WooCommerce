from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from PageObject.woocommerce_locator import ProductLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

    def shopproduct(self):
        element = self.driver.find_element(*ProductLocators.SHOP_PRODUCT_TEXT)
        actual_text = element.text
        expected_text = "Shop"
        assert actual_text == expected_text, f"Text mismatch: Found '{actual_text}', expected '{expected_text}'"
        print("Assertion passed: Text is 'Shop'")
        time.sleep(3)

    def add_to_cart(self):
        self.driver.find_element(*ProductLocators.ADD_TO_CART_BUTTON).click()

    def view_cart(self):
        wait = WebDriverWait(self.driver, 10)
        view_cart_button = wait.until(EC.element_to_be_clickable(ProductLocators.view_cart))
        view_cart_button.click()

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

    def continue_payment(self):
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*ProductLocators.PLACE_ORDER_BUTTONS)
        )

        # Wait until the button is clickable
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(*ProductLocators.PLACE_ORDER_BUTTON)
        )

        place_order_button.click()
        time.sleep(120)



    # Method to fill payment details
    def fill_payment_details(self, cardholder_name, card_number, expiration_date, cvv):
        try:

            print("Locating iframe...")
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ProductLocators.PAYMENT_IFRAME)
            )
            self.driver.switch_to.frame(iframe)
            print("Switched to payment iframe.")

            wait = WebDriverWait(self.driver, 10)

            # Fill the Cardholder Name
            cardholder_name_field = wait.until(EC.element_to_be_clickable(*ProductLocators.cardholder_name_locator))
            cardholder_name_field.clear()
            cardholder_name_field.send_keys(cardholder_name)

            # Fill the Card Number
            card_number_field = wait.until(EC.element_to_be_clickable(*ProductLocators.card_number_locator))
            card_number_field.clear()
            card_number_field.send_keys(card_number)

            # Fill the Expiration Date
            expiration_date_field = wait.until(EC.element_to_be_clickable(*ProductLocators.expiration_date_locator))
            expiration_date_field.clear()
            expiration_date_field.send_keys(expiration_date)

            # Fill the CVV
            cvv_field = wait.until(EC.element_to_be_clickable(*ProductLocators.cvv_locator))
            cvv_field.clear()
            cvv_field.send_keys(cvv)
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
        try:
            # Check for iframe context (if applicable)
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*ProductLocators.IFRAME_XPATH)
            )
            self.driver.switch_to.frame(iframe)
            print("Switched to iframe.")

            # Wait for the button to become clickable
            wait = WebDriverWait(self.driver, 10)
            checkout_button = wait.until(EC.element_to_be_clickable(*ProductLocators.IFRAMES))
            checkout_button.click()
            print("Checkout button clicked.")

            # Switch back to the main content
            self.driver.switch_to.default_content()

        except TimeoutException:
            print("Timeout: Unable to locate the Checkout button.")
        except NoSuchElementException:
            print("NoSuchElementException: The Checkout button could not be found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def create_order(self):
        element = self.driver.find_element(*ProductLocators.VERIFICATION)
        actual_text = element.text
        expected_text = "Thank you. Your order has been received."
        assert actual_text == expected_text, f"Text mismatch: Found '{actual_text}', expected '{expected_text}'"
        print("Assertion passed: Text is 'Thank you. Your order has been received.'")








