
# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3#

from math import ceil,gcd,floor
def solution(w,h):
    
    answer = w*h
    useless = 0
    
    nh = max(h,w)
    nw = min(h,w)
    
    a = nh / nw
    
    g = gcd(nh,nw)
    dw,dh = nw // g, nh//g
    
    
    for i in range(dw):
        f1 = a*i+dh
        f2 = a*(i+1) + dh
        useless += (ceil(f2)-floor(f1))
        
    if nw != dw:
        useless *= g
    
    answer -= useless
    
    
    return answer