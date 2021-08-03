from .graph import *

def graph_business_trip(graph,inlist):
    cost = 0
    result = False
    for n in range(len(inlist)-1    ):
        neighbors = graph.get_neighbors(inlist[n])
        for neib in neighbors:
            if neib.node == inlist[n+1]:
                cost += neib.weight
                result = True
                
                    

    return f'{result} , ${cost}'               




   
