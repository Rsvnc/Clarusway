#Given a number n, the task is to find out whether this number is smith or not. A Smith Number is a composite number whose sum of digits is equal to the sum of digits in its prime factorization. Examples:

#Input  : n = 4
#Output : Yes
#Prime factorization = 2, 2  and 2 + 2 = 4
#Therefore, 4 is a smith number

#Input  : n = 6
#Output : No
#Prime factorization = 2, 3  and 2 + 3 is
#not 6. Therefore, 6 is not a smith number

#Input   : n = 666
#Output  : Yes
#Prime factorization = 2, 3, 3, 37 and
#2 + 3 + 3 + (3 + 7) = 6 + 6 + 6 = 18
#Therefore, 666 is a smith number

#Input   : n = 13
#Output  : No
#Prime factorization = 13 and 13 = 13,
#But 13 is not a smith number as it is not
#a composite number



def issmith(x):
  sumnum=0
  for i in str(x):
    sumnum+=int(i)
  sum=[]
  prime=2
  result=0
  while x>1:
    if x%prime==0:
         sum.append(prime)
         x=x/prime
    else:
      prime+=1
  if len(sum)==1:
      return False
  else:
    for i in sum:
      for j in str(i):
        result+=int(j)
    return result==sumnum
  
  
print(issmith(6))
print(issmith(666))
print(issmith(4))
print(issmith(13))
print(issmith(166))
print(issmith(202))
print(issmith(265))
print(issmith(57))
print(issmith(75))
print(issmith(92))



