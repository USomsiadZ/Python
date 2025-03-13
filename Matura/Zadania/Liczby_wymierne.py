import Algorytm_Euklidesa_odejmowanie
def gcd(number1:int,number2:int) -> int:
    euclid = Algorytm_Euklidesa_odejmowanie.euclid_algorithm(number1,number2)
    return euclid
def lcm(number1:int,number2:int)-> int:
    c = abs(number1 * number2) // gcd(number1, number2)
    return c
def simplify_fraction(numerator:int,denominator:int) -> tuple[int,int]:
    a = gcd(numerator, denominator)
    numerator //= a
    denominator //= a
    return numerator,denominator
def add_fractions(number1:list,number2:list) -> tuple[int, int]:
    l1,l2 = number1[0],number2[0]
    m1,m2 = number1[1],number2[1]
    nww = lcm(m1,m2)
    fraction = (nww // m1 * l1) + (nww // m2 * l2)
    return simplify_fraction(fraction,nww)
def main() -> None:
    print(add_fractions([3,4],[1,6]))
    print(add_fractions([3,12],[1,12]))
if __name__ == '__main__':
    main()
