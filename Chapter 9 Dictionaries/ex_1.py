# Exercise 1: 
# Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. 
# Then you can use the in operator as a fast way 
# to check whether a string is in the dictionary.

  
count = 0
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue                        # Discards duplicates
        dictionary_words[word] = count      # Value is first time word appears

if 'We' in dictionary_words: # This part is case-sensitive
    print('True')
else:
    print('False')
    
    
