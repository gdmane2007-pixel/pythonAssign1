
def move_zeros_new_list(numbers):
    non_zero = []
    zero_count = 0

    for n in numbers:
        if n == 0:
            zero_count += 1
        else:
            non_zero.append(n)

    for i in range(zero_count):
        non_zero.append(0)

    return non_zero


# Method 2: Modifying the original list
def move_zeros_in_place(numbers):
    pos = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[pos] = numbers[i]
            pos += 1

    while pos < len(numbers):
        numbers[pos] = 0
        pos += 1


numbers = [0, 1, 0, 3, 12, 0, 5]

print("Original list :", numbers)
print("Method 1 (new list):", move_zeros_new_list(numbers))

move_zeros_in_place(numbers)
print("Method 2 (in place):", numbers)

# Edge cases
print(move_zeros_new_list([]))
print(move_zeros_new_list([0, 0, 0]))
print(move_zeros_new_list([4, 5, 6]))
9999
