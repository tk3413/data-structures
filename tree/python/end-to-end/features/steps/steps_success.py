from stack import Stack
from behave import *


@given('we have a stack')
def step_impl(context):
    context.stack = Stack()

@when('we push in 100 integers')
def step_impl(context):
    for num in range(1, 101):
        context.stack.push(num)

@when('we pop 3 times')
def step_impl(context):
    for _ in range(1, 4):
        context.stack.pop()

@then('peeking the stack returns 100')
def step_impl(context):
    peek_val = context.stack.peek()
    print(peek_val)
    assert peek_val == 100

@then('the stack size is 100')
def step_impl(context):
    size = context.stack.get_size()
    assert size == 100

@then('the stack size is 97')
def step_impl(context):
    size = context.stack.get_size()
    assert size == 97
