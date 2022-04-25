from itertools import combinations_with_replacement

def solution(n, info):
    # 출력을 위해 초기화
    max_answer, answer = -1, [-1]
    # 중복 조합을 만들고 반복
    for ryan_arrow in list(combinations_with_replacement(range(0, 11), n)):
        # 조합을 만든 문제로 라이언 화살 만들기
        ryan_info = [0 for _ in range(11)]
        for r in ryan_arrow:
            ryan_info[10 - r] += 1

        # 점수 계산
        apeach_score, ryan_score = 0, 0
        for idx, kakao in enumerate(zip(info, ryan_info)):
            apeach, ryan = kakao[0], kakao[1]
            if (apeach, ryan) != (0, 0):
                if apeach < ryan:
                    ryan_score += 10 - idx
                else:
                    apeach_score += 10 - idx
        # 라이언이 이기고 최대 차이보다 크면 결과 갱신
        if apeach_score < ryan_score:
            diff = ryan_score - apeach_score
            if max_answer < diff:
                max_answer = diff
                answer = ryan_info
    return answer
 
n = 10
info = 	[0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))