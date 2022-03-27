#Evey Kriter/CSCI0101/10.10.2019

#Find
def find(text, item):
    '''This function is to find the item in a string.'''
    if len(text) == 0:
        return len(text) -1
    elif item == text[-1] and find(text[:-1], item) == -1:
        return len(text) - 1
    else:
        return find(text[:-1], item)

print(find("mad man with a box", " "))

#Write a Converter
def binaryToDecimal(string):
    '''This function is to convert a binary number to a decimal.'''
    if len(string) > 0:
        x = int(string[0]) * (2**(len(string) - 1))
        return binaryToDecimal(string[1:]) + x
    else:
        return 0

print(binaryToDecimal("10001010"))