n = int(input("This program calculates the nth fibonacci number using recursion. Press Enter to continue."))
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n))