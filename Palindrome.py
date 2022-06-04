# Write a program to check if a given string is a Palindrome. A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

# INPUT: aba

# OUTPUT: True



def palindrome(text:str):
    return text[::-1].lower()==text.lower()
print(palindrome("aba"))
print(palindrome("ccaacc"))
print(palindrome("mom"))
print(palindrome("Aba"))
print(palindrome("Abca"))




