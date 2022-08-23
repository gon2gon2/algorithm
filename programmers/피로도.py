from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 최소 필요가 소모보다 작을 수도 있따?!
    for perm in permutations(dungeons):
        temp_answer = 0
        temp_k = k
        # 한 던전씩 돌면서 돌 수 있는 만큼 센다. 못 돌면 바로 break
        for p in perm:
            if temp_k < p[0]: break
            temp_answer += 1
            temp_k -= p[1]
            
        answer = max(answer, temp_answer)
            
    return answer