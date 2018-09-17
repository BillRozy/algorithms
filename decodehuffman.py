def decode_string(string, codes):
    inv_codes = {v: k for k, v in codes.items()}
    res = ''
    i = 0
    while i < len(string):
        j = i + 1
        while j <= len(string):
            code = ''.join(string[i:j])
            liter = inv_codes.get(code)
            if liter:
                res += liter
                i = j - 1
                break
            j += 1
        i += 1
    return res


uniques, size = map(lambda x: int(x), input().split(' '))
codes = {}
for i in range(0, uniques):
    liter, code = input().split(': ')
    codes[liter] = code
encoded = input()

print(decode_string(encoded, codes))
