exec(open('prime.py').read())

sum = 0
for i in range(0, 2000000):
	if isprime(i):
		sum += i
		if i > 1500000:
			print("The script is at "+str(i))

print("The sum is "+str(sum))