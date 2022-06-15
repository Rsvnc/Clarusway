#Ask the user for an integer (for example: 100) and find "which numbers form a Pythagorean relation" in the numbers "1 to this number".
 # * Pythagorean Relation -> a**2 + b**2 = c**2
 # Rules:
 # * "import" cannot be used.
 # * The number received from the user is included in the search.

max_int = input("Input maximum number: ")
list_to_max = range(1, int(max_int)+1)
for a in list_to_max:
  for b in list_to_max[(a-1):]:
    c = (a**2 + b**2)**0.5
    if c in list_to_max[b:]:
      print(a, b, int(c))
      
      
      
