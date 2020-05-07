def dict_init(word):
	"""
	Create an empty dictionary
	Walk through the word and add the letter to the dictionary with a count
	of zero if the letter is not already a key, increment otherwise.
	"""
	alphabet = {}
	for char in word:
		key = char.lower()
		if not (key in alphabet):
			alphabet[key] = 1
		else:
			alphabet[key] += 1
	return alphabet

def pretty_print(dictionary):
	"""
	Print out result
	Since we follow order of the dictionary, the output result is already in 
	the character order of word.
	"""
	for key in dictionary:
		print(key,dictionary[key],sep = ": ",end = "\n")

def main():
	"""
	main program
	"""
	pretty_print(dict_init("WOfRDF"))

main()
