Feature: graceful error handling

  Scenario: empty stack
     Given we have a stack
      When we do nothing
      Then peeking the stack returns None
      And the stack size is 0
      And popping the stack returns None

  Scenario: limit type of item pushed to stack
    Given we have a stack
    When we push an integer
    And we push a string
    Then we catch an error
