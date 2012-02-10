# Carianne Cowley
# 14881187
# Python Regular Expressions Assignment

import re
import string
import time
import difflib

def SMS_Translator(filename):
    """
    This function takes an string as a parameter and returns the SMS version of the text. This equates to text stripped
    of punctuation, uppercase letters, vowels not at the beginning or end of a word, and repeated characters. Each
    operation will be performed by means of a regular expression using the re.sub() function. It then
    """
    file_string = ""

    try:
        fin = open(filename)
        for line in fin:
            file_string += line
        fin.close()
    except IOError:                                                 # Catching file exceptions
        print "ERROR! Invalid filename or corrupt file."

    no_punctuation = punctuation.sub("", file_string)               # Get rid of punctuation
    all_lowercase = string.lower(no_punctuation)                    # Convert all letters to lowercase
    no_vowels = vowels.sub("", all_lowercase)                       # Get rid of vowels within word boundaries
    no_repeats = consonants.sub(r"\1", no_vowels)                   # Get rid of repeating characters
    no_whitespace = spaces.sub(r"\1", no_repeats)                   # Get rid of extra whitespace

    book_wordlist = all_lowercase.split()                           # List of English words for future reference
    sms_wordlist = no_whitespace.split()

    english_text = ""
    reference_list = condense_list(book_wordlist)
    reconstructed_list = []
    dict = {}
    x = 0

    while x < len(book_wordlist):
        dict[sms_wordlist[x]] = book_wordlist[x]
        x += 1

    for line in no_whitespace.split("\n"):
        for word in line.split():
            if word not in reference_list:
                entry = dict.get(word)
                english_text += entry + " "
                reconstructed_list.append(entry)
            else:
                english_text += word + " "
                reconstructed_list.append(word)
        english_text += "\n"
        
    fout = open("output.txt", "w")
    for line in english_text:
        fout.write(line)

    return english_text, reconstructed_list, book_wordlist


def condense_list(input_list):
    """
    This function takes in a list and condenses it, getting rid of duplicated entries.
    """
    added = set()
    added_add = added.add
    return [ x for x in input_list if x not in added and not added_add(x)]


punctuation = re.compile(r"[^A-Z|\s|0-9]", re.I)
vowels = re.compile(r"\B[aeiou]\B")
consonants = re.compile(r"(.)\1+")
spaces = re.compile(r"(\s)\1+")

start = time.clock()
text, reconstructed_list, words = SMS_Translator("pg2600.txt")
print text

counter = 0
total = 0
correct = 0

while counter < len(reconstructed_list):
    if reconstructed_list[counter] == words[counter]:
        correct += 1
    else:
        pass
    counter += 1

ratio = (correct / float(counter)) * 100

end = time.clock()
timey = '{0:.10f}'.format(end-start)

print "The total number of words is: " + str(counter + 1)
print "The total number of correct words is: " + str(correct)
print "The accuracy ratio is: " + str(ratio) + "%"
print "The program took: " + str(timey) + " seconds to run."