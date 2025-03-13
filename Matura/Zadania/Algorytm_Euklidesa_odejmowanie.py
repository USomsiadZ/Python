def euclid_algorithm(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
def main() -> None:
    print(euclid_algorithm(225,27))
    return
if __name__ == '__main__':
    main()
