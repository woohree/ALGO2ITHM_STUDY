# 60분
import sys
sys.stdin = open('B.txt')

'''
문제가 이해 못해서 시간 날림;;
초밥은 연속적으로 k개 먹으나 그 안에서 중복 값은 사라지게 하면 된다.
중복되지 않는 초밥의 개수에서 만약 쿠폰 번호가 없다면 1을 더해주면 된다.
1. 회전 초밥이므로 인풋인 sushi list 에서 sushi[:k-1]를 더해주었다.
2. check 딕셔너리를 이용해 초밥 중복을 지우면서 개수를 셌다.
3. 최대값 구하는 과정에서 check에 쿠폰 번호가 없다면 1 더한값을 my_max에 저장했다.
'''

N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
sushi = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
# 1번
sushi += sushi[:k-1]

my_max = 0
for i in range(N):
    # 2번
    check = {}
    temp = 0
    for j in range(i, k+i):
        if check.get(sushi[j]):
            pass
        else:
            check[sushi[j]] = 1
            temp += 1
    # 3번
    if my_max <= temp:
        my_max = temp
        if check.get(c):
            pass
        else:
            my_max = temp + 1

print(my_max)
