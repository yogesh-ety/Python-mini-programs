digits = [1,2,3,4,5,6,7,8,9,0]

#printing from reverse
print(digits[-1])

#SLICING
#printing the elements in btw
print(digits[0:3]) #includes 0th element excludes 3rd element
print(digits[0:-1])

#printing elements in definite intervals
print(digits[0:-1:2])  # prints the elements in the index 0 2 4 6 8 10

for i in range(len(digits)):
    print(digits[0:i])

windows = 4
for i in range(len(digits)-(windows-1)):
    print(digits[i:i+windows])


