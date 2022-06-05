# Write a program that takes a number from the user and prints the result to check if it is a prime number

# The examples of the desired output are as follows :

# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number





num=int(input("Enter any numbers  :  "))
for i in range(2,num):
     if num%i==0:
      result="is not a Prime Number"
      break
     else:
      result="is Prime Number"
print(num, result)




