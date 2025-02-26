def is_prime(number:int) -> bool:
    if number < 2:
        return False
    if number in [2,3]:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i*i <= number:
        if number %i==0 or number %(i+2) == 0:
            return False
        i += 6
    return True
def main() ->None:
    for i in range(1,201):
        print(i,is_prime(i))
    return
if __name__=='__main__':
    main()