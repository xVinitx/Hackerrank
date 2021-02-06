n = int(input())

# Below line read inputs from user using map() function  
A = list(map(int, input().strip().split()))[:n]

A = list(dict.fromkeys(A))
A.sort()

# printing the second last element
print(A[-2])
