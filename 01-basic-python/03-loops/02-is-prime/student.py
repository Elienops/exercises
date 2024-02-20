# Write your code here

def is_prime(n):
    for k in range(0, n):
        if n % k == 0:
            return False
    return True