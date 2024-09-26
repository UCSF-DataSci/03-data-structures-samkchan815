#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys

def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies

    # Your code here
    punctuation = """\'!()-[];:,\<>./\"?@#$%’^&‘*_~“”"""
    text = text.lower()
    wordList = text.split()
    wordList = sorted(wordList)

    for i in range(len(wordList)): # loop through each word in list
        for letter in wordList[i]: # loop through each letter in word
            if letter in punctuation:
                wordList[i] = wordList[i].replace(letter, '') # clean up punctuation

        if '—' in wordList[i]: # remove — between words
            splitWord = wordList[i].split('—')
            wordList[i] = splitWord[0] # replace joint word with first word
            if splitWord is not '':
                wordList.extend(splitWord[1]) # add second word if there is one

        if wordList[i] in frequencies: # if not already in dict, add 1
            frequencies[wordList[i]] += 1
        else: # else create new dict key-value pair
            frequencies[wordList[i]] = 1

    return frequencies

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)