# Created by stefankahn at 24/08/17
@mobile
Feature:
  As a skynet user
  I want to capability to run mobile web automation on a mobile device
  So that it can be used to test mobile web applications

  @android-chrome
  Scenario:Running a mobile web test with skynet
    Given I have a device with chrome open
    When I navigate to http://www.google.com
    Then The google homepage is displayed