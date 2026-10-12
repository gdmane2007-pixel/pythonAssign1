
def second_largest(numbers):
    largest = None
    second = None

    for n in numbers:
        if largest is None or n > largest:
            if largest is not None:
                second = largest
            largest = n

        elif n != largest and (second is None or n > second):
            second = n

    return second


def show(numbers):
    result = second_largest(numbers)

    if result is None:
        print(numbers, "->", "No second-largest distinct value")
    else:
        print(numbers, "->", result)


show([12, 35, 1, 10, 34, 35])
show([5, 5, 5, 4])
show([10, 10, 10])
show([-5, -2, -10, -1])
show([7])
show([])
