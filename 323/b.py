N = int(input())
A = [list(input().split()) for _ in range(int(N))]
A_with_counts = [(s[0], s[0].count('o'), i) for i, s in enumerate(A)]
sorted_A = sorted(A_with_counts, key=lambda x: x[1], reverse=True)

f = []
for a in sorted_A: f.append(a[2] + 1)

print(' '.join(map(str, f)))
