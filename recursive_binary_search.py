def recursive_binary_search(lst, target):
    """
    A recursive binary search that returns True is Target
    item is in a list or returns False if the item is not
    in the list
    """
    # if empty list is passed
    if len(lst) == 0:
        return False
    # if the list is not empty
    else:
        midpoint = (len(lst)) // 2

        if lst[midpoint] == target:
            return True
        else:
            if lst[midpoint] < target:
                return recursive_binary_search(lst[midpoint + 1:], target)
            else:
                return recursive_binary_search(lst[:midpoint], target)


def verify(output):
    print("Target found: ", output)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = recursive_binary_search(numbers, 17)
verify(result)

result = recursive_binary_search(numbers, 4)
verify(result)
