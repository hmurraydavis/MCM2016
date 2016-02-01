import igraph
import countries as COS
import graph as MCM_Graph
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pprint
import tabulate
import math
import random
import pickle
import sys

## load pickeled iGraph 
graph = igraph.Graph()
graph = graph.Read_Pickle('MCM_Graph.p')

endPrioritization = 'Resources'
pathPrioritization = 'HMDCost'





def pickEndCountry(metric):
    endCountries = COS.endCountryList()
    endCoLabels = []
    endCoWeight = []
    for vertex in graph.vs:
        if vertex['label'] in endCountries:
#            print vertex
            endCoLabels.append(vertex['ID'])
            endCoWeight.append( vertex[metric] )
#    print len(endCoLabels)
#    print len(endCoWeight)
    endCoWeight = [ i/sum(endCoWeight) for i in endCoWeight ]
    return np.random.choice(endCoLabels, p=endCoWeight)
    
    
def pickStartCountry():
    ## Move refs from all countries:
    if graph.vs[0]['NumRefs']<10000:
        coIDs = range( 38 )
        
        numRefsCos = []
        for coid in coIDs:
#            graph.vs[coid]['NumRefs']
            numRefsCos.append( graph.vs[coid]['NumRefs'] )
            
        try:
            originCoWeight = [ i/float(sum(numRefsCos)) for i in numRefsCos ]
        except:
#            pickle.dump( numRefsOverTime, \
#                open( 'path-'+pathPrioritization+\
#                '--edge-'+endPrioritization+".p", "wb" ) )
            sys.exit("All the refugees have moved from the Origin and Transition countries!")
    #    print originCoWeight
        return np.random.choice(coIDs, p=originCoWeight)
        
    ## Move Refs only from Origin and Transition countries    
    else:
        coList = COS.originCoList() + COS.transitionCoList()
        coIDs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        numRefsCos = []
        for coid in coIDs:
#            graph.vs[coid]['NumRefs']
            numRefsCos.append( graph.vs[coid]['NumRefs'] )
            
        try:
            originCoWeight = [ i/float(sum(numRefsCos)) for i in numRefsCos ]
        except:
#            pickle.dump( numRefsOverTime, \
#                open( 'path-'+pathPrioritization+\
#                '--edge-'+endPrioritization+".p", "wb" ) )
            sys.exit("All the refugees have moved from the Origin and Transition countries!")
    #    print originCoWeight
        return np.random.choice(coIDs, p=originCoWeight)


numRefsOverTime = {}
for vertex in graph.vs:
    numRefsOverTime[ vertex['label'] ] = [ vertex['NumRefs'] ]
    
print pickStartCountry()

for timeStep in range(7000000):

    ## Update graph properties:
    for vertex in graph.vs:
        numRefsOverTime[ vertex['label'] ].append( vertex['NumRefs'] )
    for vertex in graph.vs:
        MCM_Graph.resourcesCalculate(vertex)
    for edge in graph.es :
        MCM_Graph.costFuncMSIMCalculate(edge)
        if ( edge['Source'] == 4 ) and (edge['Target'] == 10):
            print edge
            print MCM_Graph.costFuncMSIMCalculate(edge), '\n'
            print 'Hungry Regs: ', graph.vs[10]['NumRefs'], '  Out of ', graph.vs[10]['RefCap']
            

    

    
    desiredEndCo = pickEndCountry(endPrioritization)
    startCo = pickStartCountry()
    
##    adjacents = graph.adjacent( graph.vs[4] )
##    for edge in adjacents:
##        print graph.es[edge]
##    
##    print graph.vs[4]; print graph.vs[10]
#    for edge in graph.es: 
##        print edge
#        if edge['HMDCost'] <.1:
#            print edge
#            edge['HMDCost'] = .1
    pathToEndCo = graph.get_shortest_paths(startCo, desiredEndCo, weights = 'HMDCost', output='vpath')[0]
#    sys.exit()
    
    numStepsToMove = 1
    if len(pathToEndCo) >numStepsToMove:
#        print pathToEndCo
        graph.vs[ pathToEndCo[0] ]['NumRefs'] = graph.vs[ pathToEndCo[0] ]['NumRefs'] - 100
        graph.vs[ pathToEndCo[1] ]['NumRefs'] = graph.vs[ pathToEndCo[1] ]['NumRefs'] + 100
    if (timeStep % 10000)==0:
        for vertex in graph.vs :
            vertex["size"] = int( vertex['NumRefs']*.00012 )
        layout = graph.layout("kk")
        igraph.plot(graph, \
            'path-'+pathPrioritization+'--edge-'+endPrioritization+'GraphT'+str(timeStep)+'.png', \
            layout=layout )#,  **visual_style)
        

        
#    for vertex in graph.vs: 
#        MCM_Graph.selfCostMSIMcalculate(vertex)
        

pickle.dump( numRefsOverTime, open( 'path-'+pathPrioritization+'--edge-'+endPrioritization+".p", "wb" ) )


for vertex in graph.vs :
    vertex["size"] = int( vertex['NumRefs']*.00012 )
layout = graph.layout("kk")
#igraph.plot(graph, \
#    'path-'+pathPrioritization+'--edge-'+endPrioritization+'Graph'+'.png', \
#    layout=layout )#,  **visual_style)

MCM_Graph.plotResultsFromList(numRefsOverTime, ['Syria', 'UK', 'France', 'Sweden', 'Spain'])



