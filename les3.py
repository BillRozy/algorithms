def fib_mod(n, m):
    return period(m)


def fib(n):
    mem = [0, 1]
    i = 2
    while i < n:
        mem = [mem[1], sum(mem)]
        i += 1
    return sum(mem)


def period(m):
    fiba = [0, 1]
    periods = []
    potential_period = [1] 
    zone = {1, 2, 4}
    found_first = False
    found_last = False
    first_zero_at = 0
    zeros = 0
    i = 2
    while True:
        if found_first and found_last:
            break
        num = fiba[i - 2] + fiba[i - 1]
        mod = num % m
        fiba.append(num)
        potential_period.append(mod)
        i += 1
        print(fiba)
        print(per)
        if mod == 0:
            if not found_first:
                found_first = True
                first_zero_at = i
            if not found_last:
                periods.append(potential_period)
                potential_period = []
        else:
            
            found_last = True

    return [first_zero_at, zeros]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()