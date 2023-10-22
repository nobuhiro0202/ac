N, A, B = map(int, input().split())
D = list(map(int, input().split()))

C = A + B
D = [d % C for d in D]
D = sorted(set(D))

ans = 'No'
p = D[-1] - D[0]
if p < A: ans = 'Yes'

print(ans)