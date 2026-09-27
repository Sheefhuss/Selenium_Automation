Feature: Login functionality

  Scenario: Successful login
    Given I open the login page
    When I enter username "tomsmith"
    And I enter password "SuperSecretPassword!"
    And I click the login button
    Then I should be successfully logged in