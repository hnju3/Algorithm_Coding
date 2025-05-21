import sys
sys.setrecursionlimit(100000)  
input = sys.stdin.readline

preorder = []
while True:
    line = input()
    if not line:
        break
    preorder.append(int(line.strip()))

result = []


def build_postorder(start, end):
    if start >= end:
        return

    root = preorder[start]
    idx = start + 1

    # 왼쪽 서브트리 끝 찾기
    while idx < end and preorder[idx] < root:
        idx += 1

    # 왼쪽 서브트리 처리
    build_postorder(start + 1, idx)
    # 오른쪽 서브트리 처리
    build_postorder(idx, end)
    # 루트 처리 (후위 순회)
    result.append(root)

build_postorder(0, len(preorder))

print('\n'.join(map(str, result)))
