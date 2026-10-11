def second_largest(numbers):
 largest = None # biggest value seen so far
 second = None # second biggest DISTINCT value seen so far
 for n in numbers:
 if largest is None or n > largest:
 # new biggest found, old biggest becomes second
 if largest is not None:
 second = largest
 largest = n
 elif n != largest and (second is None or n > second):
 # n is smaller than largest, different from it, and better than second
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
show([7]) # edge case: only one element
show([]) # edge case: empty list