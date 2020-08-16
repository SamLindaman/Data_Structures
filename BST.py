# This code creates an unbalanced binary tree with an option to
# print in-order traversal, post-order traversal and pre-order traversal
# as well as search if the tree contains a specific number

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    # add new node to left or right in the tree
    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.leftNode:
                self.leftNode.addChild(data)
            else:
                self.leftNode = BinaryTreeNode(data)

        else:
            if self.rightNode:
                self.rightNode.addChild(data)
            else:
                self.rightNode = BinaryTreeNode(data)

    # return an array of numbers in the in-order traversal pattern
    def inOrderTraversal(self):
        elements = []

        if self.leftNode:
            elements += self.leftNode.inOrderTraversal()

        elements.append(self.data)

        if self.rightNode:
            elements += self.rightNode.inOrderTraversal()

        return elements

    # return an array of numbers in the post-order traversal pattern
    def postOrderTraversal(self):
        elements = []

        if self.leftNode:
            elements += self.leftNode.postOrderTraversal()
        if self.rightNode:
            elements += self.rightNode.postOrderTraversal()

        elements.append(self.data)
        return elements

    # return an array of numbers in the pre-order traversal pattern
    def preOrderTraversal(self):
        elements = [self.data]
        # print(self.data)
        if self.leftNode:
            elements += self.leftNode.preOrderTraversal()

        if self.rightNode:
            elements += self.rightNode.preOrderTraversal()



        return elements

    # search for number in tree
    def search(self, value):
        found = False
        # match found
        if self.data == value:
            return True

        # value might be in the left subtree
        if value < self.data:
            if self.leftNode:
                found = self.leftNode.search(value)
            else:
                return False
        else:
            # value might be in the right subtree
            if value > self.data:
                if self.rightNode:
                    found = self.rightNode.search(value)
                else:
                    return False

        return found

    def findMin(self):
        if self.leftNode is None:
            return self.data
        return self.leftNode.findMin()

    def deleteNode(self, value):
        if value < self.data:
            if self.leftNode:
                self.leftNode.deleteNode(value)
        elif value > self.data:
            if self.rightNode:
                self.rightNode.deleteNode(value)
        else:

            if self.leftNode is None:
                return self.rightNode
            if self.rightNode is None:
                return self.leftNode

            minVal = self.rightNode.findMin()
            if self.leftNode is None and self.rightNode is None:
                minVal = None
            self.data = minVal
            self.rightNode = self.rightNode.deleteNode(minVal)

        return self

# create the binary search tree
def createBST(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root



if __name__ == '__main__':
    numbers1 = [18, 14, 2, 18, 29, 32, 22, 15]
    numbers2 = [33,44,55,66,77,88,99,100,101,5,23,78,14,90,47,81]

    tree1 = createBST(numbers1)
    tree2 = createBST(numbers2)

    print(tree1.inOrderTraversal())
    print(tree1.preOrderTraversal())
    print(tree1.postOrderTraversal())
    tree1.deleteNode(14)
    print(tree1.inOrderTraversal())
    print(tree1.search(22))
    print(tree1.search(25))


    print(tree2.inOrderTraversal())
    print(tree2.preOrderTraversal())
    print(tree2.postOrderTraversal())
    tree2.deleteNode(88)
    print(tree2.search(88))
    print(tree2.search(47))
