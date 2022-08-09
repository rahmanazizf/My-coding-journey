def prime_finder(num):
    i = 0
    primes = []
    while num > 1:
        print([num%a for a in range(1, num+1)].count())

print(prime_finder(11))
