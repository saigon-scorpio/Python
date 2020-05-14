def iterative(sequence, target):
	'''
	REQUIRED: sequence is sorted list
	This is binary search to find if target is in sequence.
	If not found, return -1.
	If find, return index (in terms of (1...n)).
	This is done iteratively.
	'''
	start = 0
	end = len(sequence) - 1
	mid = (start + end) // 2
	while (start <= end):
		if (sequence[mid] ==  target):
			return mid + 1
		elif (sequence[mid] > target):
			end = mid - 1
		elif (sequence[mid] < target):
			start = mid + 1
		mid = (start + end) // 2
	return -1


def recursive (sequence, target):
	'''
	REQUIRED: sequence is sorted list
	This is binary search to find if target is in sequence.
	If not found, return -1.
	If find, return index (in terms of (1...n)).
	This is done recursively.
	'''
	return recursive_bs(sequence, 0, len(sequence) - 1, target)

def recursive_bs(sequence, start, end, target):
	'''
	PARAMETERS: start is start index
	end is end index
	REQUIRED: sequence is sorted list
	This is binary search to find if target is in sequence.
	If not found, return -1.
	If find, return index (in terms of (1...n)).
	'''
	if (start > end):
		return -1
	mid = (start + end)//2
	if (sequence[mid] == target):
		return mid + 1
	elif (sequence[mid] > target):
		return recursive_bs(sequence,start,mid-1,target)
	else:
		return recursive_bs(sequence,mid+1,end,target)

def main():
	'''
	main program
	'''
	test_seq = [1,3,4,5,6]
	print(iterative(test_seq,4))
	print(recursive(test_seq,4))

main()

