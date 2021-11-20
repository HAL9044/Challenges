def triangle(row):
    lst = []
    
    
    for j in range(len(row)-1):
        for i in range(len(row)-1):
            
            aux = []
            
            if row[i] == row[i+1]:
                lst.append(row[i])
                
            elif row[i] != row[i+1]:
                aux.append(row[i])
                aux.append(row[i+1])
                
                if "G" in aux and "B" in aux:
                    lst.append("R")
                    
                elif "B" in aux and "R" in aux:
                    lst.append("G")
                    
                else:
                    lst.append("B")
        print(lst)
        row = lst
        lst = []
    return row[0]
