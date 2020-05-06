def open_input_file():
	'''
	Read the words.txt in current directory
	Return the file object associated with words.txt
	'''
	return open(r"words.txt",r)

def close_file(file):
	'''
	accepts file object as argument
	closes the file
	'''
	file.close()

def first_five_words():
	'''
	displays first 5 words of the file
	each words on each line
	'''
	for i in range(5):
		line = file.readline()
		print("%s" %(line), end = "\n")

def main():
	'''
	main output of the program
	'''	
	file = open_input_file()
	first_five_words()
	close_file(file)
