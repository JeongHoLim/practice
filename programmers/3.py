
# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3

import collections
def solution(lines):
    answer = 0
    stamp = []
    for line in lines:
        hh,mm,ss = map(float,line.split()[1].split(":"))
        T = float(line.split()[2][:-1])
        
        start = hh*3600 + mm*60 + ss - T + 0.001
        end = hh*3600 + mm*60 + ss
        
        start = int(start*1000)
        end = int(end*1000)
        
        stamp.append((start,end))

    stamp.sort(key=lambda x : x[1])
    for i in range(len(stamp)):
        start,end = stamp[i]
        cnt = 0
        for j in range(i,len(stamp)):
            if stamp[j][0] < end + 1000:
                cnt += 1
            
        answer = max(answer,cnt)

    return answer