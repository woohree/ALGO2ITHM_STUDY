import sys
sys.stdin = open('L.txt')


def get_cnt(col_chars):
    cnt = 0
    l = 0
    r = R-1
    while l <= r:                               # 이진 탐색
        mid = (l+r) // 2
        chars_dict = {}
        for chars in col_chars:
            chars = ''.join(chars[mid:])        # tuple 만드는 거보다 join이 빠름... 이유는 모름
            chars_dict.setdefault(chars, 0)
            chars_dict[chars] += 1
            if chars_dict[chars] > 1:
                r = mid - 1                     # 중복이 있으면 r을 mid 왼쪽으로
                break
        else:                                   # 없으면 l을 mid 오른쪽으로
            l = mid + 1
            cnt = mid                           # 이때 mid 값이 cnt가 됨

    return cnt


R, C = map(int, input().split())
sentences = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
col_chars = []
for j in range(C):                              # 세로로 뽑아다가 리스트 만드는 for문
    col_char = []                               # 문자열로도 해봤는데 리스트로 넘겨서 join 하는거 보다 느림... 이유는 모름
    for i in range(R):
        col_char.append(sentences[i][j])
    col_chars.append(col_char)
ans = get_cnt(col_chars)

print(ans)


# 완전탐색은 시간 초과
# def get_cnt(col_chars):
#     cnt = 0
#     while cnt < R-1:
#         chars_dict = {}
#         for chars in col_chars:
#             chars.popleft()
#             chars = str(chars)
#             chars_dict.setdefault(chars, 0)
#             chars_dict[chars] += 1
#             if chars_dict[chars] > 1:
#                 return cnt
#         cnt += 1
#     return cnt