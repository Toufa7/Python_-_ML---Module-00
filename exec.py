import sys
def     reverse(x):
    return (x[::-1])
i = 1
while (i < len(sys.argv)):
    print(reverse(sys.argv[i]))
    i += 1
