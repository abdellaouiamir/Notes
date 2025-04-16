from node import Node


class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_from_head(self):
        old = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        old.set_next(None)
        return old

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_to_head(self, node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def add_to_tail_2(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)


if __name__ == "__main__":
    ll = LLQueue()
    n1 = Node("amir1")
    ll.add_to_tail(n1)
    n2 = Node("amir2")
    ll.add_to_tail(n2)
    n3 = Node("amir3")
    ll.add_to_tail(n3)
    n4 = Node("amir4")
    ll.add_to_head(n4)
    v = ll.remove_from_head()
    for i in ll:
        print(i)
    print(v)

