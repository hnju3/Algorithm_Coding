import sys
input = sys.stdin.readline

K = int(input())

nodes = list(map(int, input().split()))

# 각 레벨별로 노드를 저장할 리스트
levels = [[] for _ in range(K)]

def build_tree(start, end, level):
    if start > end:
        return
    
    # 현재 부분의 중간이 루트
    mid = (start + end) // 2

    # 현재 레벨에 루트 노드 저장
    levels[level].append(nodes[mid])
    
    # 왼쪽 서브트리
    build_tree(start, mid - 1, level + 1)
    # 오른쪽 서브트리
    build_tree(mid + 1, end, level + 1)

build_tree(0, len(nodes) - 1, 0)

for level in levels:
    print(' '.join(map(str, level)))
