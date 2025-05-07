from collections import deque

def rotate_queue(n, targets):
    dq = deque(range(1, n + 1))
    count = 0

    for target in targets:
        # 목표 숫자의 인덱스 찾기
        idx = dq.index(target)

        # 왼쪽 회전이 더 빠르면 왼쪽 회전
        if idx <= len(dq) // 2:
            while dq[0] != target:
                dq.append(dq.popleft())  # 왼쪽으로 회전
                count += 1
        # 오른쪽 회전이 더 빠르면 오른쪽 회전
        else:
            while dq[0] != target:
                dq.appendleft(dq.pop())  # 오른쪽으로 회전
                count += 1

        dq.popleft()  # 맨 앞 원소 제거

    return count

n, m = map(int, input().split())
targets = list(map(int, input().split()))
print(rotate_queue(n, targets))
