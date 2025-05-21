import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

vertices = [[] for _ in range(N+1)]

# 부모 노드를 저장할 리스트
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

q = deque()
q.append(1)       # 루트 노드는 1번
parent[1] = -1    # 1번 노드는 부모가 없음

while q:
    current = q.popleft()
    for v in vertices[current]:
        if parent[v] == 0:     # 아직 부모가 정해지지 않은 노드라면
            parent[v] = current
            q.append(v)

print('\n'.join(map(str, parent[2:])))