# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:52:29 2019

@author: diego
"""
import random as rd
word_list_file="words.txt"
def load_words():
    print("Loading words list from file...")
    infile=open(word_list_file,"r")
    line=infile.readline()
    wordlist=line.split()
    print(" ",len(wordlist),"words loaded.")
    return wordlist

def choose_word(wordlist):
    return rd.choice(wordlist)

def hangman(secret_word):
    length=len(secret_word)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",length,"letters long.")
    chances=6 #2*len(secret_word)
    h=0
   # letters_guessed=[]
    a=""
    while chances!=0:
        x=input("Please type a letter: ")
        print(secret_word)
        if x in secret_word:
            a=a+x
            print(a)
        else:
            h=h+1
        if h==1:
            print(" o")
        elif h==2:
            print(" o")
            print("l")
        elif h==3:
            print(" o")
            print("-l")
        elif h==4:
            print(" o")
            print("-l-")
        elif h==5:
            print(" o")
            print("-l-")
            print("/")
        elif h==6:
            print(" o")
            print("-l-")
            print("//")
            print("Hangman")
            break
    
hangman(choose_word(load_words()))
