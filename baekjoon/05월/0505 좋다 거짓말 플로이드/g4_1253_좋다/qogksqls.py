import sys, bisect
sys.stdin = open('B.txt')

'''
1. 정렬
2. 현재 값(current)을 제외한 list 생성(new_numbers) -> slice 이용
3. new_numbers 에서 현재 값을 더해서 만들 수 있는 두 수(a, b)를 찾아야 한다. -> bisect 이용

pypy 는 600ms 인데 python3는 7% 시간초과;;
'''

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort()


def binary_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == arr[mid]:
            return True
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


answer = 0
for i in range(N):
    current = numbers[i]

    for j in range(N):
        if i != j:
            a = numbers[j]
            b = current - a
            if binary_search(numbers, b):
                if j != bisect.bisect_left(numbers, b):  # new_numbers 안에 a도 포함되어 있기 때문에 ex) current = 2, new_numbers = [0, 1]
                    answer += 1
                    break

print(answer)
