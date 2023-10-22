def cumulative_sum(arr):
    if not arr: return []
    result = [arr[0]]
    for i in range(1, len(arr)): result.append(result[-1] + arr[i])
    return result