import unittest

from .stack import Stack
from ..linked_list.linked_list import Element


class StackPushTest(unittest.TestCase):
    def test_push_on_empty_list(self):
        # Arrange
        stack = Stack()

        # Act
        stack.push(Element(1))

        # Assert
        self.assertEqual(stack.length(), 1)
        self.assertEqual(stack.pop().value, 1)

    def test_push_on_populated_list(self):
        # Arrange
        stack = Stack(top=Element(1))

        # Act
        stack.push(Element(2))

        # Assert
        self.assertEqual(stack.length(), 2)
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 1)


class StackPopTest(unittest.TestCase):
    def test_pop_on_empty_list(self):
        # Arrange
        stack = Stack()

        # Assert
        self.assertEqual(stack.pop(), None)

    def test_pop_on_populated_list(self):
        # Arrange
        stack = Stack(top=Element(1))
        stack.push(Element(2))

        # Act
        self.assertEqual(stack.pop().value, 2)
        self.assertEqual(stack.pop().value, 1)


if __name__ == '__main__':
    unittest.main()
