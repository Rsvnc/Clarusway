# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find # the score of the runner-up.


# Sample Input 
#5
#2 3 6 6 5
#Sample Output
5


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    myset=set(arr)
    myset.remove(max(myset))
    print(max(myset))
    
    
    
    
    
