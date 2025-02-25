def divisor_sum(n) -> int:
    if n == 1: return 1
    count,i = 2,2
    while i*i< n:
        if n%i==0:
            count +=2
        i+=1
    if i*i==n: #np 6 ->36 6^2 -> 36 6 jest liczone raz
        count+=1
    return count
def divisor_sum2(n) -> list[int]:
    if n == 1: return [1]
    divisors = [1,n]
    i = 2
    while i*i< n:
        if n%i==0:
           divisors.extend([i, n // i])
        i+=1
    if i*i==n: #np 6 ->36 6^2 -> 36 6 jest liczone raz
        divisors.append(i)
    return sorted(divisors)



def main() -> None:
    print(divisor_sum2(6))
    return
if __name__=='__main__':
    main()