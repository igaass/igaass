listik = [12, 13, 12, 1,0, 1, 12, 13.2, 0.0001]
x=[]
for elem in listik:
    if type(elem) == int:
        x.append(elem)
print(min(set(x)))