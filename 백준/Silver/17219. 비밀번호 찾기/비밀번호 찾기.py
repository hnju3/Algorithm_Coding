import sys

input = sys.stdin.readline

# N: 저장된 사이트 수, M: 찾으려는 사이트 수
N, M = map(int, input().split())

# 딕셔너리 이용
password_dict = {}

for _ in range(N):
    site, password = input().split()
    password_dict[site] = password.strip()

results = []

for _ in range(M):
    query = input().strip()
    results.append(password_dict[query])

print('\n'.join(results))
