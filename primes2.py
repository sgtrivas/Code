try:
    num = int(input("Enter a number to calculate: "))
    if num < 2:
        raise 
except:
    print("number is less than two")
else:
    t = 0
    def is_prime(n):
        for i in range(2,n):
            if n % i == 0:
                return i
    
    print(f'the prime values for {num} are:')
    for n in range(2,num):
        if is_prime(n):
            if n==num:
                print(n)
        else:
            t = t+n
            print(n)
    print(f"the sum of all the primes of {num} is {t}"),",",
    
