"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def length(self):
        num_elements = 0

        current = self.head

        while current:
            current = current.next
            num_elements += 1

        return num_elements

    def get_position(self, position):
        if not self.head:
            return None

        current = self.head
        i = 0

        while current:
            if i == position - 1:
                return current

            current = current.next
            i += 1

        return None

    def insert(self, new_element, position) -> None:
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        current = self.head
        past_element = None
        i = 0

        while current:
            if i == position - 1:
                new_element.next = current
                past_element.next = new_element
                return

            past_element = current
            current = current.next
            i += 1

        if i == position - 1:
            new_element.next = None
            past_element.next = new_element
            return

    def delete(self, value) -> None:
        if self.head and self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        past_element = None

        while current:
            if current.value == value:
                past_element.next = current.next
                return

            past_element = current
            current = current.next

    def delete_first(self):
        if self.head:
            self.head = self.head.next
