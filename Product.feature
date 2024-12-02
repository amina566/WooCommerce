Feature: Verify WooCommerce Product
  Scenario: 1 Add Product to Cart
    Given I open the WooCommerce website
    When I click on the "Shop" button located in the navigation bar
    Then I should see a product displayed on the shop page
    When I click on the "Add to Cart" button for the product on the shop interface
    Then the product should be added to the cart
    When I click on the cart icon located in the navigation bar
    Then the cart interface should open, displaying the product details:
        | Product Name  | Quantity | Price |
        | Demo Product  | 1        | $10.00 |
    And I click on the "Go to Checkout" button on the cart page
    Then the checkout page should open


  Scenario: 2 Billing Form Validation (No Input)
    Given I am on the checkout page
    When I click on the "Place Order" button without filling out any billing details
    Then I should see the following error messages:
        | Billing First Name                            | Billing Last Name                             | Billing Street Address                        | Billing Town / City                           | Billing ZIP Code                              | Billing Phone                                | Billing Email Address                         |
        | Billing First name is a required field.       | Billing Last name is a required field.        | Billing Street address is a required field.   | Billing Town / City is a required field.      | Billing ZIP Code is a required field.         |Billing Phone is a required field.            | Billing Email address is a required field.    |

  Scenario: 3 Successful Billing Form Submission
    Given I am on the checkout page
    When I fill in the billing details as follows:
        | First Name | Last Name  | Country / Region   | Street Address | Town / City| State   | ZIP Code | Phone     | Email Address          |
        | John       | Doe        | United States (US) | 123 Elm Street | New York   | New York| 10001    | 1234567890| john.doe@example.com   |
    And I should see the "Your Order" table with the following details:
        | Product Name  | Quantity | Subtotal | Shipping     | Total  |
        | Demo Product  | 1        | $10.00   | Free Shipping| $10.00 |
    And I click on the "Place Order" button
    Then the order should be successfully placed

