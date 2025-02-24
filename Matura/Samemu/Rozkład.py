
def get_in_number(message: str) -> int:
    number = int(input(f"{message}: "))
    return number
def get_in_position(message: str) -> int:
    position = int(input(f"{message}: "))
    return position
def digit_at_position(number: int,position: int) -> int:
    return abs(number)//10 ** (position - 1) % 10
def main() -> None:
    n = get_in_number('Podaj numer')
    p = get_in_position('Podaj pozycje')
    d = digit_at_position(n,p)
    print(d)
    return
if __name__ == '__main__':
    main()