#divcheck

def divisible(n):
	for i in range(11, 21):
		if n%i != 0: return False
	return True

def go():
	x = 2520
	while divisible(x) == False:
		if x == 1000000: print("x is at one million")
		if x == 1000000000: print("x is at one billion")
		if x == 1000000000000: print("x is at one trillion")
		x += 20
	return x

print("The script ran.")