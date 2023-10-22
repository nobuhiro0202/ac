from bisect import bisect_right
N, Q = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
def cumulative_sum(arr):
    if not arr: return []
    result = [arr[0]]
    for i in range(1, len(arr)): result.append(result[-1] + arr[i])
    return result

s = cumulative_sum(R)

for _ in range(Q):
    x = int(input())
    print(bisect_right(s, x))