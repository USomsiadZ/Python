import Sito_Eratostenesa

def find_twin_primes(n: int) -> list[tuple[int,int]]:
    count = 1
    twin_primes = [(3, 5)]
    number = 5
    while count < n:
        prime = Sito_Eratostenesa.prime(number, number+2)
        a,b = prime[0],prime[1]
        if b[0] and b[1]:
            twin_primes.append((number, number+2))
            count += 1
        number += 6
    return twin_primes

def main() -> None:
    result = find_twin_primes(10)
    print(result)
    return

if __name__ == "__main__":
    main()
