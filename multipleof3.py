#The very first solution that comes to our mind is the one that we learned in school. If the sum of digits in a number is a multiple of 3 then the number is a multiple #of 3, e.g., for 612, the sum of digits is 9 so it’s a multiple of 3. But this solution is not efficient. You have to get all decimal digits one by one, add them and #then check if the sum is a multiple of 3.




num=int(input("Enter a number : "))
sum=0
for i in str(num):
  sum+=int(i)
if sum%3==0:
  print(num ,"is  multiple of 3")
else:
  print(num ,"is not a multiple of 3")
  
  
  
  
  
