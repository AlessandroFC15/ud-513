import unittest

from .linked_list import LinkedList, Element


class LinkedListAppendTest(unittest.TestCase):
    def test_appending_on_empty_list(self):
        # Arrange
        linked_list = LinkedList()

        # Act
        element = Element(1)
        linked_list.append(element)

        # Assert
        self.assertEqual(linked_list.head, element)
        self.assertEqual(linked_list.length(), 1)

    def test_appending_on_list_with_element(self):
        # Arrange
        linked_list = LinkedList(head=Element(1))

        # Act
        element = Element(2)
        linked_list.append(element)

        # Assert
        self.assertEqual(linked_list.length(), 2)
        self.assertEqual(linked_list.get_position(2).value, element.value)


class LinkedListGetPosition(unittest.TestCase):
    def test_getting_1st_position(self):
        # Arrange
        head = Element(1)
        linked_list = LinkedList(head=head)

        # Assert
        self.assertEqual(linked_list.get_position(1), head)

    def test_getting_position_on_empty_list(self):
        # Arrange
        linked_list = LinkedList()

        # Assert
        self.assertEqual(linked_list.get_position(1), None)

    def test_getting_invalid_position(self):
        # Arrange
        head = Element(1)
        linked_list = LinkedList(head=head)

        # Assert
        self.assertEqual(linked_list.get_position(0), None)
        self.assertEqual(linked_list.get_position(-1), None)

    def test_getting_position_on_the_middle_of_list(self):
        # Arrange
        linked_list = LinkedList()
        linked_list.append(Element(1))
        linked_list.append(Element(2))
        linked_list.append(Element(3))

        # Assert
        self.assertEqual(linked_list.get_position(2).value, 2)

    def test_getting_last_position(self):
        # Arrange
        linked_list = LinkedList()
        linked_list.append(Element(1))
        linked_list.append(Element(2))
        linked_list.append(Element(3))

        # Assert
        self.assertEqual(linked_list.get_position(3).value, 3)

    def test_getting_position_greater_than_length(self):
        # Arrange
        linked_list = LinkedList()
        linked_list.append(Element(1))
        linked_list.append(Element(2))
        linked_list.append(Element(3))

        # Assert
        self.assertEqual(linked_list.get_position(10), None)


class LinkedListInsert(unittest.TestCase):
    def test_inserting_into_1st_position_on_empty_list(self):
        # Arrange
        linked_list = LinkedList()

        # Act
        element = Element("some-element")
        linked_list.insert(element, 1)

        # Assert
        self.assertEqual(linked_list.length(), 1)
        self.assertEqual(linked_list.get_position(1).value, "some-element")

    def test_inserting_into_1st_position_on_populated_list(self):
        # Arrange
        linked_list = LinkedList(head=Element("existing-element"))

        # Act
        element = Element("new-element")
        linked_list.insert(element, 1)

        # Assert
        self.assertEqual(linked_list.length(), 2)
        self.assertEqual(linked_list.get_position(1).value, "new-element")
        self.assertEqual(linked_list.get_position(2).value, "existing-element")

    # def test_inserting_at_the_last_position(self):
    #     # Arrange
    #     linked_list = LinkedList(head=Element("1st-element"))
    #     linked_list.append(Element("2st-element"))
    #     linked_list.append(Element("3rd-element"))
    #
    #     # Act
    #     linked_list.insert(Element("new-element"), 4)
    #
    #     # Assert
    #     self.assertEqual(linked_list.length(), 4)
    #     self.assertEqual(linked_list.get_position(4).value, "new-element")

    def test_inserting_in_the_middle(self):
        # Arrange
        linked_list = LinkedList(head=Element("1st-element"))
        linked_list.append(Element("2nd-element"))
        linked_list.append(Element("3rd-element"))

        # Act
        linked_list.insert(Element("new-element"), 2)

        # Assert
        self.assertEqual(linked_list.length(), 4)
        self.assertEqual(linked_list.get_position(2).value, "new-element")



if __name__ == '__main__':
    unittest.main()
