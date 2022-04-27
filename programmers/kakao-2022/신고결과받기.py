def solution(id_list, report, k):
    answer = []
    reported = {name:set() for name in id_list}
    max_k = 0
    ban = set()
    for r in report:
        _from, _to = r.split()
        reported[_to].add(_from)
        n = len(reported[_to])
        if n == k:
            ban.add(_to)
    if ban:
        answer = {name:0 for name in id_list}
        for b in ban:
            for reporter in reported[b]:
                answer[reporter] += 1
                
        return list(answer.values())
    return [0,0]
