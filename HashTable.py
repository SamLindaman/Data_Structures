# create a hash table programatically and through a python dictionary

class HashTable:
    def __init__(self):
        self.max = 50
        self.arr = [None for i in range(self.max)]

    def getHash(self, key):
        h = 0
        if isinstance(key, str):
            for char in key:
                h += ord(char)
                return h % self.max
        else:
            self.getHash(self, str(key))

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        return self.arr[h]

    def set(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.getHash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        self.arr[h] = None


if __name__ == '__main__':
    #using created hash table
    table = HashTable()
    table['march 15'] = 25
    table['jan 14'] = 100
    table['abc 22'] = 1
    table.set('August 23', 23)
    del table['abc 22']

    print(table.arr)

    #using dictionary
    tableDict = {}
    tableDict['april 14'] = 11
    tableDict['September 23'] = 123
    val = tableDict['april 14']

    print(val)
    print(tableDict)

