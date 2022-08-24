def solution(msg):
    answer = []
    alpha = {}
    # 아스키코드 이용해서 딕셔너리 만듦
    for i in range(26):
        alpha[chr(65+i)] = i+1
    # 숫자 지정해놓고 압축 됐는지 확인함
    # A는 시작지점, B는 끝나는 지점
    A, B = 0, 0
    while 1:
        B += 1
        # 만약 B가 끝에 다다랐다면 종료
        if B == len(msg):
            # answer에 딕셔너리에 있는 것을 추가함
            answer.append(alpha[msg[A:B]])
            break
        # 만약 A부터 B까지 합친 글자가 딕셔너리에 없다면 딕셔너리에 +1 해서 추가함
        if msg[A:B+1] not in alpha:
            alpha[msg[A:B+1]] = len(alpha) + 1
            answer.append(alpha[msg[A:B]])
            # 추가하고나서부터는 앞 번호를 바꿔줌
            A = B
    return answer