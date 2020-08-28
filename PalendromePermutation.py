class HashMap:

    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range(self.MAX)]

    def getKey(self, ch):
        if isinstance(ch, str):
            key = ord(ch)
            return key % self.MAX
        else:
            self.getKey(str(ch))

    def add(self, ch):
        key = self.getKey(ch)
        change = False
        for index, element in enumerate(self.arr[key]):
            if element[0] == ch:
                self.arr[key][index] = (ch, element[1] + 1)
                change = True
        if not change:
            self.arr[key].append((ch, 1))

    def checkPerm(self, string):
        if len(string) % 2 == 0:
            flag = False
        else:
            flag = True
            foundSingle = False

        for s in string:
            key = self.getKey(s)
            for index, element in enumerate(self.arr[key]):
                if flag:
                    if element[0] == s:
                        if element[1] % 2 == 1:
                            if not foundSingle:
                                foundSingle = True
                                single = element[0]
                            else:
                                if not single == element[0]:
                                    return False
                else:
                    if element[0] == s:
                        if element[1] % 2 == 1:
                            return False
        return True

    def buildTree(self, string):
        for c in string:
            self.add(c)
        perm = self.checkPerm(string)
        return perm


if __name__ == '__main__':
    map1 = HashMap()
    map2 = HashMap()
    map3 = HashMap()
    map4 = HashMap()

    string1 = 'tacocat'     # is a palindrome -> 'tacocat'
    string2 = 'TacoCat'     # is not a palindrome because of capital letters
    string3 = 'not a palindrome'
    string4 = 'aaabbccddeeffff'   # is palindrome -> 'abcdeffaffedcba'

    print(map1.buildTree(string1))
    print(map2.buildTree(string2))
    print(map3.buildTree(string3))
    print(map4.buildTree(string4))
