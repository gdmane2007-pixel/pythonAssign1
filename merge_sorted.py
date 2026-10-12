
def merge_sorted(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


print(merge_sorted([1, 4, 7, 10], [2, 3, 8, 11, 15]))
print(merge_sorted([], [1, 2, 3]))
print(merge_sorted([1, 2], []))
print(merge_sorted([1, 3, 3], [3, 4]))
