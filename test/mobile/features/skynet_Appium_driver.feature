# Created by stefankahn at 18/08/17
@mobile
Feature:
  As a skynet user
  I want to capability to run mobile app automation
  So that it can be used to test mobile apps

  @mobile-android
  Scenario: Running an android test with skynet
    Given I am on the test app home screen
    Then The home message is displayed

#  not_implemented
#  @mobile-ios
#  Scenario: Running an ios test with skynet
#    Given I am on the test app home screen
#    Then The home message is displayed
