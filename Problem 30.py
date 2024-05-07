def main():
    numbers = []
    for i in range(10, 354295):
        if i == get_sum_of_fifth_powers_of_digits(i):
            numbers.append(i)
    print(sum(numbers))


def get_sum_of_fifth_powers_of_digits(number):
    """Returns the sum of fifth powers of the digits of the number argument"""
    result = 0
    number_string = str(number)
    for digit in number_string:
        result += pow(int(digit), 5)
    return result


if __name__ == "__main__":
    main()
