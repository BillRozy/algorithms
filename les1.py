def fib(n):
    mem = [0, 1]
    i = 2
    while i < n:
        mem = [mem[1], sum(mem)]
        i += 1
    return sum(mem)

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()