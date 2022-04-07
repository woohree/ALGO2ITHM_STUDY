import sys
sys.stdin = open('L.txt')

# 50분

def get_sorting_guitar_list(serial, N):
    # 버블정렬 이용!
    for i in range(N-1, 0, -1):
        for j in range(i):
            # 길이가 다른 경우,
            # 길이가 짧은 게 앞으로 오도록!
            if len(serial[j]) > len(serial[j+1]):
                serial[j], serial[j+1] = serial[j+1], serial[j]
                
            # 길이가 같은 경우,
            # 문자열 내 숫자만 더해서 합이 작은 게 앞으로 오도록!
            elif len(serial[j]) == len(serial[j+1]):
                sum1 = 0
                sum2 = 0
                # 문자열 뒤지면서 isdecimal로 숫자인지 판별해서 더해줌
                for idx1 in range(len(serial[j])):
                    if serial[j][idx1].isdecimal() == True:
                        sum1 += int(serial[j][idx1])
                for idx2 in range(len(serial[j+1])):
                    if serial[j+1][idx2].isdecimal() == True:
                        sum2 += int(serial[j+1][idx2])
                if sum1 > sum2:
                    serial[j], serial[j + 1] = serial[j + 1], serial[j]
                
                # 숫자만 더한 값이 같은 경우,
                # 문자열을 사전순으로 배열!
                elif sum1 == sum2:
                    for idx3 in range(len(serial[j])):
                        # 같은 경우, 계속 진행
                        # if serial[j][idx3] == serial[j+1][idx3]:
                        #     continue
                        # 뒤엣놈이 큰 경우, 관둠
                        if serial[j][idx3] < serial[j+1][idx3]:
                            break
                        # 앞엣놈이 큰 경우, 바꾸고 관둠
                        elif serial[j][idx3] > serial[j + 1][idx3]:
                            serial[j], serial[j + 1] = serial[j + 1], serial[j]
                            break

    return serial

N = int(input())
serial = [input() for _ in range(N)]
ans = get_sorting_guitar_list(serial, N)
for serial_number in ans:
    print(serial_number)
