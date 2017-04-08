def retornarsuma(n):
    if n/10 == 0:
        if n%2 == 0:
            return n
        else:
            return 0
    else:
        if (n%10)%2 == 0:
            return n%10+retornarsuma(n/10)
        else:
            return retornarsuma(n/10)








    
        
