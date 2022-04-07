import sys
sys.stdin = open('B.txt')

N, r, c = map(int, input().split())

n = 2 ** N
answer = 0
while N != 0:
    check = 0
    # col
    if (n - 1) // 2 < c:
        check += 1
        c -= n // 2
    # row
    if (n - 1) // 2 < r:
        check += 2
        r -= n // 2

    if check == 0:
        answer += 4 ** (N-1) * check
        N -= 1
    elif check == 1:
        answer += 4 ** (N-1) * check
        N -= 1
    elif check == 2:
        answer += 4 ** (N-1) * check
        N -= 1
    elif check == 3:
        answer += 4 ** (N-1) * check
        N -= 1
    n //= 2

print(answer)






# 1. matrix 구현 -> N이 10 넘어가면 메모리 초과
# 2. 좌표 값 이용해서 계산 -> 시간 초과
# 3. 우현님 글 보고 마지막 도전...

# matrix 채우는 함수
# def solution(a, b):
#     global k, check
#     for q in range(a, a + 2):
#         for p in range(b, b + 2):
#             matrix[q][p] = k
#             k += 1
#     check += 1
#     return
# 1 - 3 - 7 - 15 - 31
# 최우하단 end 좌표 구하고, 필요한 범위 찾기
# end = 1
# n = 1
# check = 0
# while 1:
#     if end >= r and end < c:
#         m = 1
#         coords = [[0, end + 1]]
#         while m < n:
#             temp = []
#             for i in range(4):
#                 for tempp in temp:
#                     if tempp == [r, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                 if check == 1:
#                     break
#
#                 for coord in coords:
#                     t = coord[:]
#                     if i == 0:
#                         temp.append(t)
#                     elif i == 1:
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 2:
#                         t[0] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 3:
#                         t[0] += 2 ** m
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#             if check == 1:
#                 break
#             coords = temp[:]
#             m += 1
#         break
#     elif end < r and end >= c:
#         m = 1
#         coords = [[end + 1, 0]]
#         answer = 0
#         while m <= n:
#             temp = []
#             for i in range(4):
#                 for tempp in temp:
#                     if tempp == [r, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                 if check == 1:
#                     break
#
#                 for coord in coords:
#                     t = coord[:]
#                     if i == 0:
#                         temp.append(t)
#                     elif i == 1:
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 2:
#                         t[0] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 3:
#                         t[0] += 2 ** m
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#             if check == 1:
#                 break
#             coords = temp[:]
#             m += 1
#         break
#     elif end >= r and end >= c:
#         m = 1
#         coords = [[0, 0]]
#         answer = 0
#         while m < n:
#             temp = []
#             for i in range(4):
#                 for tempp in temp:
#                     if tempp == [r, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                 if check == 1:
#                     break
#                 for coord in coords:
#                     t = coord[:]
#                     if i == 0:
#                         temp.append(t)
#                     elif i == 1:
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 2:
#                         t[0] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 3:
#                         t[0] += 2 ** m
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#             if check == 1:
#                 break
#             coords = temp[:]
#             m += 1
#         break
#     elif 2 ** (n+1) - 1 >= r and 2 ** (n+1) - 1 >= c:
#         m = 1
#         coords = [[end + 1, end + 1]]
#         answer = 0
#         while m < n:
#             temp = []
#             for i in range(4):
#                 for tempp in temp:
#                     if tempp == [r, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                     elif tempp == [r-1, c-1]:
#                         answer = len(coords) * 4 + 4 ** n
#                         check = 1
#                         break
#                 if check == 1:
#                     break
#
#                 for coord in coords:
#                     t = coord[:]
#                     if i == 0:
#                         temp.append(t)
#                     elif i == 1:
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 2:
#                         t[0] += 2 ** m
#                         temp.append(t[:])
#                     elif i == 3:
#                         t[0] += 2 ** m
#                         t[1] += 2 ** m
#                         temp.append(t[:])
#             if check == 1:
#                 break
#             coords = temp[:]
#             m += 1
#         break
#     n += 1
#     end = 2 ** n - 1

# matrix = [[0] * (2**N) for _ in range(2**N)]

# 좌표 list
# n = 1
# coords = [[0, 0]]
# answer = 0
# while n < N:
#     temp = []
#     for i in range(4):
#         for coord in coords:
#             t = coord[:]
#             if i == 0:
#                 temp.append(t)
#             elif i == 1:
#                 t[1] += 2 ** n
#                 temp.append(t[:])
#             elif i == 2:
#                 t[0] += 2 ** n
#                 temp.append(t[:])
#             elif i == 3:
#                 t[0] += 2 ** n
#                 t[1] += 2 ** n
#                 temp.append(t[:])
#     coords = temp[:]
#
#     # coords에서
#     if [r, c] in coords:
#         for j in range(len(coords)):
#             if [r, c] == coords[j]:
#                 answer = j * 4
#                 break
#         break
#     elif [r-1, c] in coords:
#         for j in range(len(coords)):
#             if [r - 1, c] == coords[j]:
#                 answer = j * 4 + 1
#                 break
#         break
#     elif [r, c-1] in coords:
#         for j in range(len(coords)):
#             if [r, c - 1] == coords[j]:
#                 answer = j * 4 + 2
#                 break
#         break
#     elif [r-1, c-1] in coords:
#         for j in range(len(coords)):
#             if [r - 1, c - 1] == coords[j]:
#                 answer = j * 4 + 3
#                 break
#         break
#     n += 1

# matrix 만들기
# k = check = 0
# for coord in coords:
#     solution(coord[0], coord[1])
