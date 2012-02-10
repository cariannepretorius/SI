# Carianne Cowley
# 14881187
# Python Preparation

# Question 2

def rot13(text):
    """
    This function takes a string of text as a parameter and proceeds to apply ROT13 encryption to it, by creating a new
    string character by character, and then returning the encoded string.
    """
    word = text.strip()
    encoded = ""                                            # Empty string to function as encrypted string

    for char in word:                                       # Traverse string by character
        if char.isalpha():                                  # Perform ROT13 encoding on alphabetic characters
            if (char >= "N" and char <= "Z") or (char >= "n" and char <= "z"):
                encoded += chr(ord(char) - 13)
            else:
                encoded += chr(ord(char) + 13)
        else:                                               # Leave non-alphabetic characters unchanged
            encoded += char
    return encoded                                          # Return encoded string

print rot13(rot13("aBcdeFghijklmnopqrstuvwxyz"))


# Question 3

import re

def re_rot13(text):
    """
    This function takes a character as a parameter and proceeds to apply ROT13 encoding, and then returns that
    encoded character as a string.
    """
    char = text.strip()
    letter = ""                                             # Empty string to function as encoded character

    if (char >= "N" and char <= "Z") or (char >= "n" and char <= "z"):
        letter = chr(ord(char) - 13)                        # Encode character
    else:
        letter = chr(ord(char) + 13)

    return letter                                           # Return encoded character

def rot13_sub(match):
    """
    This function takes a given match object from a regular expression and determines each string object (character)
    that has been matched. Each of these are then fed into the re_rot13 function which determines the encoded version
    of the character and returns it.
    """
    value = str(match.group())
    return re_rot13(value)

