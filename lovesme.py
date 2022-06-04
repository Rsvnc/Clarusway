# "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one, saying the phrase "Loves me" and "Loves me # # not" when determining whether the one that they love, loves them back.

# Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in # # all caps. Remember to put a comma and space between phrases.

# Loves me, Loves me not, Loves me, Loves me not, LOVES ME



petal=int(input("Please enter the number of petals of your flower  : "))
res="Loves me"
result=""
for i in range(1,petal+1):
  if i % 2==0:
    love=res + ' not'
  else:
    love = res
  if i==petal:
    love= res.upper()
  result+=love+", "
print(result.rstrip(", "))





