def sieve_of_eratosthenes(n:int) -> list[bool] | list[int]:
    if n < 2:
        return []
    is_prime = [False,False] + [True] * (n-1)
    for i in range(4,n + 1,2):
        is_prime[i] = False
    p = 3

    while (p*p) <= n:
        if is_prime[p]:
            pp = p * p
            while pp <= n:
                is_prime[pp] = False
                pp += 2 * p
        p += 2



    return  is_prime
def main() -> None:
    #print(sieve_of_eratosthenes(100))
    c = 0
    sieve_list = sieve_of_eratosthenes(100)
    for m in sieve_list:
        print(c,":", m)
        c = c + 1
if __name__ == "__main__":
    main()



