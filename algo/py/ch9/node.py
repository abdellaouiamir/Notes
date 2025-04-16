class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
if __name__ == "__main__":
    node = Node("amir")
    node2 = Node("amir2")
    node.set_next(node2)
    print(node.next)
