# YAAA
def summator(number):
    x=[]
    for el in str(number):
        x.append(int(el))
        q = sum(x)
        if len(str(q))>1:
            x=[]
            x.append(q)
            return summator(q)
    print(sum(x))
# summator(input())
# VOVA
def add_digits(number):
    final=0
    for n in str(number):
        final += int(n)
    if len(str(final))>1:
        return add_digits(final)
    return print(final)
add_digits(input())