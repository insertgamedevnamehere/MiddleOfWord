word = input("Please enter a word: ")
middle_letter = len(word) / 2 # divide the length of the word by 2 to get the middle
middle_letter = int(middle_letter) # typecast to int just in case the division returns a float

''' 
if the length of the word is an even number
the middle_letter indice will be declared
at the middle right ['w' 'o' 'r' 'd']
                              ^
                        middle_letter
'''
if len(word) % 2 == 0:
	# print both the middle left and middle right letters
	print(word[middle_letter - 1], word[middle_letter])
elif len(word) % 2 == 1:
	print(word[middle_letter])
	