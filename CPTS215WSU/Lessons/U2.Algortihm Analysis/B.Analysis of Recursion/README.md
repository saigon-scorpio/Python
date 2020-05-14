Analyze recursive algorithms

1st section:

	- Implementing Binary Search Tree in 2 ways
		- Recursive way
		- Iterative way
	- Algorithm:
	```
		1. Initialize a start index to 0
		2. Initialize an end index to the length of the list minus 1
		3. Initialize a mid index to the middle of the list
		4. While the start index <= end index:
			A. Update mid index
			B. If the item at mid is smaller than target, advance start to mid index plus one
			C. Else if the item at mid is larger than target, decrement end index to mid index minus one
			D. Else the item at mid is the target, return mid
		5. Target not found
	```
	- Done Recursively:
		1. If start < end then not found
		2. If equal then return mid + 1.
		3. If A[mid] < target then recursive call on mid + 1 to end.
		4. If A[mid] > target then recursive call on start to mid - 1.




