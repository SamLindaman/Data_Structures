def compress(arr):
    i = 0
    j = 1
    while i != len(arr)-1:
        if arr[i] == arr[j]:
            while arr[i] == arr[j] and j != len(arr)-1:
                j += 1
            if j == len(arr)-1:
                j+=1
            arr = arr[:i]+ arr[i] + str(j - i) + arr[j:]
            i = i + 2
            if i == len(arr)-1 or j >= len(arr):
                break
        else:
            i=i+1
            j = i +1
    print(len(arr))
    return len(arr)


if __name__ == '__main__':
    array1 = 'aabbbcccd'        #a2b3c3d
    array2 = 'abcd'             #abcd
    array3 = 'aaaaaaaaaa'       #a10

    print('array 1 length: ' + str(len(array1)) + '\t compressed array: ' + str(compress(array1)))
    print('array 2 length: ' + str(len(array2)) + '\t compressed array: ' + str(compress(array2)))
    print('array 3 length: ' + str(len(array3)) + '\t compressed array: ' + str(compress(array3)))
