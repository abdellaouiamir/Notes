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
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_node = self.right
                while min_node.left is not None:
                    min_node = min_node.left
                self.val = min_node.val
                self.right = self.right.delete(self.val)
        return self

    def get_max(self):
        if self.right is None:
            return self.val
        return self.right.get_max()

    def get_min(self):
        if self.left is None:
            return self.val
        return self.left.get_min()

    def __repr__(self):
        return f"BSTNode(val={self.val}, left={self.left is not None}, right={self.right is not None})"


if __name__ == "__main__":
    bst = BSTNode()
    bst.insert(8)
    bst.insert(10)
    bst.insert(4)
    bst.insert(8)
    bst.insert(1)
    bst.insert(233)
    print(bst.get_max())  # Should print 233
    print(bst.get_min())  # Should print 1
    bst = bst.delete(233)  # Delete returns the modified tree
    print(bst.get_max())  # Should print 10
