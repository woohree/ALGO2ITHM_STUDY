import sys
sys.stdin = open('input.txt')
#점화식풀이
max = 11 #
num_list = [1]*max   #+1씩 하는 상황을 나타냄, 1로 가득 채운다

num = 2 #어떤 곳에서든 +2로 접근할 수 있는 곳에 이전 index 값을 더해준다
for i in range(2,max):
    num_list[i] += num_list[i - num]
num = 3 #어떤 곳에서든 +3로 접근할 수 있는 곳에 이전 index 값을 더해준다
for i in range(3,max):
    num_list[i] += num_list[i - num]

t = int(input())
for _ in range(t):
    n = int(input())
    print(num_list[n])