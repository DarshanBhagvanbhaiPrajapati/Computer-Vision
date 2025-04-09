#1 write a programm to find the sum of elements of a list



numbers= [11, 5, 17, 18, 23]

sum =0
for i in range(0, len(numbers)):
	sum = sum + numbers[i]

print("Sum of all elements in given list: ", sum)
