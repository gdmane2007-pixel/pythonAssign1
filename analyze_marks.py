
def analyze_marks(*marks):
 if len(marks) == 0:
 print("No marks were supplied.")
 return None
 total = 0
 highest = marks[0]
 passing = 0
 count = 0
 for m in marks:
 total += m
 count += 1
 if m > highest:
 highest = m
 if m >= 40:
 passing += 1
 average = total / count
 print("Total:", total)
 print("Average:", format(average, ".10f"))
 print("Highest:", highest)
 print("Passing count:", passing)
 return total, average, highest, passing
analyze_marks(35, 72, 80, 45, 90, 30)
print("---- edge cases ----")
analyze_marks()
analyze_marks(40)
analyze_marks(39, 20)