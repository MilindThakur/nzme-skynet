# Created by milindt at 21/09/16
Feature: NZH User Registration
  As a NZH user
  I want to register on the website
  So that I can get personalised

  Scenario: The user can register on NZH
    Given I open the registration form
    When I fill the registration form with fields
      |Field        | Value             |
      |First name    |testname           |
      |Last name     |testlastname       |
      |Email         |testuser1@gmail.com|
      |Confirm email |testuser1@gmail.com|
      |Password      |Agile@2016         |
      |Birth year    |1985               |
      |Postcode      |1010               |
      |Gender        |Male               |
    And I click the register button
    Then I should be registered successfully

  Scenario: Registered user can immediately login to the NZH website on successful registration
    Given I can register on NZH website successfully
    When I fill the login form
    And I click the login button
    Then I should be logged in to the NZH website