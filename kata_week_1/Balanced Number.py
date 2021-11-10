def balanced_num(number):
        
    sum2 = str(number)
    sum2 = list(sum2)
    sum2 = list(map(int, sum2))
    
    if len(sum2) <= 2:
        return ("Balanced")
    else:
        
        if len(sum2) % 2 != 0:
            
            a=(((len(sum2)-1)/2)+1)
            a = int(a)
            b = sum(sum2[0:a-1])
            c = sum(sum2[a:len(sum2)])
            
            if c == b:
                return("Balanced")
            else:
                return("Not Balanced")


        elif len(sum2) % 2 == 0:
            a = len(sum2)/2
            a = int(a)
            b = sum(sum2[0:a-1])
            c = sum(sum2[a+1:len(sum2)])
            
            if c == b:
                return("Balanced")
            
            else: 
                return("Not Balanced")