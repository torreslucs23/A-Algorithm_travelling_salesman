from math import sqrt
from random import shuffle
from random import randint
import math
import heapq



# calculate the euclidian distance
def calculateDistance(p1,p2):
    return round(float(sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)),4)

#get the coordenates of txt
def getCoordenates(entry):
    xString = entry[0].split(' ')
    yString = entry[1].split(' ')
    coordenates = []
    for i in range(0, len(xString)):
        x = float(xString[i])
        y = float(yString[i])
        coordenates.append((x,y))
    return coordenates

#aplies the operator 1
def operator1(positions, id1, id2):
    x = positions[id1]
    positions[id1] = positions[id2]
    positions[id2] = x
    return positions

#aplies the operator 2
def operator2(positions, id1, id2):
    new_positions = []
    for i in range(id1):
        new_positions.append(positions[i])
    for i in range(id2, id1-1, -1):
        new_positions.append(positions[i])
    for i in range(id2+1, len(positions)):
        new_positions.append(positions[i])
    
    return new_positions


#calculate the cost of a sequence
def calculateCost(sequence):
    cost = 0
    for i in range(len(sequence)):
        if i == len(sequence) -1:
            cost += calculateDistance(sequence[i], sequence[0])
            break
        cost += calculateDistance(sequence[i], sequence[i+1])
    return cost

#this function make a list with random indexes permutations to not repeat in the variations 
def generatePermutations(coordenates):
    permut = []
    for i in range(len(coordenates)):
        for w in range(i, len(coordenates)):
            permut.append((i,w))
    shuffle(permut)
    return permut


def minimum_spanning_tree_prim(points):
    # Create a set to store visited vertices
    visited = set()

    # Choose an arbitrary starting point
    initial_point = points[0]

    # Initialize the priority queue with edges from the starting point
    edges = [(calculateDistance(initial_point, point), initial_point, point) for point in points[1:]]
    heapq.heapify(edges)

    # Add the initial point to the set of visited points
    visited.add(initial_point)

    # Initialize the minimum spanning tree
    minimum_spanning_tree = []

    while edges:
        distance, origin, destination = heapq.heappop(edges)

        if destination not in visited:
            visited.add(destination)
            minimum_spanning_tree.append((origin, destination, distance))

            for point in points:
                if point not in visited:
                    new_distance = calculateDistance(destination, point)
                    heapq.heappush(edges, (new_distance, destination, point))

    return minimum_spanning_tree

point_list = [(0, 0), (1, 2), (2, 2)]
minimum_spanning_tree = minimum_spanning_tree_prim(point_list)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)