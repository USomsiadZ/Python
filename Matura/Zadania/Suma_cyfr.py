def get_number_input(message: str) -> int:
    return abs(int(input(message)))
def digit_sum(number) -> int:
    s = 0
    while number > 0:
        s += number % 10
        number //= 10
    return s
def main() -> None:
    num = get_number_input('Podaj liczbe')
    result = digit_sum(num)
    print(result)
if __name__ == '__main__':
    main()





