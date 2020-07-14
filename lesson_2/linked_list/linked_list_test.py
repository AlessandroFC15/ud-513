import unittest

from .linked_list import LinkedList, Element


class LinkedListAppendTest(unittest.TestCase):
    def test_appending_on_empty_list(self):
        # Arrange
        linkedList = LinkedList()

        # Act
        element = Element(1)
        linkedList.append(element)

        # Assert
        self.assertEqual(linkedList.head, element)
        self.assertEqual(linkedList.length(), 1)


if __name__ == '__main__':
    unittest.main()
