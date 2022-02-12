# 40분

# 리스트를 오름차순으로 정렬
def get_sorted_list(numbers):
    for time in range(N-1, 0, -1):
        for idx in range(time):
            if numbers[idx] > numbers[idx+1]:
                numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
    return numbers

# 리스트 내 숫자를 큰 순서로 해당 인덱스를 정렬하여 추출
def get_max_idxs(numbers):
    idxs = []
    for _ in range(N):
        my_max = 0
        my_idx = 0
        for idx in range(N):
            if my_max <= numbers[idx] and idx not in idxs:
                my_max = numbers[idx]
                my_idx = idx
        idxs.append(my_idx)
    return idxs

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# 함수화
def S(numbers1, numbers2):
    result = 0
    for idx in range(N):
        result += numbers1[idx] * numbers2[idx]
    return result

# 인풋받기
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 오름차순 정렬
sortedA = get_sorted_list(A)

# B 안의 숫자를 큰 순서로 해당 인덱스를 정렬하여 추출
max_idxsB = get_max_idxs(B)

# 새로운 리스트 new_A에,
# B에서 추출한 인덱스 마다 오름차순 정렬한 A를 넣어줌
new_A = [0] * N
idx_new = 0
for idx in max_idxsB:
    new_A[idx] += sortedA[idx_new]
    idx_new += 1

# 예시)
# A = [1 1 1 6 0]
# B = [2 7 8 3 1] 라면,
# 정렬A = [0 1 1 1 6]
# 인덱스B = [2 1 3 0 4] 가 된다.
# 이때
# new_A = [0 0 0 0 0] 이므로,
# new_A[idx]에 정렬A[0] 부터 순서대로 넣어주면 완성
print(S(new_A, B))