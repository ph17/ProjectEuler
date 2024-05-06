def main():
    numbers_set = set()
    for a in range(2, 101):
        for b in range(2, 101):
            numbers_set.add(pow(a, b))
    print(len(numbers_set))


if __name__ == "__main__":
    main()
