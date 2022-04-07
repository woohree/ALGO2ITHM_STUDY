# 75분 + 12:
# 몇 개를 구매, 포장지 색깔
# 상민이가 포장한 선물의 개수, 포장한 선물들의 번호를 오름차순으로 출력
# 지수가 포장한 선물의 개수, 포장한 선물들의 번호를 오름차순으로 출력
import sys
sys.stdin = open('B.txt')

A, B, N = map(int, input().split())
sell_list = [list(map(str, input().split())) for _ in range(N)]

if A > 0 and B > 0:
    if sell_list[-1][1] == 'B':
        sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]) * A)
    else:
        sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]) * B)
    for sell in sell_list:
        if sell[1] == 'B':
            for i in range(int(sell[0]), int(sell[0]) + int(sell[2]) * A, A):
                for a in range(1, A+1):
                    if sell_product[i - a] == 1 or sell_product[i - a] == 3:
                        sell_product[i + a] += 1
                        break
                    else:
                        sell_product[i] += 1
                        break
                    sell_product[i] += 1

        if sell[1] == 'R':
            for i in range(int(sell[0]), int(sell[0]) + int(sell[2]) * B, B):
                for b in range(1, B+1):
                    if sell_product[i - b] == 2 or sell_product[i - b] == 3 or sell_product[i + b] == 2 or sell_product[i + b] == 3:
                        sell_product[i + b] += 2
                        break
                    else:
                        sell_product[i] += 2
                        break
else:
    if A == 0 and B == 0:
        sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]))
        for sell in sell_list:
            if sell[1] == 'B':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2])):
                    sell_product[i] += 1
            if sell[1] == 'R':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2])):
                    sell_product[i] += 2

    elif A == 0 and B > 0:
        if sell_list[-1][1] == 'B':
            sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]))
        else:
            sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]) * B)

        for sell in sell_list:
            if sell[1] == 'B':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2])):
                    sell_product[i] += 1

            if sell[1] == 'R':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2]) * B, B):
                    sell_product[i] += 2

    elif A > 0 and B == 0:
        if sell_list[-1][1] == 'B':
            sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]) * A)
        else:
            sell_product = [0] * (int(sell_list[-1][0]) + int(sell_list[-1][2]))

        for sell in sell_list:
            if sell[1] == 'B':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2]) * A, A):
                    for a in range(1, A+1):
                        if sell_product[i - a] == 1 or sell_product[i - a] == 3:
                            sell_product[i + a] += 1
                            break
                        else:
                            sell_product[i] += 1
                            break

            if sell[1] == 'R':
                for i in range(int(sell[0]), int(sell[0]) + int(sell[2])):
                    sell_product[i] += 2

sangmin = jisoo = 0
sangmin_product = []
jisoo_product = []
product = 1
for i in range(len(sell_product)):
    if sell_product[i] == 1 or sell_product[i] == 3:
        sangmin += 1
        sangmin_product.append(product)
        product += 1
    if sell_product[i] == 2 or sell_product[i] == 3:
        jisoo += 1
        jisoo_product.append(product)
        product += 1

print(sangmin)
print(*sangmin_product)
print(jisoo)
print(*jisoo_product)
