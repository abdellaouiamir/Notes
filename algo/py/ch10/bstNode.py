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
                self.right = self.right.delete(min_node.val)
        return self

    def preorder(self, visited: list):
        visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited: list):
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def inorder(self, visited: list):
        if self.left is not None:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited

    def exists(self, val):
        if self.val is None:
            return False
        if val < self.val:
            if self.left is not None:
                return self.left.exists(val)
        elif val > self.val:
            if self.right is not None:
                return self.right.exists(val)
        else:
            return True
        return False

    def height(self):
        if self is None:
            return 0
        heightLeft = self.left.height()if self.left else 0
        heightRight = self.right.height()if self.right else 0
        return 1+max(heightLeft, heightRight)

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
    bst.insert(333)
    bst.insert(433)
    bst.insert(533)
    bst.insert(2)
    bst.insert(3)
    print(bst.get_max())  # Should print 233
    print(bst.get_min())  # Should print 1
    bst = bst.delete(233)  # Delete returns the modified tree
    print(bst.get_max())  # Should print 10
    bst = bst.delete(0)  # Delete returns the modified tree
    print(bst)
    print(bst.preorder([]))
    print(bst.postorder([]))
    print(bst.inorder([]))
    print(bst.exists(3))
    print(bst.exists(10000))

    bs2 = BSTNode()
    bs2.insert(4)
    bs2.insert(2)
    bs2.insert(7)
    bs2.insert(6)
    bs2.insert(1)
    print(bs2.preorder([]))
    print(bs2.postorder([]))
    print(bs2.inorder([]))
    print(bs2.exists(3))
    print(bs2.exists(1))
    print(bs2.height())

    bs3 = BSTNode()
    bs3.insert(1)
    bs3.insert(3)
    bs3.insert(2)
    bs3.insert(4)
    bs3.insert(5)
    print(bs3.height())
