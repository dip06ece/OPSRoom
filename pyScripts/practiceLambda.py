class myLambdaClass:
    def __init__(self, name, age):          # Constructor
        self.name =  name
        self.age = age
    def __str__(self):                     # String function
        return f"{self.name}({self.age})"
    def changeName(self, D):
        self.name =  self.name+D
        return self
    ################ Lambda practice  ##################
    # Lambda: small anonymous function, any number of argument but one expression
    # lambda arguments:expression
    x = lambda a:a+10
    print(x(5))

    y = lambda a,b,c:a+b+c
    print (y(3,5,1))

    def myfunc(n):
        return lambda a : a * n
    mydoubler = myfunc(2)
    print(mydoubler(11))
    ################ End of Lambda Practice #########
person1 = myLambdaClass("Dip", 36)   # Create class object
Y = lambda person: person.changeName(" Babu")   # Create Lambda Function (Can change " Babu" to a variable
print(Y(person1).name)                          # Call Lambda function and send object
print(person1)
del person1.age                                 # Delete a property
del person1                                     # Delete object
# use pass statement to keep a class empty

class childLamba(myLambdaClass):
    def __init__(self,fname,lname,age):
        super().__init__(fname, age)
        self.lname = lname
    #    self.fname = fname
    #    self.lname = lname
    #    self.age = age
    def __str__(self):
        return f"{self.name}{' '}{self.lname}({self.age})"

Z = childLamba ("Dip", "Das", 36)
print(Z)