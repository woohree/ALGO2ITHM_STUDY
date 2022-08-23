def solution(m, musicinfos):
    answer = '(None)'
    longest = 0
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        time = (int(musicinfo[6:8]) - int(musicinfo[:2])) * 60\
               + int(musicinfo[9:11]) - int(musicinfo[3:5])  # 시간 계산

        whole_music, i = [], 0  # 일단 반복 돌려서 전체 음악 구함
        while i <= time:
            if i != time - 1 and info[3][(i + 1) % len(info[3])] == '#':
                whole_music.append(info[3][i % len(info[3])] + info[3][(i + 1) % len(info[3])])
                i += 1
                time += 1
            else:
                whole_music.append(info[3][i % len(info[3])])
            i += 1

        j = 0
        while j < len(whole_music):  # 'C'나 'C#' 나오는거 구별해서 음악 계산
            temp = ''
            if whole_music[j] == m[0] or whole_music[j] == m[:2]:
                if whole_music[j] == m[0]:
                    temp, k, l = m[0], 1, 1
                else:
                    temp, k, l = m[:2], 2, 1

                while k < len(m):
                    if j + l < len(whole_music) and m[k] == whole_music[j + l]:
                        temp += m[k]
                    elif j + l < len(whole_music) and m[k:k + 2] == whole_music[j + l]:
                        temp += m[k:k + 2]
                        k += 1
                    else:
                        break
                    k += 1
                    l += 1
            if m == temp and longest < time:
                answer = info[2]
                longest = time
            j += 1
    return answer