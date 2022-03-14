
def find_paper(n, a, b):
    global one_count, zero_count, minus_one_count

    if n == 1:
        if papers[a][b] == -1:
            one_count += 1
        elif papers[a][b] == 0:
            zero_count += 1
        else:
            minus_one_count += 1

    else:
        check = 0
        for i in range(a, a + n - 2):
            # 다음 if 문에서 다음꺼까지 미리 비교하므로 range 마지막 값을 -1 해준다.
            for j in range(b, b + n - 2):
                check = papers[i][j]
                if check != papers[i][j + 1]:
                    find_paper(n//3 + 1, i, j-2)

        if check == -1:
            one_count += 1
        elif check == 0:
            zero_count += 1
        else:
            minus_one_count += 1

    return


def check_paper(n, a, b):
    for i in range(a, a + n - 2):
        # 다음 if 문에서 다음꺼까지 미리 비교하므로 range 마지막 값을 -1 해준다.
        for j in range(b, b + n - 1):
            check = papers[i][j]
            if check != papers[i][j + 1]:
                find_paper(n//3 + 1, i, j-2)

    return


import sys
sys.stdin = open('B.txt')

N = int(input())
papers = [list(map(int, input().split())) + [2] for _ in range(N)]

one_count = zero_count = minus_one_count = 0
check_paper(N+1, 0, 0)

print(minus_one_count)
print(zero_count)
print(one_count)
