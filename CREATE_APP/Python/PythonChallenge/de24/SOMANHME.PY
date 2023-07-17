import math

def nguyen_to(n):
    if n< 2 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
primes = []

def manh_me(num):
    for prime in primes:
        if num% prime == 0 and num % ( prime **2) != 0:
            return False
    return True

def get_primes(n):
    primes = []
    for num in range(2, n+1):
        if nguyen_to(num):
            primes.append(num)
    return primes

a = 0 
numbers = 10
for num in range(2, 40):
    if manh_me(num):
        print(num, end = ' ')
        if a % numbers == 0:
            print()
    