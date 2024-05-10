import math


def main():
    numbers = list(range(1, 20))
    print(get_lcm(numbers))


def get_lcm(numbers_list):
    """Returns the Least Common Multiple (LCM) of the list of numbers"""
    primes = []
    i = 2
    while not is_all_one(numbers_list):
        if divide_numbers_by_prime(i, numbers_list, primes):
            continue
        i = next_prime(i)
    return math.prod(primes)


def is_all_one(numbers_list):
    counter = 0
    for value in numbers_list:
        if value == 1:
            counter += 1
    if counter == len(numbers_list):
        return True
    else:
        return False


def divide_numbers_by_prime(p, numbers_list, primes):
    """
    Divides numbers in the list by the given prime if they are divisible.

    Args:
        p (int): The prime number to divide the list of numbers by.
        numbers_list (list): The list of numbers to be divided.
        primes (list): The list to which the prime will be appended if it divides any number.

    Returns:
        bool: True if any number in the list is divisible by the prime, False otherwise.
    """
    keep_dividing = False  # checks if current prime can divide any number of the array
    for index in range(0, len(numbers_list)):
        if numbers_list[index] % p == 0:
            numbers_list[index] = numbers_list[index] / p
            keep_dividing = True
    if keep_dividing:
        primes.append(p)
    return keep_dividing


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
