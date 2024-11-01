def fibonacci_Generator():
    a=0
    b=1
    while(True):
        yield b
        a,b= b,a+b
 
obj = fibonacci_Generator()
  
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
