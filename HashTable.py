# create a hash table programatically and through a python dictionary

class HashTable:
    def __init__(self):
        self.max = 50
        self.arr = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        if isinstance(key, str):
            for char in key:
                h += ord(char)
                return h % self.max
        else:
            self.getHash(self, str(key))

    def __setitem__(self, key, value):

        modify = False
        h = self.getHash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key, value)
                modify = True

        if not modify:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def set(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.getHash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == '__main__':
    #using created hash table
    table = HashTable()
    table['march 6'] = 25
    table['march 6'] = 55
    table['march 17'] = 17
    table['jan 14'] = 100
    table.set('August 23', 23)

    print(table.arr)

    del table['march 6']
    del table['abc 22']

    print(table.arr)

    print('\r\r')
    #using dictionary
    tableDict = {}
    tableDict['april 14'] = 11
    tableDict['September 23'] = 123
    val = tableDict['april 14']

    print(val)
    print(tableDict)

