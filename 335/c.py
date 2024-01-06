# n, q = map(int, input().split())
# d = []
# for _ in range(q):
#     t, w = input().split()
#     t = int(t)
#     if t == 1: d.append(w)
#     if t == 2:
#         w = int(w)
#         l = len(d)
#         if w > l: print(w - l, 0)
#         else:
#             vec = [1, 0]
#             for i in range(l - w + 1):
#                 if d[i] == 'R': vec[0] += 1
#                 if d[i] == 'L': vec[0] -= 1
#                 if d[i] == 'U': vec[1] += 1
#                 if d[i] == 'D': vec[1] -= 1
#             print(*vec)
            
N, Q = map(int, input().split())
A = [(i + 1, 0) for i in range(N)][::-1]
for _ in range(Q):
    T, C = input().split()
    if T == "1":
        x, y = A[-1]
        if C == "U": y+=1
        if C == "D": y-=1
        if C == "R": x+=1
        if C == "L": x-=1
        A.append((x,y))
    else:
        print(*A[-int(C)])
