# Created by milindt at 7/07/16
Feature: Test webdriver initialisation
  # Enter feature description here

  Scenario Outline: Should initialise all browser types locally- chrome, firefox, phantomJS, safari, ie
    Given I initialise webbrowser "<browserType>"
    When I navigate to url "https://www.google.co.nz"
    Then I can access the page
    Examples:
      | browserType |
      | chrome      |
#      | Firefox     |
#      | PhantomJS   |
#      | Safari      |
#      | IE          |

#  Scenario: Should initialise all latest browser types in sauce labs - chrome, firefox, safari, ie
#
#  Scenario: Should initialise android default browser on appium locally
#
#  Scenario: Should initialise android default browser on android in sauce labs
#
#  Scenario: Should initialise safari browser on iOS on appium locally
#
#  Scenario: Should initialise safari browser on iOS in sauce labs
