# Write your code here

def last_digit(n):
    n = list(str(n))
    return int(n.pop())

def remove_last_digit(n):
    n = list(str(n))
    n.pop()
    return int("".join(n))

def digit_sum(n):
    x = 0
    for k in range(len(str(n))):
        x += last_digit(n)
        n = remove_last_digit(n)
    return x

print(digit_sum(123))