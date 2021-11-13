import stack
import unittest


class TestStack(unittest.TestCase):
    def test_size(self):
        test_stack = stack.Stack()
        self.assertEqual(test_stack.get_size(), 0)

    def test_push(self):
        test_stack = stack.Stack()
        test_stack.push(1)
        self.assertEqual(test_stack.get_size(), 1)
        with self.assertRaises(TypeError):
            test_stack.push("1")

    def test_peek(self):
        test_stack = stack.Stack()
        self.assertEqual(test_stack.peek(), None)
        test_stack.push(1)
        self.assertEqual(test_stack.peek(), 1)
        self.assertEqual(test_stack.get_size(), 1)

    def test_pop(self):
        test_stack = stack.Stack()
        self.assertEqual(test_stack.pop(), None)
        test_stack.push(1)
        self.assertEqual(test_stack.get_type(), int)
        self.assertEqual(test_stack.pop(), 1)
        self.assertEqual(test_stack.get_size(), 0)
        self.assertEqual(test_stack.get_type(), None)

    def test_type(self):
        test_stack = stack.Stack()
        self.assertEqual(test_stack.get_type(), None)
