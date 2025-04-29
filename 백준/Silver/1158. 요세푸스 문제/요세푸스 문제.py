def josephus(n, k):
    p = [i for i in range(1, n+1)]
    result = []
    
    idx = 0
    
    for _ in range(n):
        idx += k - 1
        idx %= len(p)
        result.append(p.pop(idx))
    return result

n, k = map(int, input().split())
result = josephus(n, k)

print("<" + ", ".join(map(str, result)) + ">")