def stepen(a, n):
    if n == 0:
        return 1
    elif n >= 1:
        print(a,n)
        return stepen(a, n - 1) * a
    # else:
    #     return power(a, n // 2) ** 2

print(power(3,4))

