class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # Create the new_node
        new_node = RBNode(val)
        new_node.red = True  # New nodes are always red
        new_node.left = self.nil
        new_node.right = self.nil

        # Find the parent of the new_node
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # Value already exists, so return
                return

        # Set the new_node's parent
        new_node.parent = parent

        # Insert the new_node by setting the parent's child
        if parent is None:
            # This is the first node being inserted (root)
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # After insertion, we'd normally do fixup for RB tree properties,
        # but that's not part of the current requirements
        # self._insert_fixup(new_node)
