
def reverse(lst):
    if not lst:
        return []
    return reverse(lst[1:]) + [lst[0]]


print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))
