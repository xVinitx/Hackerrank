input_string = input("Enter a list elements separated by space ")

print("\n")
ar = input_string.split()
#print("user list is ", userList)
# Calculating the sum of input list elements
sum1 = 0
for num in ar:
    sum1 += int(num)
print("Sum = ", sum1)
