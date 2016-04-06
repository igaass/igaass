def missing_number(num_list):
    missing = set(num_list)^set(range(1,101))
    print(missing)
a = range(1,98)
missing_number(a)

# b=[1,2,3,4,5,6,7,8,9]
# c = set(b)^set(a)
