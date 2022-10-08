n = int(input())

max_list = [] #최고 길이를 저장할 max_list
for i in range(1, n + 1): #두번째로 나올 수를 전수조사
    my_list = [n]
    my_list.append(i)

    idx = 1
    while True: #세번째 수부터는 my list에 저장
        next_num = my_list[idx - 1] - my_list[idx] #연산
        if next_num < 0: #음수가 나오면 종료
            break
        my_list.append(next_num)
        idx += 1

    if len(max_list) < len(my_list): #지금까지 최고기록과 비교
        max_list = my_list #if문 통과시 변경

print(len(max_list))
for i in max_list:
    print(i, end=' ')