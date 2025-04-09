def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = []

    for ch in expression:
        if ch.isalpha():  # 피연산자면 바로 출력
            result.append(ch)
        elif ch == '(':  # 여는 괄호는 push
            stack.append(ch)
        elif ch == ')':  # 닫는 괄호는 ( 나올 때까지 pop
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 여는 괄호는 제거만
        else:  # 연산자
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[ch]:
                result.append(stack.pop())
            stack.append(ch)

    while stack:  # 남은 연산자 출력
        result.append(stack.pop())

    return ''.join(result)

expression = input().strip()
print(infix_to_postfix(expression))
