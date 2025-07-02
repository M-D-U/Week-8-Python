'''
name = "Lauren"

def greet(name):
    print(f"Hello {name}")
    
greet(name)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")

greet("Bob","Good Morning")