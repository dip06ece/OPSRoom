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
print(thislist)
if "cherry" in thislist:
    print("cherry found")
thislist[1:3] = ["Apple","Cherry"]              # Change a range of values in a list
                                                # Can be used to insert a list in another list
thislist[0:3] = ["Cherry"]                      # Can truncate list too
print(thislist)
thislist.insert(1, "watermelon")# Insert an item to the specified index
print(thislist)
thislist.append("Mango")                         # Adds an item at the end
print(thislist)
thislist.extend(["cow", "horse"])               # Add another list at the end of a list
print(thislist)
thislist.extend(("elephant", "rabbit"))         # Add another tuple/set/dictionaries at the end of a list
print(thislist)
thislist.remove("elephant")                     # Remove an item from list. If multiple remove first
print(thislist)
thislist.pop(-1)                                # Remove item at specified index
print(thislist)
thislist.pop()                                  # Pop the last element
print(thislist)
del(thislist[4])                                # Delete last element of list
print(thislist)
# del(thislist)                                 # Delete the list # thislist undefined from here
thislist.clear()                                # Remove all items from thislist
print(thislist)

## List iteration
thislist = ['Cherry', 'watermelon', 34, 'Mango']
for x in thislist:                              # Loop through list
    print(x)
for x in range(len(thislist)):                  # Loop using index number
    print(thislist[x])
i = 0
while i<len(thislist):                          # Print using while loop
    print("while " + str(thislist[i]))
    i+=1
# List comprehension *** Need to study more
[print(x) for x in thislist]                    ## Looping Using List Comprehension
# newlist = [expression for item in iterable if condition == True]
# newlist = [x for x in thislist if "a" in x]
# newlist = [x for x in thislist if x != "apple"]
#newlist = [x for x in thislist]
newlist = [x for x in range(10)]              # Can use range function to create an iterable
print(newlist)
newlist = [x for x in range(10) if x<5]       # Can use range function and condition to create an iterable
print(newlist)
print(thislist)
newlist = [str(x).upper() for x in thislist]  # Another example
print(newlist)
# newlist = [x if x != "banana" else "orange" for x in fruits] # expression with a condition
del(thislist[2])
thislist.sort()                                # for string list sort alpha numerically
print(thislist)
thislist.sort(reverse=True)                    # Sort in reverse order
print(thislist)
## We can customize sort function
def myfunc(n):                                 # Custom sort function taking a key
    return abs(n - 50)                         # Return a key based on logic
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)                    # Send the fuction as sort key
print(thislist)
## Case sensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Case insensitive sort
thislist.sort(key = str.lower)                  # Change the sorting key to lower case
print(thislist)
thislist.reverse()                              # Just reverse a list
print(thislist)

## List copy
newlist = thislist                              # both list same
newList2 = thislist.copy()                      # new list is different
mewList3 = list(thislist)                       # Another way to copy a List
print(newList2)

## Jon two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2                           # Simply add two lists
for x in list2:                                 # Use for loop and append all elements
    list1.append(x)
list1.extend(list2)                             # Use extend to add list2

## Tuple (ordered, allow duplicates and unchangeable)
thistuple = ("apple", "banana", "cherry")
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
print(thistuple)
print(thistuple[-1])
print(thistuple[1:2])
print(thistuple[:2])
if "apple" in thistuple:
    print ("Apple found")
# To modify tuple -> Create list from tuple -> modify list -> create and assign tuple from list
thistuple = thistuple + ("Orange",)      #Tuple have comma
print(thistuple)
# To delete tuple -> Create list from tuple -> modify list -> create and assign tuple from list
del thistuple                              # Delete this tuple completely
thistuple = ("apple", "banana", "cherry")  # Packing tuple
(x,*y) = thistuple                         # Unpacking Tuple# use asterisk to collect other values
print(x)
print(y)
# Loop through tuple in same way as list
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2                    # Join Tuple
tuple2 = tuple1 * 2                         # Multiply Tuple
print (tuple2)
print(tuple2.count("a"))                    # Count method
print(tuple2.index("b"))                    # index method

# Sets
# Unordered, Unchanged, Unindexed
thisset = {"apple", "banana", "cherry", "apple"}
thisset = {"apple", "banana", "cherry", True, 1, 2}     # True and 1 are same
thisset = {"apple", "banana", "cherry", False, True, 0} # Falso and 0 are same
print(thisset)
print(len(thisset))
print(type(thisset))
thisset = set(("apple", "banana", "cherry", "apple"))
for x in thisset:
    print(x)
