def is_palindrome(text, left, right):
 
 if left >= right:
 return True
 
 if text[left] != text[right]:
 return False

 return is_palindrome(text, left + 1, right - 1)
def check(text):
 return is_palindrome(text, 0, len(text) - 1)
print(check("racecar"))
print(check("python"))

print(check("")) 
print(check("a")) 
print(check("abba")) 
print(check("abca"))
