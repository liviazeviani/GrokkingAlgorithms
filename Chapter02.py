# Selection sort

def sort(arr):
    minor = arr[0]
    minor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i
    return minor_index


def ordering(arr):
    newArr = []
    for i in range(len(arr)):
        minor = sort(arr)
        newArr.append(arr.pop(minor))
    return newArr


print(ordering([5, 3, 6, 2, 10]))
