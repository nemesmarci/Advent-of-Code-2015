with open('input.txt') as data:
    tokens = data.read().split()

x = int(tokens[tokens.index('row') + 1].replace(',', ''))
y = int(tokens[tokens.index('column') + 1].replace('.', ''))

code, base, mod = 20151125, 252533, 33554393

print(code * pow(base, ((x + y) ** 2 - 3 * x - y + 2) // 2 - 1, mod) % mod)
