

from trees.Node import Node


class BinaryTreeNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.children = [None, None]

    def insert(self, value):
        # Create a left and right pseudo-representation

        left = self.children[0]
        right = self.children[1]

        if value < self.value:
            if left is None:
                self.children[0] = BinaryTreeNode(value)
            else:
                self.children[0].insert(value)
        elif right is None:
            self.children[1] = BinaryTreeNode(value)
        else:
            self.children[1].insert(value)