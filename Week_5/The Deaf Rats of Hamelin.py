def count_deaf_rats(town):
    der = 0
    izq = 0
    town = town.replace(' ', '')
    print(town)
    ind = town.index("P")
    print(ind)
    izq = town[1:ind:2].count("~")
    der = town[8::2].count("O")
    return izq + der

    


