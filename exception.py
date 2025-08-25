try:
    rank = -2
    if(rank<1):
        raise TypeError("it must be greater than 1")
except ZeroDivisionError:
    print("0000")

finally:
    print("Process done")












