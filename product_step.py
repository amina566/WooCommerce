from behave import *
from PageObject.product_object import ProductPage
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
product_page = ProductPage()
@given(u'I open the WooCommerce website')
def open_login(context):
    product_page.set_driver(context.driver)
    woocommerce_url = os.getenv('WOOCOMMERCE_URL')
    if woocommerce_url:
        product_page.open_page(woocommerce_url)
    else:
        print("URL is not set in the environment variables!")


@when(u'I click on the Shop button located in the navigation bar')
def shop_button(context):
    product_page.shopbutton()



@then(u'I should see a product displayed on the shop page')
def see_shop_product(context):
    product_page.shopproduct()

@when(u'I click on the Add to Cart button for the product on the shop interface')
def addto_cart(context):
    product_page.add_to_cart()

@when(u'I click on the cart icon located in the navigation bar')
def cart_icon(context):
    product_page.carticon()

@then(u'the cart interface should open, displaying the product details')
def displaying_cart(context):
    for row in context.table:
        expected_product_name = row["Product Name"]
        expected_quantity = row["Quantity"]
        expected_price = row["Price"]

        actual_product_name = product_page.get_product_name()
        actual_quantity = product_page.get_product_quantity()
        actual_price = product_page.get_product_price()

        assert actual_product_name == expected_product_name, f"Expected product name '{expected_product_name}', but got '{actual_product_name}'"
        assert actual_quantity == expected_quantity, f"Expected quantity '{expected_quantity}', but got '{actual_quantity}'"
        assert actual_price == expected_price, f"Expected price '{expected_price}', but got '{actual_price}'"

@then(u'I click on the Go to Checkout button on the cart page')
def go_to_checkout_button(context):
    product_page.checkoutbutton()

@then(u'the checkout page should open')
def checkout_page(context):
    product_page.checkoutpage()

@when(u'I fill in the billing details as follows')
def fill_billing_details(context):
    for row in context.table:
        first_name = row["First Name"]
        last_name = row["Last Name"]
        country_region = row["Country / Region"]
        street_address = row["Street Address"]
        town_city = row["Town / City"]
        # state = row["State / County"]
        postcode = row["Postcode"]
        phone = row["Phone"]
        email_address = row["Email Address"]

        product_page.fill_billing_details(first_name, last_name, country_region, street_address, town_city, postcode, phone, email_address)

@when(u'I should see the Your Order table with the following details')
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

@when('I should see payment methods displayed')
def payment_method(context):
    expected_payment_methods = [row['payment methods'] for row in context.table]
    displayed_payment_methods = product_page.get_payment_methods()

    assert expected_payment_methods == displayed_payment_methods, (
        f"Expected payment methods: {expected_payment_methods}, "
        f"but found: {displayed_payment_methods}"
    )

@when(u'I select PAYARC Hosted Checkout radio button')
def select_payarc(context):
    product_page.payarc_checkout()

@when(u'I click on the Continue to payment button on checkout page')
def click_on_button(context):
    product_page.continue_payment()

@when(u'I fill in the payment details')
def step_fill_payment_details(context):
    for row in context.table:
        card_number = row["Card number"]
        expiration_date = row["Expiration date"]
        cvc_cvv = row["CVC/CVV"]
        first_name = row["First Name"]
        last_name = row["Last Name"]
        address_line1 = row["Address Line 1"]
        address_line2 = row["Address Line 2"]
        city = row["City"]
        state = row["State"]
        zip_code = row["ZIP code"]
        email_address = row["Email address"]

        product_page.fill_payment_details(card_number, expiration_date, cvc_cvv, first_name, last_name, address_line1, address_line2, city, state, zip_code, email_address)
    # product_page.handle_payment_popup()

@when(u'I click on PAY $10.00 button')
def click_on_pay_button(context):
    product_page.click_button()

#     raise NotImplementedError(u'STEP: When I fill in all the shipping address fields')
#
#
# @then(u'the order should be not placed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the order should be not placed')
