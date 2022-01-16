
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    
    phone = {1:'L',4:'L',7:'L',
            3 :'R',6 :'R',9 :'R',
            2 : 'B',5 :'B',8 :'B',0 :'B'
            }
    pos = {1: (0,3) ,4:(0,2),7:(0,1),
            3 :(2,3),6 :(2,2),9 :(2,1),
            2 : (1,3),5 :(1,2),8 :(1,1),0 :(1,0)
          }
    
    l_pos = [0,0]
    r_pos = [2,0]

    for n in numbers:
        next = phone[n]
        if next == 'B':
            l_dis = abs(l_pos[0]-pos[n][0]) + abs(l_pos[1]-pos[n][1])
            r_dis = abs(r_pos[0]-pos[n][0]) + abs(r_pos[1]-pos[n][1])
            
            if r_dis == l_dis:
                if hand=="right": next = 'R'
                else: next ='L'
            elif r_dis > l_dis:
                next = 'L'
            else: next = 'R'
        if next == 'L': l_pos = pos[n]
        else: r_pos = pos[n]
                
        answer += next
            
    return answer