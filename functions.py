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

    acc = 0

    while edges:
        distance, origin, destination = heapq.heappop(edges)

        acc+=distance

        if destination not in visited:
            visited.add(destination)
            minimum_spanning_tree.append((origin, destination, distance))

            for point in points:
                if point not in visited:
                    new_distance = calculateDistance(destination, point)
                    heapq.heappush(edges, (new_distance, destination, point))

    return acc

#this function create a completed graph represented as hash map
def createGraph(coordenates):
    g = {i:[] for i in range(len(coordenates))}
    
    for i in range(len(coordenates)):
        for w in range(len(coordenates)):
            if i == w:
                continue
            g[i].append((calculateDistance(coordenates[i], coordenates[w]), w))
    return g


def h_calc(node, g, unvisited_nodes, cost_mst):

    nearest = float('inf')
    for city in unvisited_nodes:
        for distance, neighbor in g[node]:
            if neighbor == city:
                nearest = distance
    return nearest + cost_mst

def AStarProcedure(g, coord):
    heap = [(0, 0, [])] #this is the initial distance, node and the path
    visited = set() # i made this function to take all the nodes visited. This is a set in python, where do no repeat elements

    while heap:
        #this pop the priority element from priority queue
        cost, current_node, cities = heapq.heappop(heap)
        

        #checks if the node has been visited and skip
        if current_node in visited:
            continue


        cities.append(current_node)
        visited.add(current_node)
        
        if(len(cities) == len(g)):
            cities.append(0)
            return cities
        
        unvisited_nodes = set([i for i in range(len(g))]) - visited
        unvisited_nodes.add(0)

        subgraph = [coord[i] for i in unvisited_nodes]
        min_mst = minimum_spanning_tree_prim(subgraph)

        for distance, neighbor in g[current_node]:
            if neighbor not in visited:
                value_h = h_calc(neighbor, g, unvisited_nodes, min_mst)
                heapq.heappush(heap, (distance+value_h, neighbor, cities[:]))
    return None


def generateResult(points, coord):
    acc = 0
    for i in range(len(coord)):
        acc+=calculateDistance(coord[points[i]], coord[points[i+1]])
    return acc

#