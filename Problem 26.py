def main():
    result = 0
    size = 0
    for i in range(1, 1001):
        current_size = get_recurring_cycle_size(1, i)
        if current_size > size:
            size = current_size
            result = i
    print(result)


def get_recurring_cycle_size(dividend, divisor):
    """Returns the size of the recurring cycle"""
    remainders = {}
    position = 0
    if dividend < divisor:
        dividend *= 10
    remainder = dividend % divisor
    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        next_dividend = remainder * 10
        remainder = next_dividend % divisor
        position += 1
    
    return 0


if __name__ == "__main__":
    main()