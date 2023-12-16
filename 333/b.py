S = list(input())
T = list(input())

def length(v1, v2):
    l = abs(ord(v1) - ord(v2))
    return l if l <= 2 else (2 if l == 3 else 1)

print("Yes" if length(S[0], S[1]) == length(T[0], T[1]) else "No")