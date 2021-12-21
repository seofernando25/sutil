def insertion_sort(l):
    for j in range(len(l) - 1):
        key = l[j + 1]  # key is the current element
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


def merge_sort(l):
    # TODO is not working
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    print(mid, left, right)
    return list(left) + list(right)


ls = [1, 3, 2, 6, 5, 4]

print(ls)
print(merge_sort(ls))