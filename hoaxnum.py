#Given a number ‘n’, check whether it is a hoax number or not. 
#A Hoax Number is defined as a composite number, whose sum of digits is equal to the sum of digits of its distinct prime factors. It may be noted here that, 1 is not considered a prime number, hence it is not included in the sum of digits of distinct prime factors.
#Examples : 
 

#Input : 22
#Output : A Hoax Number
#Explanation : The distinct prime factors of 22 
#are 2 and 11. The sum of their digits are 4, 
#i.e 2 + 1 + 1 and sum of digits of 22 is also 4.

#Input : 84
#Output : A Hoax Number
#Explanation : The distinct prime factors of 84 
#are 2, 3 and 7. The sum of their digits are 12, 
#i.e 2 + 3 + 4 and sum of digits of 84 is also 12.

#Input : 19
#Output : Not a Hoax Number
#Explanation : By definition, a hoax number is 
#a composite number.



def hoax(x):
  number=0
  for j in str(x):
    number+=int(j)
  prime=set()
  num=2
  while x>1:
    if x%num==0:
      prime.add(num)
      x=x/num
    else:
      num+=1
  ttl=0
  for i in prime:
    for k in str(i):
      ttl+=int(k)
  if len(prime)==1:
      return "Not Hoax Number"
  elif ttl==number:
      return "A Hoax Number"
  else:
      return "Not Hoax Number"
print(hoax(22))
print(hoax(84))
print(hoax(19))



