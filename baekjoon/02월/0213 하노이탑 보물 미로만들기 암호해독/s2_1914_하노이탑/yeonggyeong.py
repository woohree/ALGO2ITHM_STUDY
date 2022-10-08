# n개의 원반과 3개의 기둥 
# n개의 원반을 모두 가장 끝 ( end ) 기둥으로 옮기기 위해서는 가장 큰 원반을 제외하고 
# 두번째 기둥으로 모두 이동
# 이후, 가장 큰 원반을 첫번째 기둥에서 마지막 기둥으로 이동
# 마지막으로 , 나머지 원반을 마지막 기둥으로 이동

def hanoi(start, median, end, n):

    if n == 1:
        print(start, end, sep = " ")
        return

    hanoi(start, end, median, n-1)
    hanoi(start, median, end, 1)
    hanoi(median, start, end, n-1)


n = int(input())
# 횟수를 구하는 공식
move = (2 ** n) - 1
print(move)
if n <= 20:
    hanoi(1, 2, 3, n)