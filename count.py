import string, sys
from sympy import true

def analyse_uppercase(x):
    nbr = 0
    i = 0
    while (i < len(x)):
        if (x[i].isupper() == true):
            nbr = nbr + 1
        i = i + 1
    return (nbr)

def analyse_lowercase(x):
    nbr = 0
    i = 0
    while (i < len(x)):
        if (x[i].islower() == true):
            nbr += 1
        i += 1
    return (nbr)
 
def analyse_spaces(x):
    nbr = 0
    i = 0
    while (i < len(x)):
        if (x[i].isspace() == true):
            nbr += 1
        i += 1
    return (nbr)

def analyse_punctuation(x):
    nbr = 0
    i = 0
    for i in x:
        if i in string.punctuation:
            nbr = nbr + 1
    return (nbr)


x = sys.argv[1]

print("The Text Contain %d Chars" % len(x))
print(" - %d Upper Letters" % analyse_uppercase(x))
print(" - %d Lower Letters" % analyse_lowercase(x))
print(" - %d Spaces Letters" % analyse_spaces(x))
print(" - %d Punctuation Marks" % analyse_punctuation(x))