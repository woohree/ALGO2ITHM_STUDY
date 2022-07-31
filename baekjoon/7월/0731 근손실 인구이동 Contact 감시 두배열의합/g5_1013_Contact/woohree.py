import sys
sys.stdin = open('W.txt')


for _ in range(int(input())):
    wave = input()
    is_vega = 1
    while len(wave) > 0:
        if wave[:3] == '100':                           # 100인 경우
            wave = wave[3:]

            while len(wave) > 0 and wave[0] == '0':     # 100+ 체크
                wave = wave[1:]

            if not wave:                                # 100+1 1이 하나 이상 붙어줘야함
                is_vega = 0
                break
            wave = wave[1:]

            while len(wave) > 0 and wave[0] == '1':     # 100+1+
                if len(wave) > 2 and (wave[:3] == '100' or wave[:2] == '01'):
                    break                               # 다음에 100 혹은 01이 나올 수 있음
                else:                                   # 100+1+ 체크
                    wave = wave[1:]

        elif wave[:2] == '01':                          # 01인 경우
            wave = wave[2:]

        else:
            is_vega = 0
            break
    if is_vega:
        print('YES')
    else:
        print('NO')