for i in range(101):
	if i != 7 and i % 7 != 0:
		if i % 10 != 7 and i // 10 != 7:
			print('{}'.format(i))
