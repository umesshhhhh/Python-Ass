n = int(input("Enter how many prime numbers you want: "))
primes = []
num = 2
while len(primes) < n:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print("First", n, "prime numbers:", primes)
