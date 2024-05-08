def main():
    even_values = [2]
    fibonacci = [1, 1, 2]
    while fibonacci[-1] < 4000000:
        next_value = fibonacci[-1] + fibonacci[-2]
        if next_value % 2 == 0:
            even_values.append(next_value)
        fibonacci.append(next_value)
    print(sum(even_values))


if __name__ == "__main__":
    main()
