from functions import *
from random import randint


#read the entries.txt
archive = open('entries.txt', 'r')

coordenates = getCoordenates(archive.readlines())

#made this block to remove the repeat elements from the entry


coordenates = list(coordenates)


g= createGraph(coordenates)

res = AStarProcedure(g, coordenates)



#this function shift 1 element to create new tests
def shift_elements(lst, i):
    if not lst:
        return lst  # returns empty list
    else:
        x = lst[i]
        lst[i] = lst[0]
        lst[0] = x
        return lst



#test1
if len(coordenates) <= 10:
    for i in range(len(coordenates)):
        coord = coordenates.copy()
        coord = shift_elements(coordenates, i)
        print(coord)

        g = createGraph(coord)

        res = AStarProcedure(g, coord)

        print(res)
        print(generateResult(res, coord))
else:
    visited = []
    for i in range(len(coordenates)):
        number = randint(0,len(coordenates)-1)
        while number in visited:
            number = randint(0,len(coordenates)-1)

        coordenates = shift_elements(coordenates, number)
        print(coordenates)

        g = createGraph(coordenates)

        res = AStarProcedure(g, coordenates)

        print(res)
        print(generateResult(res, coordenates))





