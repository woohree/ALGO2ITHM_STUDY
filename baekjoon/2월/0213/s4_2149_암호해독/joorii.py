from pprint import pprint
import sys
sys.stdin = open('input.txt')

key = input()

input_text = list(map(str, input()))

y = len(input_text) // len(key)

# 암호문, 평문 리스트 초기화
encrypted_text = [[0] * len(key) for _ in range(y)]
plain_text = [[0] * len(key) for _ in range(y)]

# 암호문 배열 형태로 정렬
for i in range(len(key)):
    for j in range(y):
        encrypted_text[j][i] = input_text[(i * y) + j]

# key 순서에 맞추어 암호문 열 변경
# 알파벳 순서 비교하기 위해 ord
ord_key = list(ord(char) for char in key)

# 검색 여부를 저장하기 위한 변수 리스트
temp = [0] * len(key)

for i in range(len(key)):
    # 이미 검색한 가장 작은 수가 아닌 수로 min_val, min_idx 초기화
    for k in range(len(key)):
        if temp[k] == 0:
            min_val = ord_key[k]
            min_idx = k
            break

    # key에서 우선 알파벳 고르기
    for j in range(len(key)):
        # 이미 검색했던 변수라면 넘어가기
        if temp[j] == 1:
            continue
        if min_val > ord_key[j]:
            min_val = ord_key[j]
            min_idx = j

    temp[min_idx] = 1

    # key의 알파벳 순서대로 열 바꾸기
    for r in range(y):
        plain_text[r][min_idx] = encrypted_text[r][i]

# 평문 출력하기
for i in range(len(plain_text)):
    for j in range(len(plain_text[i])):
        print(plain_text[i][j], end='')
