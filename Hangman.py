# Problem Set 2, hangman.py
# Name: Amirali Malekani Nezhad
# Collaborators: Me, Myself and I


# Hangman Game
# -----------------------------------
# Helper code
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for char in secret_word:
        if (char in letters_guessed) == False:
            guessed = False
            break
        else:
            guessed = True
    return guessed


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    correct_letters = []  # used to store the correct letters
    guessed_string = ""  # the value that is returned
    # if a guessed letter is in the secret word, then store that letter in the correct_letters list
    for item in letters_guessed:
        if item in secret_word:
            correct_letters.append(item)
    # for each letter in the secret word, if it's been guessed, display it in the guessed_string, otherwise display "_ "
    for char in secret_word:
        if char in correct_letters:
            guessed_string += char
        else:
            guessed_string += "_ "
    return guessed_string


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    list_of_all_letters = []
    str = ""
    all_letters = string.ascii_lowercase
    for i in range(len(all_letters)):
        list_of_all_letters.append(all_letters[i])

    def Diff(li1, li2):
        return sorted(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))

    return (str.join(Diff(list_of_all_letters, letters_guessed)))


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = []
    number_of_guesses = 6
    number_of_warnings = 3
    list_of_vowels = ["a","e","i","o","u"]
    list_of_unique_chars = list(set(secret_word))
    print("Welcome to the Hangman game!")
    print("I am thinking about a word with " + str(len(secret_word)) + " letters.")
    print("-------------")
    print("You have " + str(number_of_guesses) + " guesses, choose wisely!")
    print(get_available_letters(letters_guessed))
    while number_of_guesses > 0:
        if not len(letters_guessed) == 0:
            if is_word_guessed(secret_word, letters_guessed)==True:
                print("You have won! Congrats! The word was " + secret_word + ". Play again soon!")
                total_score = (number_of_guesses)*(len(list_of_unique_chars))
                print("Your total score is " + str(total_score) + ".")
                break
        print(get_guessed_word(secret_word, letters_guessed))
        print("You have " + str(number_of_guesses) + " guesses remaining.")
        print("You have " + str(number_of_warnings) + " warnings remaining")
        print("Letters remaining are : " + get_available_letters(letters_guessed))
        inputted = str(input("Please enter a letter : ")).lower()
        while not inputted.isalpha() and len(inputted)==1:
            number_of_warnings-=1
            print("Please input a valid letter")
            inputted=str(input()).lower()
            if inputted.isalpha():
                break
            if number_of_warnings==0:
                number_of_guesses-=1
        if inputted in letters_guessed:
            if number_of_warnings == 0:
                number_of_guesses -= 1
            else:
                number_of_warnings-=1
            continue
        else:
            letters_guessed.append(inputted)
        if inputted in secret_word:
            print("Nice guess!")
            continue
        else:
            if inputted in list_of_vowels :
                number_of_guesses-=2
            else :
                number_of_guesses -= 1
            print("Ooh try again.")
    if is_word_guessed(secret_word, letters_guessed) == False:
        print("Oh tough luck! The word was + " + secret_word + ". Better luck next time!")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_word = my_word.replace(" ", "")
    other_word = other_word.replace(" ", "")
    checked_chars = []
    if not len(my_word) == len(other_word):
        return False
    else:
        for j in range(len(my_word)):
            if my_word[j] == other_word[j]:
                val = True
                checked_chars.append(my_word[j])
            elif my_word[j] == "_" and other_word[j] in checked_chars:
                val = False
                break
            elif my_word[j] == "_":
                continue
            else:
                val = False
                break
    return val


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """
    list_of_matches = []
    for i in range(len(wordlist)):
        if match_with_gaps(my_word,wordlist[i]) == True:
            list_of_matches.append(wordlist[i])
    if len(list_of_matches)==0:
        print("No matches found.")
    else:
        print(', '.join(list_of_matches))


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = []
    number_of_guesses = 6
    number_of_warnings = 3
    list_of_vowels = ["a", "e", "i", "o", "u"]
    current_guess = ""
    list_of_unique_chars = list(set(secret_word))
    print("Welcome to the Hangman game!")
    print("I am thinking about a word with " + str(len(secret_word)) + " letters.")
    print("-------------")
    print("You have " + str(number_of_guesses) + " guesses, choose wisely!")
    print(get_available_letters(letters_guessed))
    while number_of_guesses > 0:
        if not len(letters_guessed) == 0:
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("You have won! Congrats! The word was " + secret_word + ". Play again soon!")
                total_score = number_of_guesses * (len(list_of_unique_chars))
                print("Your total score is " + str(total_score) + ".")
                break
        print(get_guessed_word(secret_word, letters_guessed))
        current_guess = get_guessed_word(secret_word, letters_guessed)
        print("You have " + str(number_of_guesses) + " guesses remaining.")
        print("You have " + str(number_of_warnings) + " warnings remaining")
        print("Letters remaining are : " + get_available_letters(letters_guessed))
        inputted = str(input("Please enter a letter : ")).lower()
        if inputted == "*":
            show_possible_matches(current_guess)
        else:
            while not inputted.isalpha() and len(inputted) == 1:
                number_of_warnings -= 1
                print("Please input a valid letter")
                inputted = str(input()).lower()
                if inputted.isalpha():
                    break
                if number_of_warnings == 0:
                    number_of_guesses -= 1
            if inputted in letters_guessed:
                if number_of_warnings == 0:
                    number_of_guesses -= 1
                else:
                    number_of_warnings -= 1
                continue
            else:
                letters_guessed.append(inputted)
            if inputted in secret_word:
                print("Nice guess!")
                continue
            else:
                if inputted in list_of_vowels:
                    number_of_guesses -= 2
                else:
                    number_of_guesses -= 1
                print("Ooh try again.")
    if is_word_guessed(secret_word, letters_guessed) == False:
        print("Oh tough luck! The word was " + secret_word + ". Better luck next time!")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #secret_word = "babies"
    secret_word = random.choice(wordlist)
    hangman_with_hints(secret_word)
