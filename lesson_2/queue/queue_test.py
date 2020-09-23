import unittest

from .queue import Queue
from ..linked_list.linked_list import Element


class EnqueueTest(unittest.TestCase):
    def test_enqueue_on_empty_list(self):
        # Arrange
        queue = Queue()

        # Act
        queue.enqueue(Element("new-element"))

        # Assert
        self.assertEqual(queue.length(), 1)
        self.assertEqual(queue.peek(), "new-element")

    def test_enqueue_on_populated_list(self):
        # Arrange
        queue = Queue(head=Element("existing-element"))

        # Act
        queue.enqueue(Element("new-element"))

        # Assert
        self.assertEqual(queue.length(), 2)
        self.assertEqual(queue.peek(), "existing-element")
        self.assertEqual(queue.dequeue(), "existing-element")
        self.assertEqual(queue.dequeue(), "new-element")


class DequeueTest(unittest.TestCase):
    def test_dequeue_on_empty_list(self):
        # Arrange
        queue = Queue()

        # Act and Assert
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.length(), 0)

    def test_dequeue_on_populated_list(self):
        # Arrange
        queue = Queue(head=Element("existing-element"))

        # Act
        dequeued_element = queue.dequeue()

        # Assert
        self.assertEqual(queue.length(), 0)
        self.assertEqual(dequeued_element, "existing-element")


if __name__ == '__main__':
    unittest.main()
