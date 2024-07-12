#code that turns word to plurals
def pluralise(word: str):
	"""This function is used to pluralise a given word"""
	vowel_letters = ["a", "e", "i", "o", "u"]
	if word[len(word) - 2] in vowel_letters and word[-1] != 's':
		first_word = word + 's'
		return f'The plural of the {word} is {first_word}'

	elif word[-1] == 's':
		second_word = word + "'"
		return f"The plural of the word {word} is {word} but if it's a name, the plural is {second_word}"

	elif word[-1] == 'y':
		third_word = word[:(len(word) -1)] + "ies"
		return f'The plural of the word {word} is {third_word}'

	elif word[len(word) - 2:] == "fe":
		fourth_word = word[:(len(word) -2)] + "ves"
		return f'The plural of the word {word} is {fourth_word}'

	else:
		new_plural = word + "s"
		return f'The plural of the word {word} is {new_plural}'

while True:
	user_word= input("input your word to get the plural form of it: ").replace(" " , "")
	print(pluralise(user_word)) 
