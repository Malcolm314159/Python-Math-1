import math
print("Running script...")

n = 600851475143
r2 = int(n**0.5)
r4 = int(n**0.25)

def isprime(a):
	if a == 2 or a == 3: return True
	if a < 2 or a%2 == 0: return False
	if a < 9: return True
	if a%3 == 0: return False
	r = int(a**0.5)
	f = 5
	while f <= r:
		if a%f == 0: return False
		if a%(f+2) == 0: return False
		f += 6
	return True

i = 0
while i < 10:
	if isprime(i) == True:
		print(i)
	i += 1

large_factors = []
for i in range(2, 900000):
	if n%i == 0:
		large_factors.append(int(n/i))

print('Number of large_factors: '+str(len(large_factors)))

x = large_factors[-1]

for i in range(1, x):
	if isprime(i):
		if n%i == 0:
			answer = i
			
print('here is the answer! '+str(answer))
