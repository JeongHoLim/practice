# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3#

def solution(rows, columns, queries):
    answer = []
    
    def rotate(x1,y1,x2,y2,matrix):
        p = matrix[x1-1][y1-1]
        ret = p
        for y in range(y1,y2):
            n = matrix[x1-1][y]
            matrix[x1-1][y] = p
            p = n
            ret = min(ret,p)
        
        for x in range(x1,x2):
            n = matrix[x][y2-1]
            matrix[x][y2-1] = p
            p = n
            ret = min(ret,p)
        
        for y in range(y2-1,y1,-1):
            n = matrix[x2-1][y-1]
            matrix[x2-1][y-1] = p
            p = n
            ret = min(ret,p)
        for x in range(x2,x1-1,-1):
            n = matrix[x-1][y1-1]
            matrix[x-1][y1-1] = p
            p = n
            ret = min(ret,p)
        
        return ret
            
    matrix = [[i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    
        
    for query in queries:
        answer.append(rotate(*query,matrix))
    
    return answer