# A Sphenic Number is a positive integer n which is product of exactly three distinct primes. The first few sphenic numbers are 30, 42, 66, 70, 78, 102, 105, 110, 114, … 
# Given a number n, determine whether it is a Sphenic Number or not. 

# Examples: 

# Input : 30
# Output : Yes
# Explanation : 30 is the smallest Sphenic number, 
          # 30 = 2 × 3 × 5 
          # the product of the smallest three primes

# Input : 60
# Output : No
# Explanation : 60 = 22 x 3 x 5
              # has exactly 3 prime factors but
              # is not a sphenic number
    
    
    
def sphenic(x):
  temp=x
  prime=set()
  count=2
  result=1
  while x>1:
    if x%count==0:
      prime.add(count)
      x=x/count
    else:
      count+=1
  for i in prime:
    result*=i
  return  result==temp
print(sphenic(30))
print(sphenic(60))



