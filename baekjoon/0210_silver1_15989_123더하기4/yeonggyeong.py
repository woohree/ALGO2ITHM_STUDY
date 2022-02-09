
def plus(number):

    # 1, 2, 3으로 1, 2, 3 만들 수 있는 경우의 수는 미리 세팅
    # 예를 들어, [1, 0, 0] 은 1로 1을 만들수 있는 경우는 1가지, 2로 만들 수 있는 경우는 0가지, 3으로 만들 수 있는 경우는 0가지 
    answer = [[1, 0, 0],
            [1, 1, 0],
            [1, 1, 1], ]

    # answer를 입력받은 수 만큼 늘이기 위해 진행
    for _ in range(number-3):
        answer.append([1,0,0])

    """
    4를 1으로 만들 수 있는 경우는 1가지 ( 1+1+1+1 ), 
    4를 2으로 만들 수 있는 경우는 4-2 = 2를 1과 2로 만들 수 있는 경우의 수 -> 1 + 1 총 2가지
    4를 3으로 만들 수 있는 경우는 4-3 = 1을 1, 2, 3으로 만들 수 있는 경우의 수 -> 총 1가지

    위 과정을 입력한 수까지 반복
    """
    for num in range(3,number):
        answer[num][1] = answer[num-2][0] + answer[num-2][1]
        answer[num][2] = answer[num-3][0] + answer[num-3][1] + answer[num-3][2]

    return sum(answer[number-1])

inp = int(input())

for i in range(inp):
    n = int(input())
    print(plus(n))