from words import words_list
import random
from pyautogui import *


def getRandomWord(list):
    word = random.choice(list) # choosesk something randomly from the list
    while '-' in word or ' ' in word: #checks if there is a - or a space in the selected word
        word = random.choice(list) #if there is then get another word
    return word.capitalize()# in the end return the word capitalized

def getNumberOfWords():
    wordsWanted = prompt(text='Enter amount of words:',title='Word Amount')
    return int(wordsWanted)

def getTotalWords():
    return words_list.__len__();


def main():
    wordsQuery = getNumberOfWords()
    i = 0
    while(i!=wordsQuery):
        alert(text=getRandomWord(words_list), title='Random Word')# create a pyautogui text box saying the word to make it slightly gui related.
        i=i+1

main()