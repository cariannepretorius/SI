# Carianne Cowley
# 14881187
# Python Regular Expressions Assignment

import re
import string
import time

def SMS_Translator(filename):
    """
    This function takes an string as a parameter and returns the SMS version of the text. This equates to text stripped
    of punctuation, uppercase letters, vowels not at the beginning or end of a word, and repeated characters. Each
    operation will be performed by means of a regular expression using the re.sub() function.
    """
    file_string = ""

    try:
        fin = open(filename)
        for line in fin:
            file_string += line
        fin.close()
    except IOError:
        print "ERROR! Invalid filename or corrupt file."

    punctuation = re.compile(r"[^A-Z|\s|0-9]", re.I)            # Pattern encompasses everything except alphanumeric
    no_punctuation = punctuation.sub("", file_string)           # and whitespace. Replaced by empty string.

    lowercase = re.compile(r"[A-Z]")                            # Pattern encompasses capital letters
    all_lowercase = lowercase.sub(lower_sub, no_punctuation)    # Replaced by lowercase letters using lower_sub()

    vowels = re.compile(r"\B[aeiou]\B")                         # Pattern encompasses vowels within boundaries of word
    no_vowels = vowels.sub("", all_lowercase)                   # Replaced by the empty string

    consonants = re.compile(r"(.)\1+")                          # Pattern encompasses all repeated characters
    no_repeats = consonants.sub(r"\1", no_vowels)               # Replaced by one of the appropriate consonant

    return no_repeats


def lower_sub(match):
    """
    This function takes a given match object from a regular expression and determines each string object (character)
    that has been matched. Each of these are then fed into the string.lower() function which returns the lowercase
    version of the alphabetic character.
    """
    match_string = str(match.group())
    return string.lower(match_string)


total_time = 0

for x in range(10):                                             # Timing 10 application runs
    start = time.clock()
    SMS_Translator("pg76.txt")
    SMS_Translator("pg1342.txt")
    SMS_Translator("pg1661.txt")
    SMS_Translator("pg4300.txt")
    end = time.clock()
    timey = end-start
    total_time += timey

print "The average time taken per application run is: " '{0:.10f}'.format(total_time/10) + " seconds."