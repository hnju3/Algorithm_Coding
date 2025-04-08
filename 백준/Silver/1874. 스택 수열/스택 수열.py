n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for num in sequence:
    # push 필요한 경우
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1

    # 원하는 수가 스택 맨 위에 있으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        # 수열을 만들 수 없음
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print("NO")
