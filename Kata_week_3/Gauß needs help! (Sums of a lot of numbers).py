def f(n):
    
    if isinstance(n, int) == True and n > 0:
        x = 0
        for i in range(0,n+1):
            x = x + i
        return x