Feature: Verify WooCommerce Product
  Scenario: 1 Add Product to Cart
    Given I open the WooCommerce website
    When I click on the "Shop" button located in the navigation bar
    Then I should see a product displayed on the shop page
    When I click on the "Add to Cart" button for the product on the shop interface
        | Product Name  | Price  |
        | Demo Product  | $10.00 |
    Then the product should be added to the cart
    When I click on the cart icon located in the navigation bar
    Then the cart interface should open, displaying the product details:
        | Product Name  | Quantity | Price |
        | Demo Product  | 1        | $10.00 |
    And I click on the "Go to Checkout" button on the cart page
    Then the checkout page should open

  Scenario: 2 Billing Form Validation (No Input)
    When I click on the "Place Order" button on checkout page
    Then I should see the following error messages:
        | Billing First Name                            | Billing Last Name                             | Billing Street Address                        | Billing Town / City                           | Billing Postcode                              | Billing Phone                                | Billing Email Address                         |
        | Billing First name is a required field.       | Billing Last name is a required field.        | Billing Street address is a required field.   | Billing Town / City is a required field.      | Billing Postcode is a required field.         |Billing Phone is a required field.            | Billing Email address is a required field.    |

  Scenario: 3 Successful Billing Form Submission
    When I fill in the billing details as follows:
        | First Name | Last Name  | Country / Region   | Street Address | Town / City|  Postcode | Phone     | Email Address          |
        | John       | Doe        | United States (US) | 123 Elm Street | New York   |  10001    | 1234567890| john.doe@example.com   |
    And I should see the "Your Order" table with the following details:
        | Product Name  | Quantity | Subtotal | Shipping     | Total  |
        | Demo Product  | 1        | $10.00   | Free Shipping| $10.00 |
    And I click on the "Place Order" button on checkout page
    Then the order should be successfully placed

  Scenario: 4 Fill shipping address fields and submit
    When I click on the "Ship to a different address" checkbox
    And I fill in all the shipping address fields:
      | Shipping First Name | Shipping Last Name   | Country / Region     | Street Address | Town / City| Postcode |
      | MR.                 | A                 | United States (US)   | 123 Elm St     | Nottingham | NG7 4AH   |
    And I click on the "Place Order" button on checkout page
    Then the order should be not placed

  Scenario: 5 Do not fill shipping address fields and submit
    When I click on the "Ship to a different address" checkbox
    And I click on the "Place Order" button on checkout page
    Then I should see the following error messages:
       | Shipping First Name                            | Shipping Last Name                             | Shipping Street Address                             | Shipping Town / City                           | Shipping Postcode                             |
       | Shipping First name is a required field.       | Shipping Last name is a required field.        | Shipping Street address is a required field.        | Shipping Town / City is a required field.      | Shipping Postcode is a required field.        |

  Scenario: 6 Successful Billing and Shipping Form Submission
    When I fill in the billing details as follows:
        | First Name | Last Name  | Country / Region   | Street Address | Town / City|  Postcode | Phone     | Email Address          |
        | John       | Doe        | United States (US) | 123 Elm Street | New York   |  10001    | 1234567890| john.doe@example.com   |
    And I click on the "Ship to a different address" checkbox
    And I fill in all the shipping address fields:
      | Shipping First Name | Shipping Last Name   | Country / Region     | Street Address | Town / City| Postcode |
      | MR.                 | A                 | United States (US)   | 123 Elm St     | Nottingham | NG7 4AH   |
    And I should see the "Your Order" table with the following details:
        | Product Name  | Quantity | Subtotal | Shipping     | Total  |
        | Demo Product  | 1        | $10.00   | Free Shipping| $10.00 |
    And I click on the "Place Order" button on checkout page
    Then the order should be successfully placed
