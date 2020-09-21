from ..linked_list.linked_list import LinkedList


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert(new_element, 1)

    def pop(self):
        element_on_top = self.ll.head
        self.ll.delete_first()
        return element_on_top

    def length(self):
        return self.ll.length()
