def alphabet_init():
	"""
	Create a list with 26 zeros
	Using loop and list method
	"""
	alphabet =  []
	for i in range(26):
		alphabet.append(0)
	return alphabet

def convert_letter_to_int(letter):
	"""
	Write a function to convert a letter into an integer in the range [0-25] to index into the list
	We can do this with the ord(<character>) function and ASCII codes...
	"""
	return ord(letter.lower())-ord('a')

def word_char_count(word):
	"""
	Walk through the word and increment the corresponding list position for each letter
	"""
	alphabet = alphabet_init()
	for i in range(len(word)):
		char_index = convert_letter_to_int(word[i])
		alphabet[char_index] += 1  
	return alphabet

def pretty_print(count_list):
	"""
	Convert the index of non-zero list entries back to characters using chr(<integer>) to
	print out the histogram results
	"""
	for i in range(len(count_list)):
		if (count_list[i] > 0):
			print(chr(i+ord('a')),count_list[i],sep = ": ", end ="\n")

def pretty_print_order(count_list,word):
	"""
	Print word but according to the order
	Tracking the order but update in the data after done
	"""
	for i in range(len(word)):
		if (count_list[ord(word[i].lower())-ord('a')]) > 0:
			print(word[i],count_list[ord(word[i].lower())-ord('a')],sep = ": ", end ="\n")
			count_list[ord(word[i].lower())-ord('a')] = 0

def main():
	"""
	print("Please enter your word: ")
	word = input()
	"""
	count_list = word_char_count("woffrdf")
	pretty_print_order(count_list,"woffrdf")

main()