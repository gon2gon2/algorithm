'''
아이디어를 좀 더 구체적으로 생각해보고 버리는 게 필요할 것 같다.
너무 쉽게 포기했다.
'''

def solution(name):
    answer = 0
    length = len(name)
    import string
    alpha_book = {k:min(i, 26-i) for i, k in enumerate(string.ascii_uppercase)}
    
    move_cnt = length - 1
    
    for idx, char in enumerate(name):
        answer += alpha_book[char]
        
        next_idx = idx + 1
        while next_idx < length and name[next_idx] == 'A':
            next_idx += 1
        
        move_cnt = min(move_cnt, idx + idx + length - next_idx, idx + 2 * (length-next_idx))
        
    answer += move_cnt
    return answer

