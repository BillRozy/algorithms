def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(a % b, b) if a > b else gcd(b % a, a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()