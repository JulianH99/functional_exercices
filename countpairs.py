def count_pairs(lst):
    if not list:
        return 0

    return len([x for x in lst if x % 2 == 0])


print(count_pairs([1, 3, 4, 5, 6, 10, 14, 15, 16, 18]))
