L = int(input())  # 문자열 길이
s = input()       # 문자열

r = 31
M = 1234567891

hash_value = 0
power_of_r = 1  # r^0 부터 시작

for i in range(L):
    # a_i: 알파벳의 숫자값 (a = 1, ..., z = 26)
    a_i = ord(s[i]) - ord('a') + 1
    
    # H += a_i * r^i
    hash_value += a_i * power_of_r
    
    # 다음 항을 위해 r^i 값을 r^(i+1)로 갱신
    power_of_r = (power_of_r * r) % M

print(hash_value % M)