import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randoly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
def hangman():
    word= get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    #getting user input
    while len(word_letters) > 0:
        #letters used
        print('You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives=lives-1 #takes 1 life away
                print('Letter not in word')
        elif user_letter in used_letters:
            print('You have already used that character, Please try again')
        else:
            print('Invalid character, please try again')
    #gets here when len(word_letters) == 0 OR hen lives ==0
    if lives==0:
        print('yOU DIED', word)
    else:
        print('hhah yu geusses the', word, '!!')
        
hangman()

