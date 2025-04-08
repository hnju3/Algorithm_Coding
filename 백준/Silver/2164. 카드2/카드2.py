from collections import deque

N = int(input())
cards = deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()           # 제일 위의 카드 버림
    cards.append(cards.popleft())  # 그 다음 카드를 아래로

print(cards[0])  # 마지막에 남는 카드 출력
