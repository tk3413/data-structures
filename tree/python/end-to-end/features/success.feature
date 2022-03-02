Feature: working stack

  Scenario: push, then peek
     Given we have a stack
      When we push in 100 integers
      Then peeking the stack returns 100
      And the stack size is 100

  Scenario: pop 'til you drop
     Given we have a stack
      When we push in 100 integers
      And we pop 3 times
      Then the stack size is 97
