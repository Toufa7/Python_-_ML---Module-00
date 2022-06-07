import sys

def check_even_or_odds(x):
    if (x == 0):
        return ("Zero")
    if (x % 2) == 1:
        return ("Even")
    else:
        return ("Odds")

print(check_even_or_odds(sys.argv[1]))
