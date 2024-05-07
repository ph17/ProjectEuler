import math


def main():
    primes = []
    prime_number = next_prime(1)
    number = 600851475143
    while number != 1:
        if number % prime_number == 0:
            primes.append(prime_number)
            number /= prime_number
        prime_number = next_prime(prime_number)
    print(max(primes))


def next_prime(number):
    """Returns the very next prime after the number argument"""
    i = number + 1
    while not is_prime(i):
        i += 1
    return i


def is_prime(number):
    """Returns if a number is prime or not"""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    square_of_number = math.sqrt(number)
    for i in range(3, int(square_of_number) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
