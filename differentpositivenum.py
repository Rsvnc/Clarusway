# Task: Send two different positive integer numbers to the function you will create. Let him subtract the larger one from the smaller one. If the numbers are equal or 
# negative, ask for input again.


def diffnum(x,y):
  while x<0 or y<0 or x==y:
    x=int(input("Please don't let the number be negative and equal: "))
    y=int(input("Please don't let the number be negative and equal: "))
  return f"Difference of two numbers: {sorted([x,y])[1]-sorted([x,y])[0]}"
print(diffnum(int(input("Give me a number: ")),int(input("Give me a different number: "))))



