
try:
    print("Dip")
    #raise TypeError("Not this name")
except TypeError:
    print(TypeError)
except:
    print("Other error")
else:
    print("No error")
finally:
    print("finally!!")

x= input("A integer: ")
print(x)