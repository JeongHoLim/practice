# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

def solution(places):
    answer = []
    
    def is_valid(x,y):
        if x<0 or x >4  or y> 4 or y <0: return False 
        return True
    
    def check(dirs,place,x,y):
        
        for i,j in dirs:
            if is_valid(x+i,y+j):
                if place[x+i][y+j] == 'P':
                    if abs(i)+abs(j) == 1:
                        return False
                    if i*j == 0:
                        if i==0:
                            j -= j//abs(j)
                        else:
                            i -= i//abs(i)
                        if place[x+i][y+j] != 'X': return False
                    else:
                        ni,nj = 0,j
                        if place[x+ni][y+nj] != 'X': return False
                        ni,nj = i,0            
                        if place[x+ni][y+nj] != 'X': return False
                        
        return True                
        
            
    def get_answer(place):
        dirs = [[-1,0],[-2,0],[-1,1],[0,1],[0,2],[1,1],
                [1,0],[2,0],[1,-1],[0,-1],[0,-2]]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not check(dirs,place,i,j):
                        return 0
        return 1
    
    for place in places:
        answer.append(get_answer(place))          
    
    return answer