def magic(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
    
@magic    
def print_hello():
    print("hello")
print_hello()