pattern = re.compile("[A-Z]", re.I)                         # Creating the pattern to match alphabetic characters
print pattern.sub(rot13_sub, 'abcdefghijklmnopqrstuvwxyz...')
print pattern.sub(rot13_sub, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ...')


# Question 4

def encode_base64(user_input, user_output):
    """
    This function takes an input file and output file as parameters. It then performs Base64 encoding on the text found
    in the input file, and writes the output to the output file. A message concerning the success or failure of the
    operation is returned.
    """
    binary = ""
    encoded = ""
    base64_codes = {                                        # A dictionary of Base64 codes
                    0: "A",
                    1: "B",
                    2: "C",
                    3: "D",
                    4: "E",
                    5: "F",
                    6: "G",
                    7: "H",
                    8: "I",
                    9: "J",
                    10: "K",
                    11: "L",
                    12: "M",
                    13: "N",
                    14: "O",
                    15: "P",
                    16: "Q",
                    17: "R",
                    18: "S",
                    19: "T",
                    20: "U",
                    21: "V",
                    22: "W",
                    23: "X",
                    24: "Y",
                    25: "Z",
                    26: "a",
                    27: "b",
                    28: "c",
                    29: "d",
                    30: "e",
                    31: "f",
                    32: "g",
                    33: "h",
                    34: "i",
                    35: "j",
                    36: "k",
                    37: "l",
                    38: "m",
                    39: "n",
                    40: "o",
                    41: "p",
                    42: "q",
                    43: "r",
                    44: "s",
                    45: "t",
                    46: "u",
                    47: "v",
                    48: "w",
                    49: "x",
                    50: "y",
                    51: "z",
                    52: "0",
                    53: "1",
                    54: "2",
                    55: "3",
                    56: "4",
                    57: "5",
                    58: "6",
                    59: "7",
                    60: "8",
                    61: "9",
                    62: "+",
                    63: "/"
                   }

    file_string = handle_input_file(user_input)             # Append data from file into a string

    if file_string == "":                                   # Handle IO Errors
        return "ERROR! A problem was encountered while processing the input file."
    else:
        for word in file_string:
            for char in word:
                try:
                    ascii_no = ord(char)                    # Fetching ASCII code for each character
                except ValueError:
                    return "ERROR! Illegal character encountered while encoding data."
                binary += dec_to_binary(ascii_no, 8)        # Convert each ascii code into a string of binary digits
                                                            # with length 8 (padding 0's to the left of the digits)
        six_len_binary = split_binary(binary, 6)            # Splitting the binary string into groups of 6 bits each

        for digit in six_len_binary:                        # Providing padding for incomplete sestets of bits
            full = digit.ljust(6, "0")                      # according to MIME specifications
            encoded += base64_codes[int(full, base=2)]
            if len(digit) == 4:
                encoded += "="
            elif len(digit) == 2:
                encoded += "=="

        encoded_lines = split_string(encoded, 76)           # Splitting string of encoded data into lines of no more
                                                            # than 76 characters each according to MIME specifications
        user_message = write_to_file(encoded_lines, user_output)
        return "\n" + user_message                          # Write to file and return message of success or failure


def dec_to_binary(decimal_no, length):
    """
    This function takes a number in the decimal format as well as a specified desired length as parameter, and returns a
    string format of the binary representation of the given decimal number based on the desired length.
    """
    binary_no = ""

    if decimal_no is 0:                                     # Control for 0
        binary_no += "0"

    while decimal_no > 0:                                   # Apply binary algorithm to decimal
        remainder = decimal_no % 2.0
        if remainder == 0.0:
            binary_no += "0"
        else:
            binary_no += "1"

        decimal_no /= 2

    binary_no = binary_no[::-1]                             # Reverse the binary string to reveal correct number
    binary_no = binary_no.rjust(length, "0")                # Pad with zeroes to the left to reach specified length

    return binary_no                                        # Return resulting string


def handle_input_file(filename):
    """
    This function handles a given input file by taking a filename as a parameter and returning the contents of the file
    as a string.
    """
    file_string = ""
    try:
        f = filename + ".txt"                               # Append appropriate extension to filename
        fin = open(f)                                       # Create connection to file
        for line in fin:
            file_string += line                             # Append each line to string
        fin.close()                                         # Close file to avoid data corruption
    except IOError:                                         # Handle file errors
        file_string = ""

    return file_string                                      # Return contents of file as string


def split_binary(whole_binary, length):
    """
    This function takes a binary string and specified length as parameters and returns a list of binary numbers of the
    specified length as a result of splitting the given string into the specified units.
    """
    binary_list = []
    for i in range(0, len(whole_binary), length):
        binary_list.append(whole_binary[i:i+length])

    return binary_list


def split_string(string_output, length):
    """
    This function takes a string and specified length as parameters and returns a list of strings of the specified
    length as a result of splitting the given string into the specified units.
    """
    line_list = []
    for i in range(0, len(string_output), length):
        line_list.append(string_output[i:i+length] + "\n")

    return line_list


def write_to_file(line_list, output_file):
    """
    This function takes a list of line strings and an output file name as parameters and returns a success of failure
    message depending on the outcome of writing the strings in the list to the given file.
    """
    try:
        fout = open(output_file + ".txt", "w")              # Open file and write each line to file
        for line in line_list:
            fout.write(line)
        fout.close()                                        # Close file to avoid data corruption and return message
        return "The output was successfully written to file."
    except IOError:                                         # Handle file errors
        return "ERROR! A problem was encountered while writing to file."


def decode_base64(user_input, user_output):
    """
    This function takes an input file and output file as parameters. It then performs Base64 decoding on the text found
    in the input file, and writes the output to the output file. A message concerning the success or failure of the
    operation is returned.
    """
    binary = ""
    count_pads = 0
    decimal_list = []
    decoded_list = []
    base64_chars = {                                        # A dictionary of Base64 codes
                    0: "A",
                    1: "B",
                    2: "C",
                    3: "D",
                    4: "E",
                    5: "F",
                    6: "G",
                    7: "H",
                    8: "I",
                    9: "J",
                    10: "K",
                    11: "L",
                    12: "M",
                    13: "N",
                    14: "O",
                    15: "P",
                    16: "Q",
                    17: "R",
                    18: "S",
                    19: "T",
                    20: "U",
                    21: "V",
                    22: "W",
                    23: "X",
                    24: "Y",
                    25: "Z",
                    26: "a",
                    27: "b",
                    28: "c",
                    29: "d",
                    30: "e",
                    31: "f",
                    32: "g",
                    33: "h",
                    34: "i",
                    35: "j",
                    36: "k",
                    37: "l",
                    38: "m",
                    39: "n",
                    40: "o",
                    41: "p",
                    42: "q",
                    43: "r",
                    44: "s",
                    45: "t",
                    46: "u",
                    47: "v",
                    48: "w",
                    49: "x",
                    50: "y",
                    51: "z",
                    52: "0",
                    53: "1",
                    54: "2",
                    55: "3",
                    56: "4",
                    57: "5",
                    58: "6",
                    59: "7",
                    60: "8",
                    61: "9",
                    62: "+",
                    63: "/"
                   }

    base64_codes = dict((v,k) for k, v in base64_chars.iteritems())
                                                            # Reverse dictionary of codes for reverse lookup
    file_string = handle_input_file(user_input)             # Handle input file and fetch string containing file data

    file_string = file_string.replace("\n", "")             # Replace line breaks with the empty string

    for word in file_string:                                # Count the padding characters in encoded data and look up
        for char in word:                                   # the codes for the given characters and append to list
            if char in base64_codes.keys():
                code = base64_codes[char]
                decimal_list.append(code)
            elif char is "=":
                count_pads += 1
            else:
                return "ERROR! Illegal character encountered while decoding data."

    for decimal in decimal_list:                            # Convert each Base64 code into binary stings of length 6
        binary += dec_to_binary(decimal, 6)

    if count_pads == 1:
        binary = binary[0:len(binary) - 2]                  # Trim the padding from the final sestet if required and
    elif count_pads == 2:                                   # append to binary string
        binary = binary[0:len(binary) - 4]

    binary_list = split_binary(binary, 8)                   # Split the binary string into octets

    for octet in binary_list:                               # Decode each octet into its original ASCII character
        decoded_list.append(chr(int(octet, base=2)))

    user_message = write_to_file(decoded_list, user_output) # Write to file and return message of success or failure

    return "\n" + user_message

                                                            # Provide some basic interface for user
print "------------------------------------------------------------------------------"
print "Welcome to the Base64 Encoder and Decoder".center(78)
print "------------------------------------------------------------------------------"
input_file = raw_input("Please type in the name of the file that you would like to encode or decode:\n" +
                       "(Leave out the extension please)\n")
output_file = raw_input("Please type in the name of the file that you would like to save your output in:\n" +
                       "(Leave out the extension please)\n")
operation = raw_input("\n1. Encode data into Base64\n" + "2. Decode data from Base64\n" + "Q. Quit\n" +
                      "\nWhat would you like to do? (Enter 1, 2, or Q)\n")

if operation == "1":
    print encode_base64(input_file, output_file)            # Test instances
elif operation == "2":
    print decode_base64(input_file, output_file)
elif operation == "Q" or "q":
    pass
else:
    print "You have entered an invalid option. Exiting now..."
print "------------------------------------------------------------------------------"