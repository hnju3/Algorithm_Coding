import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
A = set(map(int, data[1:N+1]))

M = int(data[N+1])
queries = map(int, data[N+2:N+2+M])  # 찾고자 하는 값들

# 존재 여부 확인
for q in queries:
    print(1 if q in A else 0)