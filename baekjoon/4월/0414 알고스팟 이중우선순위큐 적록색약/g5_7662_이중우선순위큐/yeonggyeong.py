import heapq
import sys
sys.stdin = open('G.txt')

T = int(input())
for tc in range(T):
    k = int(sys.stdin.readline())

    max_heap, min_heap = [], []
    dic = dict()

    for _ in range(k):
        operator, num = sys.stdin.readline().split()

        if operator == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
            
            # 들어온 숫자를 key로 하는 dictionary생성
            if int(num) not in dic.keys():
                dic[int(num)] = 1
            else:
                dic[int(num)] += 1
        else:
            # 최댓값 삭제
            if num == '1':
                while max_heap:
                    number = - heapq.heappop(max_heap)
                    if dic[number] > 0:
                        dic[number] -= 1
                        break
            # 최솟값 삭제
            else:
                while min_heap:
                    number = heapq.heappop(min_heap)
                    if dic[number] > 0:
                        dic[number] -= 1
                        break

    # 남아있는 숫자들만 뽑아내기   
    remain = []
    for key, value in dic.items():
        if value > 0:
            remain.append(key)
    
    remain.sort()
    if remain:
        print(str(remain[-1]),str(remain[0]))
    else:
        print('EMPTY')