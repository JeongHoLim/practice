
n = int(input())
fibs = dict()
def fib(n):
    if n not in fibs:
        if n <= 1:
            fibs[n] = n
            return n
        else:
            fibs[n-1],fibs[n-2] = fib(n-1),fib(n-2)
            fibs[n] = fibs[n-1] + fibs[n-2]
            return fibs[n]
    else:
        return fibs[n]

print(fib(n))