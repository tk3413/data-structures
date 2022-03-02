from stack import Stack
from behave import *

@when('we do nothing')
def step_impl(context):
    pass

@then('peeking the stack returns None')
def step_impl(context):
    assert context.stack.peek() is None

@then('the stack size is 0')
def step_impl(context):
    assert context.stack.get_size() == 0

@then('popping the stack returns None')
def step_impl(context):
    assert context.stack.pop() is None

@when('we push an integer')
def step_impl(context):
    context.stack.push(1)

@when('we push a string')
def step_impl(context):
    try:
        context.stack.push("1")
    except TypeError as te:
        context.error = te

@then('we catch an error')
def step_impl(context):
    assert type(context.error) == TypeError
