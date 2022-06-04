# Let's learn about list comprehensions! You are given three integers x,y  and z representing the dimensions of a cuboid along with an integer n .
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k  is not equal to n .


# Sample Input 0

#1
#1
#1
#2

#Sample Output 0

#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])

