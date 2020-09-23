class Queue:
    def __init__(self, head=None):
        self.storage = [head] if head else []

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0].value if self.storage[0] else None

    def dequeue(self):
        if len(self.storage) == 0:
            return None

        head = self.storage[0].value

        self.storage = self.storage[1:]

        return head

    def length(self):
        return len(self.storage)
