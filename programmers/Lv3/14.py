# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3#

from collections import defaultdict,deque
def solution(gems):
    answer = []

    s = e = 0
    count = defaultdict(int)
    window = deque()
    current,n = 0, len(set(gems))
    length = float('inf')

    while e < len(gems):
        cur = gems[e]
        count[cur] += 1
        window.append(e)
        if count[cur] == 1:
            current += 1
        if current == n:
            while True:
                if length > e-s+1:
                    answer = [s+1,e+1]
                length = min(length,e-s+1)
                if length == n: 
                    return [s+1,e+1]
                peek = gems[s]
                if count[peek] == 1:
                    break
                count[gems[window.popleft()]] -= 1
                s += 1

        e += 1
    while count[gems[s]] > 1:
        length = min(length,e-s)
        count[window.popleft()] -= 1
        s += 1

    return answer