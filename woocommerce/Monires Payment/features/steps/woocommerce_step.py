from behave import *
from PageObject.woocommerce_object import ProductPage
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
product_page = ProductPage()
@given(u'I open the shop page')
def open_login(context):
    product_page.set_driver(context.driver)
    woocommerce_url = os.getenv('WOOCOMMERCE_URL')
    if woocommerce_url:
        product_page.open_page(woocommerce_url)
    else:
        print("URL is not set in the environment variables!")

@when(u'I should see a product displayed')
def see_shop_product(context):
    product_page.shopproduct()

@when(u'I click on the Add to Cart button')
def addto_cart(context):
    product_page.add_to_cart()

@when(u'I click on the view cart button')
def cart_icon(context):
    product_page.view_cart()

@then(u'I click on the Go to Checkout button')
def go_to_checkout_button(context):
    product_page.checkoutbutton()

@then(u'the checkout page open')
def checkout_page(context):
    product_page.checkoutpage()


@when(u'I fill in the billing details')
def fill_billing_details(context):
    for row in context.table:
        first_name = row["First Name"]
        last_name = row["Last Name"]
        country_region = row["Country / Region"]
        street_address = row["Street Address"]
        town_city = row["Town / City"]
        postcode = row["Postcode"]
        phone = row["Phone"]
        email_address = row["Email Address"]

        product_page.fill_billing_details(first_name, last_name, country_region, street_address, town_city, postcode, phone, email_address)

@when(u'I should see the Your Order table')
def verify_order_table(context):
    for row in context.table:
        product_name = row["Product Name"]
        subtotal = row["Subtotal"]
        shipping = row["Shipping"]
        total = row["Total"]

        actual_details = product_page.get_order_details()
        assert product_name == actual_details["Product Name"], f"Expected product name '{product_name}', but got '{actual_details['Product Name']}'"
        assert subtotal == actual_details["Subtotal"], f"Expected subtotal '{subtotal}', but got '{actual_details['Subtotal']}'"
        assert shipping == actual_details["Shipping"], f"Expected shipping '{shipping}', but got '{actual_details['Shipping']}'"
        assert total == actual_details["Total"], f"Expected total '{total}', but got '{actual_details['Total']}'"


@when(u'I click on the Continue to payment button')
def click_on_button(context):
    product_page.continue_payment()

@when(u'I fill payment details')
def step_fill_payment_details(context):
    for row in context.table:
        cardholder_name = row["Cardholder Name"]
        card_number = row["Card Number"]
        expiration_date = row["MMYY"]
        cvv = row["CVV"]

        product_page.fill_payment_details(cardholder_name, card_number, expiration_date, cvv)
@when(u'I click on Checkout button')
def click_on_pay_button(context):
    product_page.click_button()

@then(u'Order created successfully')
def order_created(context):
    product_page.create_order()


