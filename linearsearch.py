# A simple approach is to do a linear search, i.e  

# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of elements, return -1.


def search(num,array):
    if num in array:
      return array.index(num)
    return -1

print(search(110,[10, 20, 80, 30, 60, 50, 110, 100, 130, 170]))
print(search(110,[10, 20, 80, 30, 60, 50]))


