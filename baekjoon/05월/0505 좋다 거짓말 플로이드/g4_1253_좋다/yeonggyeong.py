import bisect
import sys
sys.stdin = open('G.txt')

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

good = 0
for i in range(N):
    new_numbers = numbers[:i] + numbers[i+1:]
    new = numbers[i]
    start, end = 0, len(new_numbers) - 1

    while start < end:
        sum_number = new_numbers[start] + new_numbers[end]
        if sum_number == new:
            good += 1
            break
        elif new > sum_number:
            start += 1
        elif new < sum_number:
            end -= 1
print(good)
























#
# import bisect
# import sys
# sys.stdin = open('G.txt')
#
# N = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
#
# numbers.sort()
#
#
# answer = 0
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             new_number = numbers[i] + numbers[j]
#             min_lo = bisect.bisect_left(numbers, new_number)
#             max_lo = bisect.bisect_right(numbers, new_number)
#             good_number = []
#             for idx in range(min_lo, max_lo):
#                 if idx not in (i, j):
#                     good_number.append(idx)
#             if len(good_number) >= 1:
#                 answer += 1
#                 break
# print(answer)




# visited = [0 for _ in range(1000000000)]
# answer = 0

# for i in range(N):
#     for j in range(i+1, N):
#         new_number = numbers[i] + numbers[j]
#         new_matrix = numbers[j+1:]
#         find_idx = bisect.bisect_left(new_matrix, new_number)
#         if find_idx < len(new_matrix) and new_matrix[find_idx] == new_number and not visited[new_number]:
#             visited[new_number] = 1
#             answer += 1

#
# for i in range(N-1, 1, -1):
#     for j in range(i):
#         diff = numbers[i] - numbers[j]
#         matrix = numbers[j+1:i]
#         find_idx = bisect.bisect_left(matrix, diff)
#         if find_idx < len(matrix) and numbers[find_idx] == diff:
#             answer += 1
#             break
        # print(bisect.index(numbers, numbers[i] - numbers[j]))
        # if (numbers[i] - numbers[j]) in numbers:
        #     answer += 1
        #     break
# print(answer)
