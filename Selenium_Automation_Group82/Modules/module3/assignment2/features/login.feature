Feature: Login functionality

  Scenario Outline: Login with different test data
    Given I open the login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then I should get "<result>"

    Examples:
      | username  | password              | result  |
      | tomsmith  | SuperSecretPassword!  | success |
      | wronguser | SuperSecretPassword!  | failure |
      | tomsmith  | wrongpassword         | failure |
      | wronguser | wrongpassword         | failure |