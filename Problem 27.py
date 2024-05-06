import math


def main():
    possible_b_values = get_possible_b_values()  # b must be prime
    value = 0
    final_a = 0
    final_b = 0
    for b in possible_b_values:
        for a in range(-999, 1000, 2):  # a must be odd
            n = 0
            while is_prime(do_formula(n, a, b)):
                n += 1
            if n > value:
                value = n
                final_b = b
                final_a = a
    result = final_a * final_b
    print(result)


def do_formula(n, a, b):
    """Calculates the formula"""
    return pow(n, 2) + (a * n) + abs(b)


def get_possible_b_values():
    """Get the possible values of b"""
    values = []
    for i in range(3, 1001):
        if is_prime(i):
            values.append(i)
    return values


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
