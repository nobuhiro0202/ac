N = int(input())

def f(num):
    return 0 if num == 1 else f(num // 2) + f(num - (num // 2)) + num

print(f(N))
