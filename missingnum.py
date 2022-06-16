#You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing from the list. #Write an efficient code to find the missing integer.
#Example: 

#Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
#Output: 5

#Calculate the sum of the first n natural numbers as sumtotal= n*(n+1)/2


def missingnum(arr):
     return ((arr[-1]*(arr[-1]+1))//2) - sum(arr)
print(missingnum([1,2,3,4,5,7,8,9]))
print(missingnum([1,2,4,5]))
print(missingnum([1,2,3,4,5,7]))


