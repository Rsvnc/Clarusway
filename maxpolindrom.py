# Find the largest palindrome made by multiplying a 3-digit number


polindrom=[]
for i in range(100,1000):
  for y in range(100,1000):
        num=i*y
        if str(num)==str(num)[::-1] :
                 polindrom.append(num)                
print(max(polindrom))




        # Second Way #
  
  print(
    max(
    [i * j for i in range(100, 1000) for j in range(100, 1000) if str(i*j) == str(i*j)[::-1] ]
    )
)
  
  
  
  
  
  
