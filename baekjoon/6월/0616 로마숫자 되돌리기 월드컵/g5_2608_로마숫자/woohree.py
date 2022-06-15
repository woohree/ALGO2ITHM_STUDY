import sys
sys.stdin = open('L.txt')


def rome_to_arab(rome1):
    arab1 = 0
    rome_dict_one = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rome_dict_two = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    len_rome = len(rome1)
    visited = [0] * len_rome                # 인덱스 중복 체크
    for i in range(len_rome):
        if not visited[i]:
            if i < len_rome-1 and rome1[i] + rome1[i+1] in rome_dict_two:   # 두 글자 있는 경우
                visited[i], visited[i+1] = 1, 1
                arab1 += rome_dict_two[rome1[i]+rome1[i+1]]
            else:                           # 한 글자
                visited[i] = 1
                arab1 += rome_dict_one[rome1[i]]
    return arab1


def arab_to_rome(arab2):
    rome2 = ''
    arab_list_one = ['I', 'X', 'C', 'M']    # 1, 10, 100, 1000
    arab_list_two = ['V', 'L', 'D']         # 5, 50, 500
    arab_list_thr = ['IV', 'XL', 'CD']      # 4, 40, 400
    arab_list_for = ['IX', 'XC', 'CM']      # 9, 90, 900
    i = len(arab2) - 1                      # 리스트 탐색 인덱스
    j = 0                                   # 아라비아 숫자 인덱스(좌측부터)
    while j < len(arab2):
        n = arab2[j]
        if n == '4':                        # 4, 9는 한 가지씩 뿐
            rome2 += arab_list_thr[i]
        elif n == '9':
            rome2 += arab_list_for[i]
        elif n in '123':                    # 1, 2, 3 중 하나면 수만큼 반복
            for _ in range(int(n)):
                rome2 += arab_list_one[i]
        elif n in '5678':                   # 5, 6, 7, 8 중 하나면
            rome2 += arab_list_two[i]       # 일단 5 더하고
            if n != '5':                    # 5 아닌 경우에, 나머지만큼 반복
                for _ in range(int(n)%5):
                    rome2 += arab_list_one[i]
        i -= 1
        j += 1
    return rome2


arab = 0
for _ in range(2):
    rome = input()
    arab += rome_to_arab(rome)
print(arab)
print(arab_to_rome(str(arab)))
