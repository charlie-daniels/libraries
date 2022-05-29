import math

def binary(arr, target):
	"""Returns the index of the first occurance of
	an integer in a sorted array using a binary search"""

	min = 0
	mid = 0
	max = len(arr)
	while True:
		mid = (min + max) // 2
		if arr[mid] == target:
			return mid
		elif target > arr[mid]:
			min = mid + 1
		else:
			max = mid - 1
	return -1

def linear(arr, target):
	"""Returns the index of the first occurance of
	an integer in an array using a linear search"""

	for i, val in enumerate(arr):
		if val == target:
			return i
	return -1

# import itertools

def jump(arr, target):
	"""Returns the index of the first occurance of
	an integer in a sorted array using a jump search"""

	arr_len = len(arr)
	block_size = math.sqrt(arr_len)
	step = block_size
	prev = 0

	while arr[int(min(step, arr_len) - 1)] < target:
		prev = step
		step += block_size
		if prev >= arr_len:
			return -1

	temp_arr = arr[int(prev):int(prev+block_size)]
	return linear(temp_arr, target) + int(step - block_size)






