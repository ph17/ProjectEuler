def main():
    print(abs(do_faulhaber_formula(100) - pow(do_gauss_formula(100), 2)))


def do_gauss_formula(n):
    """
    Calculate the sum of the first n natural numbers using Gauss's formula.

    Parameters:
    n (int): The number of natural numbers to sum.

    Returns:
    int: The sum of the first n natural numbers.

    """
    return (n * (n + 1)) / 2


def do_faulhaber_formula(n):
    """
    Calculate the sum of the squares of the first n natural numbers using Faulhaber's formula.

    Parameters:
    n (int): The number of natural numbers whose squares are to be summed.

    Returns:
    int: The sum of the squares of the first n natural numbers.

    """
    return (n * ((n + 1) * (2 * n + 1))) / 6


if __name__ == "__main__":
    main()
