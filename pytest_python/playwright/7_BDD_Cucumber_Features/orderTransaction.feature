Feature: Order Transaction
    Test related to Order Transactions

    Scenario Outline: Verify order success message in order details page
        Given Login by API using <username> and <password> and create order
        And take note of the ORDER number
        And user is on landing page

        When Login to the application using UI with same <username> and <password>
        And go to order history
        And select order details using previous ORDER number

        Then Validate the order details - order message should be "Thank you for Shopping With Us"
        Examples:
            | username                    | password               |
            | wrs888888888@dwerewrwer.com | CCCCacc/dffg3412345678 |
            | x2xx@ii.com                 | Aa/12345678            |
