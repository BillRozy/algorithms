def fib(n):
    mem = [0, 1]
    i = 2
    while i < n:
        mem = [mem[1] % 10, sum(mem) % 10]
        i += 1
    return sum(mem) % 10

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()