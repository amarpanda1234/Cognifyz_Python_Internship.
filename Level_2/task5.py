# FILE MANIPULATION
# =================

import string

def count_word_occurences(filename):
    word_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(string.punctuation)
                    word_counts[word] = word_counts.get(word, 0) + 1
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        return None
    return word_counts

def display_word_count(word_counts):
    if word_counts:  # Only display if word_counts is not None
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0].lower())
        for word, count in sorted_word_counts:
            print(f"{word} : {count}")
    else:
        print("No word counts to display.")

while True:
    filename = input("Enter the filename: ")
    word_count = count_word_occurences(filename)
    
    if word_count is not None:  # If word_count is valid, proceed to display
        display_word_count(word_count)
        break
    else:
        choice = input("Do you want to enter another filename? (yes/no): ").lower()
        if choice != "yes":
            break


'''
OUTPUT
======
Enter the filename: tech.txt
 : 1
all : 1
are : 2
Everyone : 1
fine : 1
go : 1
healthy : 1
Hello : 1
How : 1
hpoe : 1
I : 1
Let's : 1
outside : 1
you : 2
'''