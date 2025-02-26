def get_prime_factors(n) -> list[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i*i <= n:
        while n % i ==0:
            factors.append(i)
            n //= i
        i +=2

    if n > 2:
        factors.append(int(n))
    return  factors
def main() -> None:
    print(get_prime_factors(25))
    print(get_prime_factors(105))
    print(get_prime_factors(100))
    print(get_prime_factors(64))
if __name__=='__main__':
    main()