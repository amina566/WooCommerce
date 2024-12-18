Feature: Verify WooCommerce Product
  Scenario: 1 Add Product to Cart
    Given I open the shop page
    When I should see a product displayed
    When I click on the Add to Cart button
    When I click on the view cart button
    Then I click on the Go to Checkout button
    Then the checkout page open

  Scenario: 2 Successful Billing Form Submission
    When I fill in the billing details:
        | First Name | Last Name  | Country / Region   | Street Address | Town / City |Postcode | Phone     | Email Address          |
        | John       | Doe        | United Kingdom (UK)        | 123 Elm Street | New York    |10001    | 1234567890| fzfzhce463@generad.club   |
    And I should see the Your Order table:
        |Product Name| Subtotal | Shipping     | Total  |
        |Demo Product  × 1| $10.00  | Free shipping| $10.00 |
    And I click on the Continue to payment button
    And I fill payment details:
      | Cardholder Name      | Card Number | MMYY  |CVV  |
      | Test demo | 4242424242424242       |0123       | 123       |
    And I click on Checkout button
    Then Order created successfully