def euclid_gcd(n1, n2):
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
    import sys

    n1, n2 = sys.argv[1:]
    gcd = euclid_gcd(n1, n2)
