def get_int(message: str) -> int:
    return int(input(f"{message}: \n"))

def is_even(n: int) -> bool:
    return n % 2 == 0


def main() -> None:
    n = get_int('podaj liczbe')
    print('Liczba parzysta' if is_even(n) else "Nie parzysta")

if __name__ == "__main__":
    main()
