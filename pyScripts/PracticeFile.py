import sys
import random               # to generate random number
print(sys.version)          # Import sys and print pthon version

# Indentation example
x =  5
y = "Hello Dip!" # y = 'Hello Dip!' --> Also same
y = str(x)       # Casting to str
z = int(y)       # Casting to int
o = float(x)     # Casting to float
print(type(x))
print(type(y))
print(type(z))
print(type(o))
x,y,o = 4,"hi!",1.2 # Assign multiple values to multiple
x=z=9               # Assign Single value to multiple
w = """ This is a 
Multiline Comment/string ''' can be used too
"""
print(y)         # print command
if x>3:
    print ("x is greater than 3!")  # Same block same number of indentation

#Unpacking
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)
# Output variables
print (a,b,c)
print (a+b+c)

# Local variables
def myfunc():
    m = "fantastic"     #m is declared local
    print("Python is " + m)
myfunc()
# Global variables
def myfunc2():
    global x           #x is global here
    x = str(x)+"fantastic"
    print(x)
myfunc2()

# Data Types:
# Text Type : str
# Numeric Type: int, float, complex
# Sequence Type: list, tuple, range
# Mapping Type: dict
# Set Type: set, frozenset
# Boolean Type: bool
# Binary Type: bytes, bytearray, memoryview
# None Type: NoneType
cx = 1j                             # Complex           # cx = complex(1j)
cl = ["apple", "banana", "cherry"]  # list              # cl = list(("apple", "banana", "cherry"))
ct = ("apple", "banana", "cherry")  # Tuple             # ct = tuple(("apple", "banana", "cherry"))
cr = range(6)                      # Range
cd = {"name" : "John", "age" : 36}  # Set               # cd = dict(name="John", age=36)
cs = {"apple", "banana", "cherry"}  # set               # cs = set(("apple", "banana", "cherry"))
cfs = frozenset({"apple", "banana", "cherry"}) # Frozenset  # frozenset(("apple", "banana", "cherry"))
cby = b"Hello"                      # byte
cbya = bytearray(5)                 # byte array
cmv = memoryview(bytes(5))          # Memory view
cn = None                           # None

# Random number
print (random.randrange(1,10))    # print a random number

# String
print(w)
print(w[9])                         # Access string as an array
print(len(w))                       # print length of a string
for i in w:                         # Looping through strings
    print(i)
print("line" in w)                  # check if a phrase is present in string --> Opposite "not in"
if "line" in w:                     # in if condition   --> Opposite "not in"
    print("line is in w")
print(w[1:9])                       #slice a string (first and last position not included)
print(w[:9])                        # Slice default from first
print(w[0:])                        # Slice default to the last
print(w[-10:-6])                    # Use negative position -- count from last
print(w.upper())                    # Change string to uper case
print(w.lower())                    # Change string to lower case
print(w.strip())                    # remove spaces
print(w.replace("/"," or ")) # replace substring
print(w.split(" "))                 # Split string to parts based on parameter

# Format string                     # use leading f to format string
txt = f"Hello Dip! X is now {z}"
txt = f"Hello Dip! X is now {z:.2f}"
txt = f"Hello Dip! X is now {3*20}"
print (txt)
# use / character in string to use not permitted characters
txt = "We are the so-called \"Vikings\" from the north."
print(len(txt))
# Condition
if (len(txt)>10):
    print("large!")
else:
    print("small")
# Check instance type of x
print(isinstance(x,int))
# Arithmetic Operator: + - * / % (Exponentiation **) (Floor division //)
# Assignment Operator: =  +=  -=  *=  /=  %=  //=   **=  &=  |=  ^=   >>=  <<=   :=
# Comparison Operator: ==   !=  >   <   >=   <=
# Logical Operator: and   or   not
# Identity Operator:  is    is not
# Membership Operator: in   not in
# Bitwise operator: AND (&), OR (|), XOR (^), NOT (~), ZERO FILL LEFT SHIFT (<<), SIGNED RIGHT SHIFT (>>)
# Precedence: Parentheses, Exponentiation, Unary plus, unary minus, and bitwise NOT,
#             Multiplication, division, floor division, and modulus, Addition and subtraction
#             Bitwise left and right shifts, Bitwise AND, Bitwise XOR, Bitwise OR
#             Comparisons, identity, and membership operators, Logical NOT, AND, OR
# Operators with same precedence are evaluated left to right

# List
thislist = ["banana", "cherry", "apple", 34]    # can contain different types of data
                                                # can use constructor: thislist = list(("apple", "banana", "cherry"))
print(thislist[-1])                             # Negative index means start from end thislist[-1]
print(thislist[1:3])                            # Returns a sub list thislist[:3]   thislist[1:]
print(len(thislist))
if "cherry" in thislist:
    print("cherry found")
