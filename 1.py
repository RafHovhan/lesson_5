def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b - 1)

A = int(input())
B = int(input())

result = f(A, B)
print(result)