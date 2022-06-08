def euclid_gcd(n1, n2):
    if not (isinstance(n1, int) and isinstance(n2, int)):
        raise TypeError("Arguments must be ints")

    if n1 > n2:
        a, b = n1, n2
    else:
        a, b = n2, n1

    while (b != 0):
        old_b = b
        b = a % b
        a = old_b

    return a


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("n1", help="Primeiro número", type=int)
    parser.add_argument("n2", help="Segundo número", type=int)
    args = parser.parse_args()
    gcd = euclid_gcd(args.n1, args.n2)
    print(f"O maior divisor entre {args.n1} e {args.n2} é: {gcd}")
