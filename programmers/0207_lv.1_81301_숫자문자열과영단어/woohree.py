def solution(s):    
    answer = ''
    words = {'zero': '0',
             'one': '1',
             'two': '2',
             'three': '3',
             'four': '4',
             'five': '5',
             'six': '6',
             'seven': '7',
             'eight': '8',
             'nine': '9'}

    word = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            word += char
            if word in words:
                answer += words[word]
                word = ''
    return int(answer)