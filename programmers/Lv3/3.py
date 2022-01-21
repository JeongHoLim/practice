# https://programmers.co.kr/learn/courses/30/lessons/60059

from copy import deepcopy
def solution(key, lock):
    answer = False
    
    M,N = len(key),len(lock)
    
    my_lock = [[-1 for _ in range(N+2*M)] for _ in range(N+2*M)]
    
    for i in range(N):
        for j in range(N):
            my_lock[M+i][M+j] = lock[i][j]
    
    def is_open(my_lock,N,M):
        
        for i in range(N):
            for j in range(N):
                if my_lock[M+i][M+j] != 1: return False
        
        return True
        
    
    for _ in range(4):
        copy_key = [[] for _ in range(M)]
        for i in range(M):
            copy_key[i].extend([key[j][i] for j in range(M-1,-1,-1)])
        key = deepcopy(copy_key)
        for x in range(N+M):
            for y in range(N+M):
                copy_my_lock = deepcopy(my_lock)
                
                for i in range(M):
                    for j in range(M):
                        copy_my_lock[x+i][y+j] += key[i][j]                
                        
                if is_open(copy_my_lock,N,M):
                    return True        
                for i in range(M):
                    for j in range(M):
                        copy_my_lock[x+i][y+j] = my_lock[x+i][y+j]                
                
    return answer