# Task : Print the prime numbers which are between 1 to entered limit number (n).

# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


num=int(input("Please enter any number : "))
prime=set()
for i in range(2,num+1):
  for a in range(2,i):
          if i%a==0:
             break
  else:
    prime.add(i)
print(list(prime))




