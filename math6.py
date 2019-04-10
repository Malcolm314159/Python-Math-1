#math6

print("Hello World")

#variables
sum = 0
sum1 = 0

for i in range(1, 101):
	sum += i
	sum1 += i**2

square = sum**2
difference = square - sum1
print("The sum of the squares is "+str(sum1))
print("The square of the sum is "+str(square))
print("The difference between those two is "+str(difference))