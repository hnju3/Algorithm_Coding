import sys
from collections import deque

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# deque를 사용하여 큐를 생성
queue = deque()

# 출력 결과를 모아서 한 번에 출력할 리스트
output = []

# 명령의 개수 입력 받기
n = int(input())

# n개의 명령을 처리
for _ in range(n):
    # 한 줄 명령 입력 받고 공백 제거
    command = input().strip()

    # 명령이 push로 시작하면 정수 X를 큐에 추가
    if command.startswith("push"):
        _, value = command.split()
        queue.append(int(value))
    
    # pop 명령: 큐에서 앞의 원소를 제거하고 출력, 비었으면 -1
    elif command == "pop":
        output.append(f"{queue.popleft() if queue else -1}")
    
    # size 명령: 큐에 들어있는 원소의 개수 출력
    elif command == "size":
        output.append(f"{len(queue)}")
    
    # empty 명령: 큐가 비어있으면 1, 아니면 0 출력
    elif command == "empty":
        output.append(f"{1 if not queue else 0}")
    
    # front 명령: 큐의 맨 앞 원소 출력, 없으면 -1
    elif command == "front":
        output.append(f"{queue[0] if queue else -1}")
    
    # back 명령: 큐의 맨 뒤 원소 출력, 없으면 -1
    elif command == "back":
        output.append(f"{queue[-1] if queue else -1}")

# 모든 출력 결과를 한 번에 출력 (속도 향상을 위해)
sys.stdout.write("\n".join(output) + "\n")
