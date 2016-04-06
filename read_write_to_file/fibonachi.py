


fib = lambda x: fib(x-1)+fib(x-2) if x>2 else 1
print(fib(1))

# factorial = lambda x: x and factorial(x-1)* x or 1

# def fib(x):
#     if(x > 2):
#         return fib(x - 1)+fib(x-2)
#     else:
#         return 1
#
# print(fib(6))
#
#
# def fib(n):
#     a=0
#     b=1
#     for _ in range(n):
#         a,b = b, a+b
#     return a
#
# !!!!!!!!!!!!!!!!!!
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, b + a

print (list(fib(100)))