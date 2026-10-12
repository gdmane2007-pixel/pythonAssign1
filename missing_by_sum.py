
def missing_by_sum(numbers, n):
    expected_total = n * (n + 1) // 2
    actual_total = 0

    for x in numbers:
        actual_total += x

    return expected_total - actual_total


def missing_by_xor(numbers, n):
    result = 0

    for i in range(1, n + 1):
        result ^= i

    for x in numbers:
        result ^= x

    return result


numbers = [1, 2, 4, 6, 3, 7, 8]
print("Sum method:", missing_by_sum(numbers, 8))
print("XOR method:", missing_by_xor(numbers, 8))

numbers = [2, 3, 4, 5]
print("Sum method:", missing_by_sum(numbers, 5))
print("XOR method:", missing_by_xor(numbers, 5))

print(missing_by_sum([1, 2, 3], 4))
print(missing_by_xor([], 1))
