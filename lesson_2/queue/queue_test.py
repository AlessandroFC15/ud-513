import unittest

from .queue import Queue
from ..linked_list.linked_list import Element


class QueueEnqueueTest(unittest.TestCase):
    def test_enqueue_on_empty_list(self):
        # Arrange
        queue = Queue()

        # Act
        queue.enqueue(Element("new-element"))

        # Assert
        self.assertEqual(queue.length(), 1)
        self.assertEqual(queue.peek(), "new-element")

    def test_enqueue_on_populated_list(self):
        # TO-DO
        pass


if __name__ == '__main__':
    unittest.main()
