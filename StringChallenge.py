#Have the function StringChallenge(**str**) take the **str** parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (**ie.** c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
#Examples
#Input: "hello*3"
#Output: Ifmmp*3
#Input: "fun times!"
#Output: gvO Ujnft!



def stringchallange(word):
    result = ''
    vowels = ['a','e','i','o','u']
    for i in word:
        if i.isalpha():
            if ord(i) == 122:
                change = chr(97)
            else:
                change = chr(ord(i)+1)
            if change in vowels:
                result += change.upper()
            else:
                result += change
        else:
            result += i
    return result
print(stringchallange("hello*3"))



####### 2.Way  ##########


import string
lower_letters=list(string.ascii_lowercase)
vovel=["a","e","i","o","u"]
word=input("write a word : ")
for i in word:
  if i in lower_letters:
    word=word.replace(i, lower_letters[(lower_letters.index(i)+1)%len(lower_letters)])
for i in word:
  if i in vovel:
    word=word.replace(i, i.upper())
print(word)




