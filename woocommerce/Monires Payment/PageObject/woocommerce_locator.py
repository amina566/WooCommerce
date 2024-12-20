from selenium.webdriver.common.by import By

class ProductLocators:
    SHOP_BUTTON = (By.XPATH, '//*[@id="modal-1-content"]/ul/ul/li/a[contains(text(), "Shop")]')
    SHOP_PRODUCT_TEXT = (By.XPATH, '//*[@id="wp--skip-link--target"]/h1')
    PRODUCTS_NAME = (By.ID, '//a[text()="Demo Product"]')
    PRODUCTS_PRICE = (By.XPATH, "//bdi[contains(text(), '10') and ./span[@class='woocommerce-Price-currencySymbol']]")
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="wp--skip-link--target"]/div[4]/ul/li/div/button')
    view_cart = (By.CSS_SELECTOR, 'a[title="View cart"]')
    PRODUCT_NAME = (By.XPATH, '//a[@class="wc-block-components-product-name"]')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'input.wc-block-components-quantity-selector__input')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.wc-block-formatted-money-amount.wc-block-components-formatted-money-amount.wc-block-components-product-price__value')
    CHECKOUT_BUTTON = (By.XPATH, '//*[@id="wp--skip-link--target"]/div/div/div/div/div/div/div/div/a')
    CHECKOUT_PAGE_TEXT = (By.XPATH, '/html/body/div[1]/header/div/p/a')
    BILLING_FIRST_NAME = (By.NAME, "billing_first_name")
    BILLING_LAST_NAME = (By.ID, "billing_last_name")
    BILLING_COUNTRY = (By.ID, "billing_country")
    BILLING_ADDRESS_1 = (By.ID, "billing_address_1")
    BILLING_CITY = (By.ID, "billing_city")
    BILLING_POSTCODE = (By.ID, "billing_postcode")
    BILLING_PHONE = (By.ID, "billing_phone")
    BILLING_EMAIL = (By.ID, "billing_email")
    Order_PRODUCT_NAME = (By.XPATH, '//*[@id="order_review"]/table/tbody/tr/td[1][contains(text(), "Demo Product")]')
    SUBTOTAL = (By.XPATH, '//table/tbody/tr[1]/td[2]')
    SHIPPING = (By.XPATH, '//table/tfoot/tr[2]/td')
    TOTAL = (By.XPATH, '//table/tfoot/tr[3]/td')
    PAYMENT_METHODS = (By.CSS_SELECTOR,'#payment ul.payment_methods > li > label')
    PAYARC_PAYMENT_METHOD = (By.ID, 'payment_method_payarc_hosted')
    PLACE_ORDER_BUTTONS = (By.XPATH, '//*[@id="moneris_place_order"]' )
    PLACE_ORDERS_BUTTON = (By.XPATH, '//*[@id="moneris_place_order"]')
    PAYMENT_IFRAME = (By.XPATH, '//iframe[@id="monerisCheckout-Frame"]')
    PAY_BUTTON = (By.XPATH, '//input[@value="Checkout"]')
    VERIFICATION=(By.XPATH, '//*[@id="wp--skip-link--target"]/div/p')
    cardholder_name_locator = (By.XPATH, '//input[@name="cardholder"]')
    card_number_locator = (By.XPATH, '//input[@name="pan"]')
    expiration_date_locator = (By.XPATH, '//input[@name="expiry_date"]')
    cvv_locator = (By.XPATH, '//input[@name="cvv"]')
    IFRAMES = (By.XPATH, '//*[@id="process"]')
    IFRAME_XPATH = (By.XPATH, '//iframe[@id="monerisCheckout-Frame"]')



