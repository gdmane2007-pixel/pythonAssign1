
def process(numbers):
    squares = []

    for n in numbers:
        if n < 0:
            continue

        if n % 2 != 0:
            continue

        squares.append(n * n)

    total = 0
    count = 0
    largest = None

    for s in squares:
        total += s
        count += 1

        if largest is None or s > largest:
            largest = s

    return total, count, largest


def show(numbers):
    total, count, largest = process(numbers)

    print("Input:", numbers)
    print("Total:", total)
    print("Count:", count)

    if largest is None:
        print("Largest squared value: None (no number satisfied the conditions)")
    else:
        print("Largest squared value:", largest)


show([-2, 1, 2, 3, 4, 6, -8])

print("---- edge cases ----")

show([])
show([1, 3, 5])
show([-2, -4])
show([0, 2])


from functools import reduce


def process_functional(numbers):
    positives = filter(lambda x: x >= 0, numbers)
    evens = filter(lambda x: x % 2 == 0, positives)
    squares = list(map(lambda x: x * x, evens))

    if not squares:
        return 0, 0, None

    total = reduce(lambda a, b: a + b, squares)
    largest = reduce(lambda a, b: a if a > b else b, squares)

    return total, len(squares), largest


print("---- functional version ----")
print(process_functional([-2, 1, 2, 3, 4, 6, -8]))
print(process_functional([1, 3]))
