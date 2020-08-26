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

    startFlag = len(string) - 1
    stopFlag = len(string) - 1

    for i in range(len(string) - 1, -1, -1):
        if string[i] == ' ':
            string = string[:startFlag] + '%20' + string[startFlag + 1:stopFlag] + string[stopFlag:]
            stopFlag = startFlag + 3
        startFlag -= 1

    return string


if __name__ == '__main__':
    string1 = 'Hello World !'
    string2 = make_new_string(string1)
    print(string2 + '\n')

    string3 = ' this is a test to replace spaces '
    string4 = make_new_string(string3)
    print(string4 + '\n')

    string5 = '          '
    string6 = make_new_string(string5)
    print(string6)
