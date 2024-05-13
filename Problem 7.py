import math


def main():
    prime = 0
    for _ in range(1, 10002):
        prime = next_prime(prime)
    print(prime)


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
