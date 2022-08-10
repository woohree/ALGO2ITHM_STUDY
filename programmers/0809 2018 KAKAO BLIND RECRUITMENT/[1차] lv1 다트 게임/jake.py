def solution(dartResult):
    # 리스트로 바꾸기
    dartResult = list(dartResult)
    stack_one = None
    stack_two = None
    stack_three = None
    for i in range(len(dartResult)):
        # 숫자 스택에 채워놓기
        if dartResult[i].isdecimal() == True:
            # 10일 때
            if dartResult[i+1].isdecimal() == True:
                if stack_one == None :
                    stack_one = 10
                    # 10으로 이미 바꿨으므로 다음 숫자를 없앰
                    dartResult[i+1] = 'C'
                elif stack_one != None and stack_two == None :
                    stack_two = 10
                    dartResult[i+1] = 'C'
                elif stack_one != None and stack_two != None and stack_three == None:
                    stack_three = 10
                    dartResult[i+1] = 'C'
            # 0~9일 때 그냥 추가
            else:
                if stack_one == None :
                    stack_one = int(dartResult[i])
                elif stack_one != None and stack_two == None :
                    stack_two = int(dartResult[i])
                elif stack_one != None and stack_two != None and stack_three == None:
                    stack_three = int(dartResult[i])
        else:
            # 첫번째 점수
            if stack_two == None and stack_three == None:
                if dartResult[i] == 'S':
                    pass
                elif dartResult[i] == 'D':
                    stack_one *= stack_one
                elif dartResult[i] == 'T':
                    stack_one *= stack_one*stack_one
                elif dartResult[i] == '#':
                    stack_one = -stack_one
                elif dartResult[i] == '*':
                    stack_one *= 2
            # 두번째 점수
            elif stack_two != None and stack_three == None:
                if dartResult[i] == 'S':
                    pass
                elif dartResult[i] == 'D':
                    stack_two *= stack_two
                elif dartResult[i] == 'T':
                    stack_two *= stack_two*stack_two
                elif dartResult[i] == '#':
                    stack_two = -stack_two
                elif dartResult[i] == '*':
                    stack_two *= 2
                    stack_one *= 2
            # 세번째 점수
            elif stack_three != None:
                if dartResult[i] == 'S':
                    pass
                elif dartResult[i] == 'D':
                    stack_three *= stack_three
                elif dartResult[i] == 'T':
                    stack_three *= stack_three*stack_three
                elif dartResult[i] == '#':
                    stack_three = -stack_three
                elif dartResult[i] == '*':
                    stack_two *= 2
                    stack_three *= 2
    answer = stack_one + stack_two + stack_three
    return answer