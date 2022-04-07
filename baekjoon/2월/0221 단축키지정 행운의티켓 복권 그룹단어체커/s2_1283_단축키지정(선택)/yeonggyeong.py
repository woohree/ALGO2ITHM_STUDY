import sys
sys.stdin = open('G.txt')

shortcut_list = [] # 단축키로 설정된 리스트 ( 대문자 )
idx_list = [] # print하기 위해 index리스트 설정
n = int(input())
funs = [input() for _ in range(n)]

register_fun = []
for fun in funs:
    for i in range(len(fun)):
        # 첫번째 글자가 단축키 리스트에 없다면 단축키 리스트 추가
        if i == 0 and fun[i].upper() not in shortcut_list and fun[i] != ' ':
            register_fun.append(fun)
            shortcut_list.append(fun[i].upper())
            idx_list.append(i)
            break
        # 단어가 공백이며 다음글자가 단축키 리스트에 없다면 단축키 리스트 추가
        elif fun[i] == ' ' and fun[i+1].upper() not in shortcut_list and fun[i+1] != ' ':
            register_fun.append(fun)
            shortcut_list.append(fun[i+1].upper())
            idx_list.append(i+1)
            break

for fun in funs:
    # 단축키가 등록되지 않은 기능이라면
    if fun not in register_fun:
        for i in range(len(fun)):
            # 왼쪽글자 부터 반복하여 등록되지 않은 글자를 단축키 리스트 추가
            if fun[i] != ' ' and fun[i].upper() not in shortcut_list:
                register_fun.append(fun)
                shortcut_list.append(fun[i].upper())
                idx_list.append(i)
                break
        # 전부 안 된다면, 의미없는 값 추가
        if fun not in register_fun:
            register_fun.append(fun)
            shortcut_list.append('99')
            idx_list.append(-1)

for fun in funs:
    for i in zip(register_fun, idx_list):
        # 처음 입력 받은 단어의 순서와 단축키 등록 순서가 다르기 때문에, zip 사용
        # (New, 0) 과 같은 형식
        if fun == i[0]:
            for j in range(len(fun)):
                # 단축키로 설정된 인덱스와 현재 인덱스가 같다면 [] 추가
                if j == i[1]:
                    print('['+ f'{i[0][j]}' + ']', end='')
                else:
                    print(i[0][j], end ='')
            # 가장 마지막 기능은 뒤에 공백 제거
            if fun != funs[-1]:
                print()

    
