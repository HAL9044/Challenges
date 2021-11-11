def balanced_num(number):
        
    #number string is first turned into a list of integers: 

    number_list = str(number)
    number_list = list(number_list)
    number_list = list(map(int, number_list))
    
    #If the amount if digits is less or equal to two, return balanced automaticaly 

    if len(number_list) <= 2:
        return ("Balanced")
    else:
        #check if the amount of digits is odd. Then find middle number, turn the resulting float into an int and use it to sum both sides. 
        if len(number_list) % 2 != 0:
            
            middle_number=(((len(number_list)-1)/2)+1)
            middle_number = int(middle_number)
            left_side = sum(number_list[0:middle_number-1])
            right_side = sum(number_list[middle_number:len(number_list)])
            
            if right_side == left_side:
                return("Balanced")
            else:
                return("Not Balanced")

        #check if number is even, if so, divides by 2 and sums both sides with two middle digits as 'dividers'. 
        elif len(number_list) % 2 == 0:
            middle_number = len(number_list)/2
            middle_number = int(middle_number)
            left_side = sum(number_list[0:middle_number-1])
            right_side = sum(number_list[middle_number+1:len(number_list)])
            
            if right_side == left_side:
                return("Balanced")
            
            else: 
                return("Not Balanced")

