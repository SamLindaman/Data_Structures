'''
Cracking Coding Interview 1.2

This file checks if string1 could somehow make string2 from some permutation
these strings are entered by the user
'''

class HashMap:
    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range (self.MAX)]

    def getHash(self, ch):
        h=0
        if isinstance(ch, str):
            h += ord(ch)
            return h % self.MAX
        else:
            self.getHash(self, str(ch))

    def __setitem__(self, key, value):
        h = self.getHash(key)

        add = False

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, element[1]+value)
                add = True

        if not add:
            self.arr[h].append((key, value))

    def checkChar(self, key,  value):
        h = self.getHash(key)

        if not self.arr[h]:
            return True

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, element[1]-value)
                if (element[1] -1) < 0:
                    return True

            else:
                return True




# fail = return true

    def createHashTable(self, string):
        for ch in string:
            self.__setitem__(ch,1)

if __name__ == '__main__':

    fail = False

    mainString = input('Enter main string: ')
    string2 = input('Enter second string: ')

    hashMap = HashMap()

    hashMap.createHashTable(mainString)

    for ch in string2:
        fail = hashMap.checkChar(ch,1)
        if fail:
            break

    if fail:
        print(mainString + ' could NOT make ' + string2)
    else:
        print(mainString + ' could make ' + string2 )

    print('(case sensitive)')

