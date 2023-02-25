# Factorial


def factorial(num):
    assert num >= 0 and int(num) == num
    if num in [1,0]:
        return 1
    else:
        return num * factorial(num-1)

factorial(1) # 1
factorial(2) # 2
factorial(4) # 24
factorial(7) # 5040