
def longest_run(numbers):
    if len(numbers) == 0:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


print(longest_run([1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]))
print(longest_run([7, 7, 7, 7]))
print(longest_run([]))
print(longest_run([5]))
print(longest_run([1, 2, 3, 4]))
