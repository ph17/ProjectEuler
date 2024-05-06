def main():
    print(sum(get_diagonal_numbers(1001)))


def get_diagonal_numbers(size):
    """Returns the list of diagonal numbers from any size grid that follows the pattern described by the question"""
    diagonal_numbers = []
    number = 1
    step = 2
    counter = 0
    while number <= (size * size):
        if counter == 4:
            step += 2
            counter = 0
        diagonal_numbers.append(number)
        number += step
        counter += 1
    return diagonal_numbers


if __name__ == "__main__":
    main()