thisset.add("orange")
thisset2= set(("Pineapple",))
thisset.update(thisset2)                        # Add items from another set to current set
thisset.update(thislist)                        # Can add a list as well
thisset.remove("apple")                         # Delete item that exist otherwise error
thisset.discard("banana")                       # Delete item does not exist - no error
x = thisset.pop()                               # Remove a random item
thisset.clear()                                 # Empties the set
#del thisset                                     # Deleted the set
# union() update() joins two sets
# intersection()  keeps only duplicates
# difference() keeps items of fist excluding 2nd
# symmetric_difference() all items EXCEPT the duplicates
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3}
set3 = set1.union(set2)                          # union
set3 = set1 | set2                               # union
set3 = set1.union(set2,thisset2)             # can give a comma seperated lists or set1 | set2 | set3 etc.
# set1.update(set2)                              # same as union
set3 = set1.intersection(set2)                   # Intersection
set3 = set1 & set2                               # intersection
set3 = set1.difference(set2)                     # Difference
set3 = set2 - set1                              # Difference
set1.difference_update(set2)                     # Difference update returns the same set excluding common items
set1 = {"a", "b", "c", 1}
set2 = {1, 2, 3}
set3 = set1.symmetric_difference(set2)           # Symmetric difference (discards the common items and keeps both)
set3  = set1 ^ set2
set1.symmetric_difference_update(set2)           # same but result is in set1
print(set1)
# List: Ordered, changeable, duplicate
# Tuple: Ordered, unchangeable, duplicate
# Set: unordered, unchangeabe, not indexed, no duplicate
#Dictionaries: Ordered, changable, no duplicate
thisdict = {                                    # Define Dictionary
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "engine": ["oil","electric"]         # Can have other data types
}
thisdict2 = dict(name="john", age = 36, country = "Norway")
thisdict["color"] = ["red", "purple", "blue"]   # Can add more items
print(thisdict2)
print(thisdict["color"])                        # Access Dictionary items
print(thisdict.get("color"))                    # Same effect
print(len(thisdict))                            # Length of Dictionary
print(thisdict.keys())                         # Print dictionary keys # Adding more key will automatically add it
print(thisdict.values())                       # Print dictionary values # Changing thisdict.values() will change values
print(thisdict.items())                        # Returns a list view of items
if "model" in thisdict:                        # Check if a key exists
    thisdict["year"] =2010                     # Change dictionary values
    thisdict.update({"year": 2020})             # Same effect
    print(thisdict["year"])
    print("model found")
# remove an item
thisdict.pop("model")
print(thisdict)
# remove last item
thisdict.popitem()
print(thisdict)
#remove specified item
del thisdict["brand"]
print(thisdict)
# Clear dictionary
thisdict.clear()
print(thisdict)
# Delete Dictionary
del thisdict
# While looping through the dictionary return values are the keys
for x in thisdict2:                 # Can loop through thisdict.values() or thisdict.keys()
    print(thisdict2[x])
# loop through both key values using items
for x, y in thisdict2.items():
    print(x, y)
# Copy a dictionary
thisdict = dict(thisdict2)
thisdict = thisdict2.copy()

# Dictionary of dictionaries
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily["child1"]["name"])

# Loop through nested dictionaries
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
# If condition:
if 2>3:
    print("2>3")
elif 2==3:
    print("2 is equal to 3")
else:
    print("2 less than 3")
# shorthand if else
if 2>3: print(3)
print(2) if 2>3 else print(3)
print(2) if 2 > 3 else print("=") if 2 == 3 else print("3")
# and or not
if 2>3 and 2!=3: print(3)
if not 2>3:
    print(3)
if 2>3:
    pass                            # Leave the if statement empty

# While loop
i = 1
while i < 6:
    print(i)
    i+=1
    #if i ==3:               # Break conditions
    #    break
else:                        # Do something when loop condition is false
    print("loop complete")

# For loop
for x in range(1,7,2):       # start, end, increment
    if x==2:
    #    break
        continue  #Skip loop for this condition
    print (x)
else:
    print("loop done!")

# Functions
def my_function(arg):                  # Pass a list of arguments
    # def my_function(arg, /) will not allow argument as arg = 5
    #
    print(arg)
my_function(5)
my_function(arg = 55)
def my_function2(*arg):                 # Pass a list of arguments
    print(arg)
my_function2(5,5,6,6,7,8,9)

def my_function3(**args):               #Pass a dictionary of arguments
    print(args["fname"])
my_function3(fname="Dip", lname="Das")

def my_country(country = "Bangladesh"): # Supply a default parameter value
    print(country)
    return 0
my_country()
my_country("USA")

# Positional and keyword argument
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)