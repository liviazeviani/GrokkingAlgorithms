# Binary search

def binary_search(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lista[mid]

        if guess == item:
            return mid
        if guess > item:
            high = low - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))
print(binary_search(my_list, 3))
print(binary_search(my_list, 5))
print(binary_search(my_list, 7))
print(binary_search(my_list, 9))


