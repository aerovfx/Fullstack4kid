t = int(input())

for _ in range(t):
    n = int(input())
    
    # Find the largest power of 2 that divides n
    power_of_two = 0
    while n % 2 == 0:
        n //= 2
        power_of_two += 1
    
    # If n is a power of 2, output 0 as a and n as b
    if n == 1:
        print(0)
    else:
        # Find the smallest prime factor of n (excluding 2)
        smallest_prime_factor = 3
        while smallest_prime_factor * smallest_prime_factor <= n:
            if n % smallest_prime_factor == 0:
                break
            smallest_prime_factor += 2
        
        # If n is prime, output 1 as a and n as b
        if n == smallest_prime_factor:
            print(1)
        else:
            # Output 2 as a and (n//2) as b
            print(2)
