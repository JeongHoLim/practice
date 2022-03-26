N,L,K = list(map(int,input().split()))
easy = 100
hard = 140
easy_problem = []
hard_problem = []

for i in range(N):
    deg1,deg2 = list(map(int,input().split()))
    if deg2 <= L:
        hard_problem.append(i)
    elif deg1 <= L:
        easy_problem.append(i)

score = 0
if K <= len(hard_problem):
    score = hard*K
elif K > len(hard_problem):
    score += hard*len(hard_problem)
    K -= len(hard_problem)
    score += easy*min(K,len(easy_problem))
print(score)