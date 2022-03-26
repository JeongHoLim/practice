t = int(input())

def zero(n,idx,eq):
    
    if idx == n:
        value = eval(eq.replace(" ",""))
        if value == 0:
            print(eq)
        return

    for op in [" ","+","-"]:
        zero(n,idx+1,eq+op+str(idx+1))
        

for i in range(t):
    n = int(input())
    if i>0: print()
    zero(n,1,"1")