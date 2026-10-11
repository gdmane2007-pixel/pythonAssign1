def count_chars(text):
 counts = {}
 for ch in text:
 if ch in counts:
 counts[ch] += 1
 else:
 counts[ch] = 1
 return counts
def is_anagram(first, second):
 
 first = first.lower().replace(" ", "")
 second = second.lower().replace(" ", "")
 if len(first) != len(second): 
 return False
 return count_chars(first) == count_chars(second)
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

print(is_anagram("Listen", "Silent"))
print(is_anagram("dormitory", "dirty room"))
print(is_anagram("aab", "abb")) 
print(is_anagram("", "")) 