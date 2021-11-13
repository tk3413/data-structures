Feature: working stack

  Scenario: push, pop, then peek
     Given we have a stack
      When we push in 100 integers
      Then peeking the stack returns 100
