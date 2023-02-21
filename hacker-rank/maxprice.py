
def robbery(cap,va,vb,wa,wb):
    
    
    N = 1e5
    ans = -1
    x = 0
    while (wa*x <= cap and x <=N):
        y = (cap-wa*x)/wb
        value = (va*x + vb*y)
        ans = max(ans,value)
        x+=1
        
    x = 0    
    while (wb*x <= cap and x <=N):
        y = (cap-wb*x)/wa
        value = (va*y + vb*x)
        ans = max (ans,value)
        x+=1
        
    return int(ans)
    
            

if __name__ == '__main__':
    cap = int(input())
    va = int(input())
    vb = int(input())
    wa = int(input())
    wb = int(input())
    ans = robbery(cap,va,vb,wa,wb)
    print(ans)

    