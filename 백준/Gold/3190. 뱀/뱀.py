from collections import deque

def play_dummy(n, apples, directions):
    # 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0  # 처음 방향은 오른쪽

    board = [[0] * n for _ in range(n)]
    for x, y in apples:
        board[x-1][y-1] = 1  # 사과는 1로 표시

    snake = deque()
    snake.append((0, 0))  # 뱀의 시작 위치
    board[0][0] = 2  # 뱀의 몸통은 2로 표시

    time = 0
    x, y = 0, 0  # 뱀 머리 위치

    direction_changes = dict(directions)

    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽에 부딪히거나 자기 몸과 부딪히면 종료
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return time

        # 사과 있는 경우: 꼬리 안 움직임
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snake.appendleft((nx, ny))
        else:  # 사과 없는 경우: 꼬리 제거
            board[nx][ny] = 2
            snake.appendleft((nx, ny))
            tx, ty = snake.pop()
            board[tx][ty] = 0

        x, y = nx, ny

        # 방향 전환 시점이면 전환
        if time in direction_changes:
            if direction_changes[time] == 'L':
                direction = (direction - 1) % 4
            else:  # 'D'
                direction = (direction + 1) % 4

n = int(input())
k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]

l = int(input())
directions = []
for _ in range(l):
    x, c = input().split()
    directions.append((int(x), c))

print(play_dummy(n, apples, directions))
