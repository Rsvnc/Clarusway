# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

# pluralize(["table", "table", "table"]) ➞ { "tables" }

# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }


def pluralize(mylist):
  new=[]
  for i in mylist:
    if mylist.count(i)>1:
      new.append(i+"s")
    else:
      new.append(i)
  return set(new)
print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))




