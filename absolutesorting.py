# Let's try some sorting. Here is an array with the specific rules.

# The array (a list) has various numbers. You should sort it, but sort it by absolute value in ascending order. For example, the sequence (-20, -5, 10, 15) will be #sorted like so: (-5, 10, 15, -20). Your function should return the sorted list or tuple.

#Precondition: The numbers in the array are unique by their absolute values.

#Input: An array of numbers , a tuple..

#Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.



def checkio(values: list) -> list:
    x=[]
    for i in values:
        x.append(abs(i))
    x.sort()
    y=[]
    for i in x:
        if -i in values:
            y.append(-i)
        else:
            y.append(i)
        
    return y

if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
