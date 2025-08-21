num = [1,2,3,4,5]

res = 7

for i in num:
    for j in num:
        if i+j == res:
            print(i,j)
        elif j==1:
            break