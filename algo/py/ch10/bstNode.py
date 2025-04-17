class User:
    id = 0

    def __init__(self, name):
        self.name = name
        self.id = id
        User.id += 1

    def __eq__(self, other):
        if isinstance(User, other):
            return other.name == self.name
        return False


class BSTNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val and self.left is None:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
            return
        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def get_max(self):
        if self.right is None:
            return self.val
        return self.right.get_max()

    def get_min(self):
        if self.left is None:
            return self.val
        return self.left.get_min()


if __name__ == "__main__":
    bst = BSTNode()
    bst.insert(8)
    bst.insert(10)
    bst.insert(4)
    bst.insert(8)
    bst.insert(1)
    bst.insert(233)
    print(bst.get_max())
    print(bst.get_min())
