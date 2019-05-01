
def equal_list(lst1, lst2):
    return False not in [a == b for a, b in zip(lst1, lst2)]


print(equal_list([1, 2, 3], [1, 2, 3]))
