# Created by milindt at 21/09/16
  @regression
Feature: NZH User Registration
  As a NZH user
  I want to register on the website
  So that I can get personalised

  @uat @mobile @post-prod
  Scenario: The user can register on NZH
#    Given I open the registration form
#    When I fill the registration form
#    And I click the register button
    When I fill register form and submit
    Then I should be registered successfully
    And I should see the username on the homepage