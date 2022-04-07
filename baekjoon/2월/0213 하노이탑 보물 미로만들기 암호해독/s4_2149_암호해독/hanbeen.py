# 백준 2149 암호해독 S4 문제
# 5:45 알고리즘 시작 -> 6:20 코드짜기 시작 ->
# 7:48 예제 출력값 나왔지만 백준에서는 런타임에러(IndexError)뜸
# 8:02 놓친거 발견
# 8:22 성공 => 총 소요시간 : 2시간 37분
import sys
sys.stdin = open('input.txt')

key = input()
ciphertext = input()

N, M = len(key), len(ciphertext)  # key의 길이 N, 암호문의 길이 M, ex) N=6, M=24

process = [[''] * N for i in range(0, M // N)]  # 2차 list process 선언, ex) 요소 개수가 6인 list 4개 들어 있는 list
for n in range(0, M // N):  # 0부터 <암호문의 길이 / key의 길이의 몫>까지, ex) 0~3
    for m in range(0, M, M // N):  # 0부터 M까지 <암호문의 길이 / key의 길이의 몫>씩 증가, ex) 0~23, 4씩 증가
        process[n][m // (M // N)] += ciphertext[m+n]  # process에 암호문의 m+n의 값이 들어감, ex) 0, 4, 8 ··· 번째 단어 들어감

sort_key_list = sorted(list(key))  # key 문자열을 리스트로 전환하고 사전순으로 정렬, sorted 함수 쓰면 쉽게 정렬됨... 안 쓰고는 힘들지도..

result = [[''] * N for i in range(0, M // N)]  # 2차 list result 선언, ex) 요소 개수가 6인 list 4개 들어 있는 list
for k in range(M // N):  # ex)0부터 3까지
    key_list = list(key)  # 문자열 key를 첫 번째 for문에서 설정
    for j in range(N):  # A B B O T Y
        for i in range(N):  # B A T B O Y
            if sort_key_list[j] == key_list[i]:  # 같은 문자 발견
                result[k][i] += process[k][j]  # process에 j 순서에 있는 문자를 result의 i 순서에 넣어줌
                key_list[i] = '*'  # 한 번 쓰인 단어는 알파벳 외의 임의의 다른 문자로 바꿔줌. 같은 문자가 있을 때를 위해서.
                break  # 최상위 for문을 탈출함

for i in range(len(result)):
    result[i] = ''.join(result[i])

result = ''.join(result)  # list를 문자열로 변환

print(result)
