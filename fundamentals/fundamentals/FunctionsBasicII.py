def countDown(num):
    array = []
    for x in range(num,-1,-1):
        array.append(x)
    return array
print(countDown(10))


def printReturn(arr):
    print(arr[0])
    return arr[1]
print(printReturn([9,5]))


def firstPlusLength(arr):
    x = arr[0]
    y = len(arr)
    z = x + y
    return z
print(firstPlusLength([0,1,2,3,4]))


def greaterSecond(arr):
    newArr = []
    if len(arr) < 2:
        return False
    for x in arr:
        if x>arr[0]:
            newArr.append(x)
    print(len(newArr))
    return newArr
print(greaterSecond([2]))
print(greaterSecond([4,5,6,7]))


def lengthValue(size, value):
    arr = []
    for x in range(0,size):
        arr.append(value)
    return arr
print(lengthValue(3,4))
