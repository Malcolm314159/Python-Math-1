exec(open('prime.py').read())

primes = []
n = 0
while len(primes) != 10001:
	if isprime(n):
		primes.append(n)
	n += 1

print("The answer is "+str(primes[-1]))