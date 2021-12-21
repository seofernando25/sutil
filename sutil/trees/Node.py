# Base node class that just inserts childrens
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def preorder(self, node=None):
        if node is None:
            node = self
        print("Traversing node:", node)
        yield node
        for child in (child for child in node.children if child is not None):
            yield from self.preorder(child)

    def inorder(self, node=None):
        if node is None:
            node = self
        # Traverse all childrens except the last one
        for child in (child for child in node.children if child is not None)[:-1]:
            print("Traversing node:", child)
            yield from self.inorder(child)
        # Traverse the last child
        if len(node.children) > 0:
            print("Traversing node:", node.children[-1])
            yield from self.inorder(node.children[-1])
        print("Traversing node:", node)
        yield node


    def postorder(self, node=None):
        if node is None:
            node = self
        for child in (child for child in node.children if child is not None):
            yield from self.postorder(child)
        print("Traversing node:", node)
        yield node

    def insert(self, value):
        node = Node(value)
        node.parent = self
        self.children.append(node)
        return node

    def __str__(self):
        return str(self.value) + " " + str(id(self))[-4:]



    def __repr__(self):
        return str(self.value)
