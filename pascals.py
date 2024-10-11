def fact(n):
    if n == 0 or n == 1:
        return 1
    num = n
    for i in range(n-1, 0, -1):
        num *= i
    return num

def choose(a, b):
    top = fact(a)
    den = fact(b) * fact(a - b)
    return top // den

def row(n):
    for i in range(n + 1):
        print(choose(n, i), end=' ')
    print()

def main():
    n = int(input("(n-1)st row:"))        #input n-1
    row(n+1)                              #outputs coefficients of nth row

if __name__ == "__main__":
    main()
