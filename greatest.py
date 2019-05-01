def greatest(lst):
    if not lst:
        return 0
    if lst[0] > greatest(lst[1:]):
        return lst[0]
    return greatest(lst[1:])


print(greatest([1, 3, 4, 50, 100, 7, 8, 10]))
