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

    no_punctuation = punctuation.sub("", file_string)
    all_lowercase = string.lower(no_punctuation)
    no_vowels = vowels.sub("", all_lowercase)
    no_repeats = consonants.sub(r"\1", no_vowels)

    return no_repeats


punctuation = re.compile(r"[^A-Z|\s|0-9]", re.I)
vowels = re.compile(r"\B[aeiou]\B")
consonants = re.compile(r"(.)\1+")


total_time = 0

for x in range(10):
    start = time.clock()
    SMS_Translator("pg76.txt")
    SMS_Translator("pg1342.txt")
    SMS_Translator("pg1661.txt")
    SMS_Translator("pg4300.txt")
    end = time.clock()
    timey = end-start
    total_time += timey

print "The average time taken per application run is: " '{0:.10f}'.format(total_time/10) + " seconds."