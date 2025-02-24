# Rozklad liczby na cyfry
def digit_at_position(number: int, position: int) -> int:
    if position < 0:
        return -1
    else:
        return (abs(number) // 10 ** position) % 10

def digit_at_position_str(number: int, position: int) -> int:
    number_str = str(abs(number))
    if position < 0 or position  >= len(number_str):
        return -1
    return int(number_str[-1 - position])

def main() -> None:

    return

if __name__ == "__main__":
    main()