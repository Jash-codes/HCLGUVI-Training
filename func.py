def sum(*a, b):
    print("Positional args:", a)
    print("positional arg b:", b)

sum(1, 2, 3, b="hello")

print(sum.__dict__)

# we can use zip too 
# print(zip(a[0],a[1]))
