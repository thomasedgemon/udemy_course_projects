
def prime_checker(number):
    is_prime = True
    range_1 = range(2, number)
    for i in range_1:
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime number.")
    else:
        print("it's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)