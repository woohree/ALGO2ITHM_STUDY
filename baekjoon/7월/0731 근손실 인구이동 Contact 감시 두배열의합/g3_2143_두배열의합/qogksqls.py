import sys, bisect
sys.stdin = open('B.txt')

'''
bisect_left(literable, value) : 왼쪽 인덱스를 구하기
bisect_right(literable, value) : 오른쪽 인덱스를 구하기
'''

T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

sums1 = []
a = 0
while a < n:
    temp = 0
    for i in range(a, n):
        temp += arr1[i]
        sums1.append(temp)
    a += 1

sums2 = []
b = 0
while b < m:
    temp = 0
    for i in range(b, m):
        temp += arr2[i]
        sums2.append(temp)
    b += 1

sums1.sort()  # [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
sums2.sort()  # [1, 2, 3, 4, 5, 6]

'''
sum2에서 (T - sum1[i])에 해당하는 숫자의 개수를 찾는 과정
le와 ri는 각각 해당 숫자가 처음으로 나오는 인덱스와 다를 숫자가 나오게 되는 인덱스를 가져옴
따라서 ri - le 하면 해당 숫자의 개수가 나옴
그걸 ans에 더하면 됨
'''
ans = 0
for i in range(len(sums1)):
    le = bisect.bisect_left(sums2, T - sums1[i])
    ri = bisect.bisect_right(sums2, T - sums1[i])
    ans += ri - le
print(ans)

'''
def solution(x):
    global ans
    l = 0
    while l < m:
        temp2 = x
        for j in range(l, m):
            temp2 += arr2[j]
            if temp2 == T:
                ans += 1
                break
        l += 1
    return


sum_arr2 = sum(arr2)
ans, k = 0, 0
while k < n:
    temp1 = 0
    for i in range(k, n):
        temp1 += arr1[i]
        solution(temp1)
    k += 1
print(ans)
'''