def divisible(x,y):
    return x % y == 0

def divisibles(x):
    return [y for y in range(1, x) if divisible(x, y)]

def esPrimo(n):
    return len(divisibles(n)) <= 2

def primos(n):
    return [x for x in range(1, n) if esPrimo(x)]

if __name__ == '__main__':
    print(primos(100))