def solution(s):
    if 1 <= len(s) <= 50:
        if s.startswith('0') or s.startswith('z'):
            return '0이나 zero로 시작하면 안됩니다.'
    else:
        return 's의 길이가 너무 깁니다..'
    
    if s.find('one') != -1:
        return solution(s.replace('one', '1'))
    elif s.find('two') != -1:
        return solution(s.replace('two', '2'))
    elif s.find('three') != -1:
        return solution(s.replace('three', '3'))
    elif s.find('four') != -1:
        return solution(s.replace('four', '4'))
    elif s.find('five') != -1:
        return solution(s.replace('five', '5'))
    elif s.find('six') != -1:
        return solution(s.replace('six', '6'))
    elif s.find('seven') != -1:
        return solution(s.replace('seven', '7'))
    elif s.find('eight') != -1:
        return solution(s.replace('eight', '8'))
    elif s.find('nine') != -1:
        return solution(s.replace('nine', '9'))
    elif s.find('zero') != -1:
        return solution(s.replace('zero', '0'))
    else:
        return int(s)