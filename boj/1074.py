n,r,c = list(map(int,input().split()))

def z(n,r,c,sx,sy,ex,ey,cost):

    if n == 1:
        return cost + (r-sx)*2 + c-sy
    else:
        cx,cy = (ex-sx+1)//2 + sx ,(ey-sy+1)//2 + sy
        if r < cx and c < cy: #1
            return z(n-1,r,c,sx,sy,cx-1,cy-1,cost)
        elif r < cx and c >= cy: #2
            return z(n-1,r,c,sx,cy,cx-1,ey,cost+ 4**(n-1))
        elif r >= cx and c < cy: #3
            return z(n-1,r,c,cx,sy,ex,cy-1,cost+ 4**(n-1) * 2)
        else: #4
            return z(n-1,r,c,cx,cy,ex,ey,cost+4**(n-1) * 3)


    

print(z(n,r,c,0,0,2**n-1,2**n-1,0))