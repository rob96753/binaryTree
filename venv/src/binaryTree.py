import os
import json
from collections import deque

VALUE_LIST = 'VALUE_LIST'
VALUES = 'values'

"""
example environment values:
    VALUE_LIST={"values":[9,4,8,1,3,6,7,2,5,10,0]}
"""

class Node(object):
    value = None
    key = None
    left = None
    right = None

    def getKey(self):
        return self.key

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getValue(self):
        return self.value

    def addNode(self, node):
        if self.getKey() > node.getKey():
            self.left = node
        else:
            self.right = node

    def __init__(self, value):
        if type(value) is str:
            if value.isdigit():
                value = int(value)
            self.key = value
            self.value = value
        elif type(value) is dict:
            if "key" in value:
                self.key = value.get('key')
                self.value = value
            else:
                raise Exception(f'Tree value of type dict must contain a "key" attribute. {value}')
        elif type(value) is int:
            self.key = value
            self.value = value
        else:
            raise Exception(f'Unexpected type of {type(value)} for tree node. {value}')




class BinaryTree(object):
    valueList = []
    root = None
    sorted = []
    def __init__(self):
        valueList = os.getenv(VALUE_LIST)
        if valueList is None:
            raise Exception(f'{VALUE_LIST} must be defined in the environment')
        self.valueList = json.loads(valueList)[VALUES]

    def addNode(self, node):
        try:
            currentNode = self.root
            while not currentNode is None:
                if node.getKey() < currentNode.getKey():
                    if currentNode.getLeft() is None:
                        break
                    currentNode = currentNode.getLeft()
                elif node.getKey() > currentNode.getKey():
                    if currentNode.getRight() is None:
                        break
                    currentNode = currentNode.getRight()
                else:
                    raise Exception(f'Node key has already been inserted')
            currentNode.addNode(node)
        except Exception as ex:
            raise Exception(f'Exception in Binary Tree Add Node {ex}')

    def getRoot(self):
        return self.root

    def buildTree(self):
        try:
            for value in self.valueList:
                node = Node(value)
                if self.root is None:
                    self.root = node
                else:
                    self.addNode(node)
        except Exception as ex:
            raise Exception(f'Build Tree exception: {ex}')

    def printTree(self, tree):
        if not tree.getLeft() is None:
            self.printTree(tree.getLeft())

        self.sorted.append(tree.getValue())

        if not tree.getRight() is None:
            self.printTree(tree.getRight())

    def printTreePre(self, tree):

        self.sorted.append(tree.getValue())

        if not tree.getLeft() is None:
            self.printTree(tree.getLeft())

        if not tree.getRight() is None:
            self.printTree(tree.getRight())

    def printTreePost(self, tree):
        if not tree.getLeft() is None:
            self.printTree(tree.getLeft())

        if not tree.getRight() is None:
            self.printTree(tree.getRight())

        self.sorted.append(tree.getValue())

    def treeHeight(self, tree):
        if tree is None:
            return 0
        else:
            # get the height of each subtree
            lHeight = self.treeHeight(tree.getLeft())
            rHeight = self.treeHeight(tree.getRight())

            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    # Function to print reverse level order traversal
    def reverseLevelOrder(self, root, height):
        for i in reversed(range(1, height + 1)):
            print(f'Level: {i}')
            self.givenLevel(root, i)

    def givenLevel(self, tree, level):

        if tree is None:
            return
        if level == 1:
            print(tree.value)
        elif level > 1:
            self.givenLevel(tree.left, level - 1)
            self.givenLevel(tree.right, level - 1)

    def getSorted(self):
        return self.sorted

    def clearSorted(self):
        self.sorted = []

    def __repr__(self):
        return str(self.valueList)

    """
    levelorder(root)
    q ← empty queue
    q.enqueue(root)
    while not q.isEmpty() do
        node ← q.dequeue()
        visit(node)
        if node.left ≠ null then
            q.enqueue(node.left)
        if node.right ≠ null then
            q.enqueue(node.right)
    """
    def breadthFirstSearch(self, tree):
        queue = collections.deque()
        queue.push(tree)
        while len(queue) > 0:
            node = queue.pop()
            #visit node

            if not node.left is None:
                queue.push(node.left)
            if not node.right is None:
                queue.push(node.right)





def main():
    try:
        bt = BinaryTree()
        print(f'Binary Tree {bt}')
        bt.buildTree()
        bt.printTree(bt.getRoot())
        print(f'Print Tree: {bt.getSorted()}')
        bt.clearSorted()
        bt.printTreePre(bt.getRoot())
        print(f'Pre-order Tree: {bt.getSorted()}')
        bt.clearSorted()
        bt.printTreePost(bt.getRoot())
        print(f'Post-order Tree: {bt.getSorted()}')
        bt.clearSorted()
        bt.printTreeReverse(bt.getRoot())
        print(f'Reverse-order Tree: {bt.getSorted()}')

        height = bt.treeHeight(bt.getRoot())
        for i in reversed(range(1, height + 1)):
            print(f'Level: {i}')
            bt.givenLevel(bt.getRoot(), i)

        print(f' Tree Height: {height}')

    except Exception as ex:
        print(f'Application failed with error: {ex}')

if __name__ == "__main__":
    main()