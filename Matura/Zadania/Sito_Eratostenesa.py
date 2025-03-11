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
def prime(*numbers:int):
    sieve_list = sieve_of_eratosthenes(max(numbers))
    prime_numbers = []
    for number in numbers:
        if sieve_list[number]:
            prime_numbers += [True]
        else:
            prime_numbers += [False]
    return numbers,prime_numbers

def main() -> None:
    num,num_bool = prime(5,10,100,2,1,15)
    for m in range(len(num)):
        print(num[m],":",num_bool[m])

if __name__ == "__main__":
    main()



