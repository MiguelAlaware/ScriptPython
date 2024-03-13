import re


def backwards(string):
    for i in range(len(string)):
        print(string[-i -1])


def find(word, letter, start):
    index = start 
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count(word, letter, start):
    count = 0 
    index = start
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return count 

word = "banana"

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def rotate_word(word, number):
    codified = list() 
    for letter in word:
        codify = ord(letter) + number
        decodify = chr(codify) 
        codified.append(decodify)
    return ''.join(codified)

print(rotate_word("cheer", 7))


        



        
