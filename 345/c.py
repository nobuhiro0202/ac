s = input()
n = len(s)
cnt = [0] * 26
same = False

for char in s: cnt[ord(char) - ord('a')] += 1

ans = n * n
for i in range(26):
    ans -= cnt[i] * cnt[i]
    if cnt[i] > 1: same = True

ans //= 2
if same: ans += 1

print(ans)