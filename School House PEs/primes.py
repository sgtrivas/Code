def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status
num = int(input("Enter a number to calculate: "))
t = 0
print(f'the prime values for {num} are:')
for n in range(1,num):
    if is_prime(n):
        if n==num:
            print(n)
        else:
            t = t+n
            print(n)
print(f"the sum of all the primes of {num} is {t}"),",",
