#a + b + c = 1000
#a2 + b2 = c2

for a in range(10, 950):
	for b in range(10, 850):
		for c in range(10, 900):
			if a**2+b**2 == c**2:
				if a+b+c == 1000:
					answer = a*b*c
					aa = a
					bb = b
					cc = c
	print("checked a = "+str(a))

print("The answer is "+str(answer))
print("a is "+str(aa))
print("b is "+str(bb))
print("c is "+str(cc))