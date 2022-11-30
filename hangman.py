# Problem Set 2, hangman.py
# Name: Sheliah Nataliia
# Collaborators:-
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():

    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')
    
    line = inFile.readline()
    
    wordlist = line.split()
    
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):

  return random.choice(wordlist)
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

  letters_guessed = set(letters_guessed)
  for letter in secret_word:
      if letter not in letters_guessed:
        return False
  return True


def get_guessed_word(secret_word, letters_guessed):

  letters_guessed = set(letters_guessed)  
  result = ''
  for letter in secret_word:
    if letter in letters_guessed:
      result += letter
    else:
      result += '_'
  result = result.replace('  ', ' ') 
  return result.strip()


def get_available_letters(letters_guessed):

  letters1 = string.ascii_lowercase
  for let in letters_guessed:
        letters1 = letters1.replace(let, "")
  return letters1

    
    

def hangman(secret_word):
    
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = set()
    n = "-"*30

    print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have {warnings_remaining} warnings left.')

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
      print(n,f'\nYou have {guesses_remaining} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')

      input_a = input('Please guess a letter: ').strip().lower()
      
      invalid = not (input_a.isalpha() and len(input_a) == 1)
      already_is = input_a in letters_guessed
      
      if invalid or already_is:
        if invalid:
          print('Oops! That is not a valid letter.', end=' ')
        else:
          print("Oops! You've already guessed that letter.", end=' ')

        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'You have {warnings_remaining} warnings left:', end=' ')
        else:
          guesses_remaining -= 1
          print('You have no warnings left so you lose one guess:', end=' ')
      else:
        letters_guessed.add(input_a)
        if input_a not in secret_word:
          if input_a in 'aeiou':
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
            print(f'Oops! That letter is not in my word:', end=' ')
        else:
          print(f'Good guess:', end=' ')
      print(get_guessed_word(secret_word, letters_guessed))

    print(n)
    if guesses_remaining < 0:
      print('Congratulations, you won!')
      print(f'Your total score for this game is: {len(set(secret_word)) * guesses_remaining}')
    else:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

  


def match_with_gaps(my_word, other_word):

  my_word = my_word.replace(' ','')
  if len(my_word) != len(other_word):
        return False
  for i, letter in enumerate(other_word):
        if my_word[i] == letter:
            continue
        elif my_word[i] == '_' and letter not in my_word:
            continue
        return False
  return True


def show_possible_matches(my_word):

  my_word_res= ''
  for i in my_word:
    y_word_resault += i
  match_count = 0
  for i in wordlist:
    if match_with_gaps(my_word_res, i):
      match_count += 1
      print(i, end=" ")
  if match_count == 0:
        print('No matches found')


def hangman_with_hints(secret_word):
   
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = set()
    n = "-"*30

    print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have {warnings_remaining} warnings left.')

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
      print(f'You have {guesses_remaining} guesses left.\nAvailable letters: {get_available_letters(letters_guessed)}')

      input_a = input('Please guess a letter: ').strip().lower()
      
      if input_a == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
      
      invalid = not (input_a.isalpha() and len(input_a) == 1)
      already_is = input_a in letters_guessed
      
      if invalid or already_is:
        if invalid:
          print('Oops! That is not a valid letter.', end=' ')
        else:
          print("Oops! You've already guessed that letter.", end=' ')

        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'You have {warnings_remaining} warnings left:', end=' ')
        else:
          guesses_remaining -= 1
          print('You have no warnings left so you lose one guess:', end=' ')
      else:
        letters_guessed.add(input_a)
        if input_a not in secret_word:
          if input_a in 'aeiou':
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
          print(f'Oops! That letter is not in my word:', end=' ')
        else:
          print(f'Good guess:', end=' ')
      print(get_guessed_word(secret_word, letters_guessed))

    print(n)
    if guesses_remaining < 0:
      print('Congratulations, you won!')
      print(f'Your total score for this game is: {len(set(secret_word)) * guesses_remaining}')
    else:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

  

if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)