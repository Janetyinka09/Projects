from collections import Counter 
import itertools
words = ()
def dict_words(file_name):
    with open(file_name , "r") as file :
        words = file.read().split()
        return [word.lower() for word in words]
def can_form_word(word, letter_count):
    word_counter = Counter(word) 
    for letter, count in word_counter.items():
        if letter_count[letter] < count:
            return(False) 
    return True
def unscrambled_word (scrambled_word , words) :
    scrambled_counter = Counter(scrambled_word) 
    correct_words = [word for word in words if can_form_word(word, scrambled_counter)]
    return correct_words
def main():
    words - dict_words("words.txt") 
    while True:
        letters = input("Enter letters to bring out likely possible words from it").replace(" " , "").replace("," , "").replace("." , "").lower() 
        correct_words = unscrambled_word(letters , words)
        if correct_words:
            print("Valid words that can be formed :")
            for word in correct_words:
                print(word)
        else:
            print("Unfortunately, there where no valid words for the letter you inputed") 
if __name__ == "_main_" :
    main()