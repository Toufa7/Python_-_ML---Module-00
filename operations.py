import sys

def sum(x, y):
    rslt = int(x) + int(y)
    return (rslt)

def diff(x, y):
    rslt = int(x) - int(y)
    return (rslt)

def product(x, y):
    rslt = int(x) * int(y)
    return (rslt)

def quotient(x, y):
    rslt = float(x) / float(y)
    return (float(rslt))

def modulo(x , y):
    rslt = int(x) % int(y)
    return (rslt)

if (len(sys.argv) == 2 or len(sys.argv) > 3):
    print ("Please Provide a valid 2 Numbers")
    quit()

if (len(sys.argv) == 1):
    print ("Usage: python operations.py <number1> <number2>")
    print ("Example:")
    print ("    $>python operations.py 10 3")
else:
    x = sys.argv[1]
    y = sys.argv[2]
    print("Sum:         %d" % sum(x,y))
    print("Diffrence:   %d" % diff(x,y))
    print("Product:     %d" % product(x,y))
    print("Quotient:    %.2f" % quotient(x,y))
    print("Remainder:   %d" % modulo(x,y))

# print (type(x))
# if (type(x) == int):
#     print ("Bravo")
#     quit()
# else:
#     print ("Ghierha")
#     quit()
