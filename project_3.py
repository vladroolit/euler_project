print('Простые делители числа 13195 - это 5, 7, 13 и 29.\nКаков самый большой делитель числа 600851475143, являющийся простым числом?')
a = []
y = []
n = 10000
for j in range(2, n+1):
    prime = True
    for i in range(2, j):
        if j % i == 0:
            prime = False
            break
    if prime:
        a.append(j)
   
for x in a:
	if 600851475143 % x != 0:
		pass
	if 600851475143 % x == 0:
	    y.append(int(x))
print('\n\n')
print(max(y))
