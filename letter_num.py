# Write a Python program that accepts a string and calculates the number of numbers and letters.

#Input
# Python 3.2 

# Expected output:
# Letters: 6 Numbers:2


import string
word=input("Plesae enter any words : ")
letter=string.ascii_lowercase
number=string.digits
lettercount=0
numcount=0
for i in word:
  if i in letter:
    lettercount += 1
  elif i in number:
    numcount += 1
print(f"{word} consist of {lettercount} letter and {numcount} numbers ")

