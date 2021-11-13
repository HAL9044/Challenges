import numpy as np
def sum_or_product(list, n):
    

    list.sort() #sort the list in order to operate
    suma = sum(list[-n:len(list)]) #sum biggest numbers starting from the end of the list
    product = np.prod(list[n]) #multiply smallest numbers from the start of the list

    #check whether sum is bigger or smaller than product, and return accordingly 
    
    if suma > product:
        return "sum"
    elif suma < product:
        return "product"
    else:
        return "same"
