def euclid_algorithm(a,b):
    while a != 0 and    b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a,b

def main() -> None:
    print(euclid_algorithm(25,225))
    return
if __name__ == '__main__':
    main()