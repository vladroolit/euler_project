a = b = 1

print(a, end="")
print(b, end="")

for i in range (2, 100):
	a,b = b, a + b
	print(b)
	if b > 4000000000:
		break

