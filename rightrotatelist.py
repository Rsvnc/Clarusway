# Given a list, right rotate the list by n position.

# Write a program to shift every element of a list to circularly right.

def rightrotate(mylist:list, num:int):
  return mylist[len(mylist)-num:]+mylist[0:len(mylist)-num]
print(rightrotate([1,3,6,8,9,3,4], 6))


