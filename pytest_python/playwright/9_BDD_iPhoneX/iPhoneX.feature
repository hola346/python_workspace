Feature: iPhone X Product Verification
    Verify that iPhone X product is available on the shop page after login

    Scenario Outline: Verify iPhone X product is present on shop page
        Given user navigates to login page
        When user enters username "<username>" and password "<password>"
        And user selects terms checkbox
        And user clicks on Sign In button
        Then user is navigated to shop page
        And iPhone X product should be present on the page

        Examples:
            | username            | password               |
            | rahulshettyacademy  | Learning@830$3mK2      |
