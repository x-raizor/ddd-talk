def accumulate(list):
	''' (list of numbers) -> list of numbers
		Create list of absolute values by summations items in list of increments
	>>> accumulate([1, 2, 3])
	[1, 3, 6]
	>>> accumulate([1, 1, 1])
	[1, 2, 3]
	'''
	sum = 0
	new_list = []
	for item in list:
		value = item + sum
		new_list.append(value)
		sum = value
	return new_list


if __name__ == '__main__':
    import doctest
    doctest.testmod() 