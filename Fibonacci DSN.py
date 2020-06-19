limit = 4000000
even_fibonacii = []
fibonacii = list(range(1,3))
current = 0
init = 0
while current < limit:
	init = fibonacii[-1] + fibonacii[-2]
	if init < limit:
		fibonacii.append(init)
	current = init
		
for even in fibonacii:
	if even % 2 == 0:
		even_fibonacii.append(even)
sum_even_fibonacii = sum(even_fibonacii)
print(sum_even_fibonacii)