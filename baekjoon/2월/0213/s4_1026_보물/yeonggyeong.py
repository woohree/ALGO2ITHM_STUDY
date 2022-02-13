
# 문제 해결을 위해서는 a_list의 최솟값과 b_list의 최댓값을 곱해야 최종 합이 최솟값이 된다고 생각
# 따라서, 기존 리스트의 최솟값, 최댓값을 각각 찾아 새로운 리스트에 할당 한 후, 기존 리스트에 제거를 반복

def solution(n, a_list, b_list):
    # 최솟값과 최대값을 곱한 결과를 담을 새로운 리스트 생성
    answer_lst = []
    for i in range(n):
        # 초기값 설정[최솟값/최대값, 인덱스]
        min_a = [101, 0]
        max_b = [0, 0]
        # 반복문을 한 번만 돌리기 위해서 zip과 enumerate 사용하여 각각의 인덱스도 저장
        for idx, a_b in enumerate(zip(a_list, b_list)):
            if a_b[0] < min_a[0] :
                min_a[0] = a_b[0]
                min_a[1] = idx

            if a_b[1] > max_b[0] :
                max_b[0] = a_b[1]
                max_b[1] = idx
        # 찾은 최솟값과 최대값을 곱하여 리스트에 저장
        answer_lst.append(min_a[0] * max_b[0])
        # 해당 값 삭제 => [1, 1, 1, 6, 0] , [2, 7, 8, 3, 1] --> [1, 1, 1, 6], [2, 7, 3, 1]
        del a_list[min_a[1]]
        del b_list[max_b[1]]

    answer = 0
    for an in answer_lst:
        answer += an
    return answer

n = int(input())
a_list = list(map(int,input().split(' ')))
b_list = list(map(int,input().split(' ')))
print(solution(n, a_list, b_list))