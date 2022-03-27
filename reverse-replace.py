#Evey Kriter CSCI 0101 this assignment is for practicing recursion

def reverse(text):
    '''reverses a string without using splicing'''
    if len(text) > 0:
        text = text[-1] + reverse(text[0:-1])
        return text
    else:
        return text

print(reverse("codingishard"))


def replace(text, oldsubstr, newsubstr):
    '''replaces a certain letter, word, or phrase in a string with a new letter, word, or phrase'''
    x = text.find(oldsubstr) #this is to find out where to start deleting
    y = len(oldsubstr) #we need to find out how much of the string to delete so we can replace it
    if x > -1:
        #this compiles the substrings into one new string with the letters/words replaced
        text = text[0:x] + newsubstr[0:] + replace(text[x+y:], oldsubstr, newsubstr)
        return text
    else:
        return text
    
print(replace("one fish, two fish, red fish, blue fish", "fish", "fish"))