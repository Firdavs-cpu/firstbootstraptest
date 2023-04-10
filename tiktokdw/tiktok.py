x = [1,2,3]

def foo(x):
    a = 42 
    x[1]= a
    x = a

foo(x)
print(x)