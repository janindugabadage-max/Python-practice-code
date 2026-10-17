a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
print(a is c)
print(a is b)
print(a is not b)

x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.5
if (type(x) is not float):
    print("true")
else:
    print("false")
    
