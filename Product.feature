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

  Scenario: 2 Successful Billing Form Submission
    When I fill in the billing details as follows:
        | First Name | Last Name  | Country / Region   | Street Address | Town / City |Postcode | Phone     | Email Address          |
        | John       | Doe        | United Kingdom (UK)        | 123 Elm Street | New York    |10001    | 1234567890| fzfzhce463@generad.club   |
    And I should see the Your Order table with the following details:
        |Product Name| Subtotal | Shipping     | Total  |
        |Demo Product  × 1| 10 $   | Free shipping| 10 $ |
    And I should see payment methods displayed
        | payment methods         |
        | Credit Card             |
        | PAYARC Hosted Checkout  |
    And I select PAYARC Hosted Checkout radio button
    And I click on the Continue to payment button on checkout page
    And I fill in the payment details:
      | Card number      | Expiration date | CVC/CVV  |First Name  |Last Name |Address Line 1 |Address Line 2|City     | State | ZIP code  | Email address    |
      | 4761739012347120 | 0123            |123       | John       |Doe       |123 Main St    |Apt 4B       |New York | NY    |10001      |fzfzhce463@generad.club |
    And I click on PAY $10.00 button
