import os 

# To indicate infinite number of arguments use parameter *args
#An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:
def mean(*args):
    return sum(args)/len(args) 

print(mean(1,3))


def convertUpper(*args):
    l = []
    for a in args:
        l.append(a.upper())
    l.sort() # sort is in place function, changes L but returns None 
    return l

#print(convertUpper("str", "als", "kgfkl"))

# key word arguments function should be called with *kwargs and will return in the form of dictionary 
#  An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
# to get the key use kwargs.get
def testKeyWordarg(**kwargs):
    return kwargs

#print(testKeyWordarg(a = 1, s= "str"))


def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)

#print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))


__location__= os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Reading file, created in RAM, thus add close file: 
file = open(os.path.join(__location__,"fruits.txt"), 'r')
print(file.read())

# This will not print two times, because there is a notion of cursor in 
# read file at the beginning of the first read function 
# cursor is at the beginning of the file, whereas at the second print 
# cursor is at the end, thus, it will just print empty line 

print(file.read())

# to print twice you need to store it in the objects
content  = open(os.path.join(__location__,"fruits.txt"), 'r').read()

print(content[:5])

# Count number of occurences in the string of character s 
def getCount(s, filepath):
    #file = open(filepath)
    content1 = filepath
    return content1.count(s)

print(getCount('a', content))

print(content.count("a"))

# Better way to open file is to use with, this way you do not need to close it 

with open("Python data structures/fruits.txt", 'r') as file:
    content = file.read()

print(content)

with open("vegetables.txt", "w") as file:
    file.write("Tomato\nOnion\n")