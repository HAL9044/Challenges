def count_deaf_rats(town):
    der = 0
    izq = 0
    town = town.replace(' ', '')
    ind = town.index("P")
    izq = town[1:ind:2].count("~")
    der = town[ind::2].count("O")
    return izq + der
