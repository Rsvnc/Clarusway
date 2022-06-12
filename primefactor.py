#Given two numbers n and k, print k-th prime factor among all prime factors of n. For example, if the input number is 15 and k is 2, then output should be “5”. And if the k is 3, then output should be “-1” (there are less than k prime factors). 
#Examples: 
 

#Input : n = 225, k = 2        
#Output : 3
#Prime factors are 3 3 5 5. Second
#prime factor is 3.

#Input : n = 81, k = 5
#Output : -1
#Prime factors are 3 3 3 3



def primefactor(x,y):
  prime=[]
  num=2
  while x>1:
    if x%num==0:
      prime.append(num)
      x=x/num
    else:
      num+=1
  if y>=len(prime):
    return -1
  else:
    return prime[y-1]
print(primefactor(225,2))
print(primefactor(81,5))


