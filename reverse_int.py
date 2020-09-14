MAX = 2147483647
MIN = 2147483648


def reverse(number):
    if number>0:
        isNegative = False
    else:
        isNegative = True
    digit = 0
    reversedNumber = 0

    if isNegative:
        number = number * -1

    while number != 0:
        digit = number % 10
        number = number / 10
        if reversedNumber > MAX / 10:
            return
        elif reversedNumber == MAX / 10:
            if isNegative and digit > 8:
                return
            if not isNegative and digit > 7:
                return

        reversedNumber = reversedNumber * 10 + digit

    if isNegative:
        reversedNumber *=-1

    return reversedNumber

if __name__ == '__main__':
    number1 = 1234567
    number2 = -987753333
    number3 = 80000

    revNumber1 = reverse(number1)
    revNumber2 = reverse(number2)
    revNumber3 = reverse(number3)

    print(revNumber1)
    print(revNumber2)
    print(revNumber3)
    print(reverse(9999999999999999))