
import json
import os
import random
import string


def find_index(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def thin_choices(optional_words, correct_guess, correct_indices):
    thinned = []
    for word in optional_words:
        if set(find_index(word, correct_guess)) == set(correct_indices):
            thinned.append(word)
        else:
            continue
    return thinned

def remove_choices(optional_words, wrong_guess):
    return [word for word in optional_words if not any(map(lambda x: x in word, wrong_guess))]


def most_frequent_letter(optional_words):
    letters = {}
    for word in optional_words:
        for letter in word:
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1

    return dict(sorted(letters.items(), key=lambda item: item[1]))



def main():
    with open('./words_by_length.json', 'r') as dataset:
        dataset = json.load(dataset)
        print("welcome to hangman!")
        print("think of a word and i will try to guess it with my infinite knowledge")
        print("---------------------------------------------------------------------")
        print("press any key to start")
        print("---------------------------------------------------------------------")
        input()
        os.system("clear")
        word_length = input("what is the length of your word?\n >")
        optional_words = dataset[word_length]
        frequency = most_frequent_letter(optional_words)
        guessed = []
        tries = 0
        mistakes = 0
        while True:
            frequency = list(most_frequent_letter(optional_words).keys())
            if guessed is not None:
                for i in guessed:
                    frequency.remove(i)
            guess = random.choice(frequency[-7:])
            print("is {} in your word?".format(guess))
            answer = input(">")
            if answer == "y":
                print("in what indices?")
                indices = [int(i) - 1 for i in input(">").split(",")]
                optional_words = thin_choices(optional_words, guess, indices)
                guessed.append(guess)
            elif answer == "n":
                optional_words = remove_choices(optional_words, guess)
                mistakes += 1
    
            if len(optional_words) == 1:
                os.system("clear")
                print ("i guessed your word in {} tries and {} mistakes!\nits {}".format(tries,mistakes,optional_words[0]))
                return
            else:
                print(optional_words)
                tries += 1
                print(tries)




        

if __name__ == '__main__':
    main()