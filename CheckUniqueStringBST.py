'''
Cracking Coding Interview 1.1

"implement an algorithm to determine if a sting has all unique characters."

my solution:
    create a binary tree with the bit values of each character, if there is a repeated value when creating the tree,
    return True, to signify a match. This will run at O(Nlog(N)) efficiency if there are no matches
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getAscii(ch):
    return ord(ch)


def addChild(node, data):
    if node.data == data:
        #print(" match")
        return True
    if data < node.data:
        if node.left:
            match = addChild(node.left, data)
            return match
        else:
            node.left = Node(data)
    if data > node.data:
        if node.right:
            match = addChild(node.right, data)
            return match
        else:
            node.right = Node(data)



def buildTree(str):
    root = Node(getAscii(str[0]))
    for c in range(1, len(str)):
        match = addChild(root, getAscii(str[c]))
        if match:
            return True


if __name__ == '__main__':
    string1 = 'abbbd'
    string2 = 'unique?'
    string3 = 'no matches'
    check1 = buildTree(string1)
    check2 = buildTree(string2)
    check3 = buildTree(string3)
    print(string1 + ' Matches: ' + str(check1))
    print(string2 + ' Matches: ' + str(check2))
    print(string3 + ' Matches: ' + str(check3))


