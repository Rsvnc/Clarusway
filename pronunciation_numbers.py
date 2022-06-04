# Write a program that takes a maximum two-digit (1-99) number from the user and finds the pronunciation of that number. For example:

# İnput:97

# Output:Ninety Seven
  
  
num=int(input("Please enter a number between (1-99)  : "))
singledigit=["","one","two","three","four","five","six","seven","eight", "nine"]
special=["ten","eleven","twelve","thirteen","fourteen","fiveteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
twodigits=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
one_digit=num%10
two_digit=num//10
if two_digit==1:
  print(special[one_digit].title())
else:
  print(twodigits[two_digit].title(), singledigit[one_digit].title())
  
  
  
  
  ### in turkish number ###
  
  
num=int(input("Please enter a number between (1-99)  : "))
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi", "otuz","kırk", "elli", "altmış","yetmiş", "seksen", "doksan"]
one_digit=num%10
two_digit=num//10
print(onlar[two_digit].title(),birler[one_digit].title())




