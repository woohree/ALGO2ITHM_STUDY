'''
1. temp라는 리스트에
    [헤더(소문자 변환), 숫자, 순서, 원래 파일 명]
    이라는 배열을 넣고 sort 돌림
'''


def solution(files):
    temp = []
    for i in range(len(files)):
        hnt = files[i].split('.')
        header, number = '', ''
        for j in range(len(hnt[0])):
            if hnt[0][j].isdigit():
                number += hnt[0][j]
            else:
                if not number:
                    header += hnt[0][j].lower()
        number = int(number)
        index = 0
        for t in temp:
            if t[0] == header and t[1] == number:
                index += 1
        temp.append([header, number, index, files[i]])
    temp.sort()
    answer = []
    for t in temp:
        answer.append(t[3])
    return answer


solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
