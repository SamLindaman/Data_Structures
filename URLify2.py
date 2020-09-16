"""
URLify: Write a method to replace all spaces in a string with '%20'.
        (Note: if implementing in Java, pleae use a character array so that you can
        perform this operation in place.)

EXAMPLE
Input:  "Mr John Smith"
Output: "Mr%20John%20Smith"

"""


def make_new_string(string):
    count = 0

    if not isinstance(string, str):
        make_new_string(str(string))

    stopFlag = len(string) - 1

    for i in range(len(string) - 1, -1, -1):
        if string[i] == ' ':
            string = string[:i] + '%20' + string[i + 1:stopFlag] + string[stopFlag:]
            stopFlag = i + 3

    return string


if __name__ == '__main__':
    string1 = 'Hello World !'
    print(make_new_string(string1) + '\n')

    string2 = ' this is a test to replace spaces '
    print(make_new_string(string2) + '\n')

    string3 = '          '
    print(make_new_string(string3))
