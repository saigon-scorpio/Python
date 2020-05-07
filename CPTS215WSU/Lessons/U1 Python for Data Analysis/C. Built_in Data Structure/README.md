Suppose we want to keep track of the frequency of letters in a word. For example, the word "hello" has 4 letters with the following frequencies:

	h: 1
	e: 1
	l: 2
	o: 1

Let's write a program to prompt the user to enter a word. Our program will tell the user the frequency of each letter in the word. We could solve this problem with either a list or a dictionary:

List solution:

	- Create a list with 26 zeros
	- Write a function to convert a letter into an integer in the range [0-25] to index into the list. We can do this with the ord(<character>) function and ASCII codes...
	- Walk through the word and increment the corresponding list position for each letter
	- Convert the index of non-zero list entries back to characters using chr(<integer>) to print out the histogram results

Dictionary solution:

	- Create an empty dictionary
	- Walk through the word and add the letter to the dictionary with a count of zero if the letter is not already a key, increment otherwise.


Suggested Solution:

The dictionary solution lends itself more suitable to this problem because we do not have to allocate space for all letters ahead of time and we don't have to perform a character to integer conversion to index into the data structure. Save O(Space)