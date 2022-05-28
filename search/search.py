def binary(data, target):
	"""Returns the index of the first occurance of
	 an integer in an array using a binary search"""
	min = 0
	mid = 0
	max = len(data)
	while True:
		mid = (min + max) // 2
		if data[mid] == target:
			return mid
		elif target > data[mid]:
			min = mid + 1
		else:
			max = mid - 1

