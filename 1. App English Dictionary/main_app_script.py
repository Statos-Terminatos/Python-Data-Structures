import json
import os
import difflib
import sys

with open("data.json") as file:
    data = json.load(file)

data_lower = {k.lower(): v for k, v in data.items()}

def typeYesNo(word):

    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}
    choice = input("May be you meant %s? Type yes or no: " % word.upper()).lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        while (choice not in yes) or (choice not in no):
            choice = input("Please enter yes or no. May be you meant %s? Type yes or no: " % word.upper()).lower()
            if choice in yes:
                    return True
            elif choice in no:
                    return False
 
def translateWord():
    word = input("Enter a word you are searching for: ")
    word = word.lower()
    if word in data_lower.keys():
        return "The definition of word %s is:\n%s" %( word.upper(), data_lower[word][0])
    elif len(difflib.get_close_matches(word, data_lower.keys()))>0:
        i = 0
        yesNo =False
        l = difflib.get_close_matches(word, data_lower.keys(), n = 5)
        while yesNo !=True:
            try : 
                word_similar = l[i]
                yesNo = typeYesNo(word_similar)
                i +=1
            except IndexError: 
                return ("No other words close to %s found"  % word.upper()) 
        return "The definition of word %s is:\n %s" %( word_similar.upper(), data_lower[word_similar][0])    
    else:     
        return "Sorry, I do not know word %s" % word.upper()

print(translateWord())