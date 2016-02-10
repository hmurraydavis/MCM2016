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

endPrioritization = 'HMDCost'
pathPrioritization = 'HMDCost'
print 'Begining. Prioritizing on ', pathPrioritization
print 'Land/water nope toggle...'

numFailures = 0
numTimesNoPath = 0

removeEdgeList = []
for edge in graph.es:
    if edge['TransitMethod'] != 'land':
#        print edge.index
        removeEdgeList.append( edge.index )
#        edgeID = graph.get_eid( edge['Source'], edge['Target'] )
#        print 'Deleting ', edge['SourceCo'], edge['TargetCo']
#        graph.delete_edges( edge )
#    else:
#        print edge
graph.delete_edges(removeEdgeList)
      
#removeVertexList = []

#for vertex in graph.vs:
#    if vertex['label'] == 'Morocco':
#        print graph.adjacent( vertex )
#    if len( graph.adjacent( vertex ) ) < 1:
##        graph.delete_vertices( vertex )
#        removeVertexList.append( vertex.index )
#graph.delete_vertices( removeVertexList )

#for vertex in graph.vs :
#    vertex["size"] = 8 
#layout = graph.layout("kk")    
#igraph.plot(graph)


    
def resourcesCalculate(vertex, update=True):
    ''' Validated by Jessie hand math.'''
    resources = ( vertex['GNI']* \
        (1 - vertex['Unemployment']) * \
        vertex['Education'] * \
        vertex['LifeExp'] * \
        vertex['GDPHealth'] ) * 10**(-7)
    if update==True:
        vertex['Resources'] = resources
    return resources



def costFuncMSIMCalculate(edge, update=True):
    ''' 
    Calculate the cost for a given edge using a heavily modified Spacial 
    Interaction Model ("Jessie" model).
    Option to automatically update the "Cost" attribute for the edge. 
    Default behavior.
    
    INPUT: edge : indivigual igraph edge object.
        *update : Boolian. If True, execution will update the Cost attribute 
        of the given edge.
    
    RETURNS: cost : The evaluated value of the cost function.
    '''
    source = edge['Source']
    target = edge['Target']
    
    ## Set land/sea toggle value
    if edge['TransitMethod']=='land': landval = 0.75
    elif edge['TransitMethod']=='sea': landval = 1
    else: print 'WARNING: No transit method defined for: ', edge
    
    
    if graph.vs[target]['NumRefs'] > graph.vs[target]['RefCap']:
        val = 0.00000001   
                 
        if update==True:
            edge['Cost'] = val
            edge['HMDCost'] = 10000/float(val)
        return val
    
    if edge['TargetCo'] in COS.endCountryList():
        ## Equation D case (end countries):
        pt1 = edge['Safety'] * \
            graph.vs[target]['SafetyCo'] * \
            graph.vs[target]['Resources'] * \
            graph.vs[target]['NumRefs'] * \
            graph.vs[target]['natPop'] * \
            landval
            
        
        
        den = edge['Distance']**.5 *\
            edge['MoneyCost'] * \
            graph.vs[source]['Resources'] *\
            graph.vs[source]['natPop'] * \
            graph.vs[source]['SafetyCo']
        
            
        endmult = 1 - \
            ( graph.vs[target]['NumRefs'] / \
            float( graph.vs[target]['RefCap'] ) )
        val = pt1 * endmult / den
        
        
        if graph.vs[target]['NumRefs'] > graph.vs[target]['RefCap']:
            val = 0.00000001   
                 
            if update==True:
                edge['Cost'] = val
                edge['HMDCost'] = 10000/float(val)
            return val       
            
        if update==True:
            edge['Cost'] = val
            edge['HMDCost'] = 10000/float(val)
        return val   
        
    elif edge['TargetCo'] in COS.transitionCoList():
        ## Equation C case (Transition countries):
        pt1 = edge['Safety'] * \
            graph.vs[target]['SafetyCo'] * \
            graph.vs[target]['Resources'] * \
            graph.vs[target]['NumRefs'] * \
            landval
        
        den = edge['Distance'] * \
            edge['MoneyCost'] * \
            resourcesCalculate( graph.vs[source], update=False ) * \
            graph.vs[source]['SafetyCo']
        
        endmult = 1 - \
            ( graph.vs[target]['NumRefs'] / \
            float( graph.vs[target]['RefCap'] ) )
            
        val = pt1 * endmult / den
#        
#        if graph.vs[target]['NumRefs'] > graph.vs[target]['RefCap']:
#            val = 0.00000001   
                 
        if update==True:
            edge['Cost'] = val
            if val < .0000001:
                edge['HMDCost'] = .0000001
            else: edge['HMDCost'] = 10000/float(val)
        return val
        

def pickEndCountry(metric):
    endCountries = COS.nordicCountries() + COS.westernEuropeCountries()
    endCoLabels = []
    endCoWeight = []
    for vertex in graph.vs:
        if vertex['label'] in endCountries:
#            print vertex
            endCoLabels.append(vertex['ID'])
#            endCoWeight.append( vertex[metric] )
#    print len(endCoLabels)
#    print len(endCoWeight)
    endCoWeight = [ i/sum(endCoWeight) for i in endCoWeight ]
    return np.random.choice(endCoLabels)#, p=endCoWeight)
    
    
def pickStartCountry():
    ## Move refs from all countries:
    if graph.vs[0]['NumRefs']<10000:
        coIDs = range( 38 )
        
        numRefsCos = []
        for coid in coIDs:
#            graph.vs[coid]['NumRefs']
            numRefsCos.append( graph.vs[coid]['NumRefs'] )
            

        originCoWeight = [ i/float(sum(numRefsCos)) for i in numRefsCos ]
            
    #    print originCoWeight
        return np.random.choice(coIDs, p=originCoWeight)
        
    ## Move Refs only from Origin and Transition countries    
    else:
        coList = COS.originCoList() + COS.transitionCoList()
        coIDs = []#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        numRefsCos = []
        for vertex in graph.vs:
            if vertex['label'] in coList:
                numRefsCos.append( vertex['NumRefs'] )
                coIDs.append( vertex.index )
#        for coid in coIDs:
#            graph.vs[coid]['NumRefs']
#            numRefsCos.append( graph.vs[coid]['NumRefs'] )
            
        originCoWeight = [ i/float(sum(numRefsCos)) for i in numRefsCos ]

    #    print originCoWeight
        return np.random.choice(coIDs, p=originCoWeight)




numRefsOverTime = {}
for vertex in graph.vs:
    numRefsOverTime[ vertex['label'] ] = [ vertex['NumRefs'] ]
    
print pickStartCountry()

for timeStep in range(7000000):
#        print 'TS: ', timeStep
#    try:
        ## Update graph properties:
        for vertex in graph.vs:
            numRefsOverTime[ vertex['label'] ].append( vertex['NumRefs'] )
        for vertex in graph.vs:
            resourcesCalculate(vertex)
        for edge in graph.es :
            #print edge
            costFuncMSIMCalculate(edge)

        

        
        desiredEndCo = pickEndCountry(endPrioritization)
#        print 'Des end: ', desiredEndCo
        startCo = pickStartCountry()
        
#    try:
        pathToEndCo = graph.get_shortest_paths(startCo, desiredEndCo, weights = pathPrioritization, output='vpath')[0]
    
        numStepsToMove = 1
        if len(pathToEndCo) >numStepsToMove:
    #        print pathToEndCo
            graph.vs[ pathToEndCo[0] ]['NumRefs'] = \
                    graph.vs[ pathToEndCo[0] ]['NumRefs'] - 300
            graph.vs[ pathToEndCo[1] ]['NumRefs'] = \
                    graph.vs[ pathToEndCo[1] ]['NumRefs'] + 300
#    except:
        numTimesNoPath = numTimesNoPath + 1
            
        if (timeStep % 10000)==0:
            for vertex in graph.vs :
                vertex["size"] = int( vertex['NumRefs']*.00012 )
            layout = graph.layout("kk")
            igraph.plot(graph, \
                'NoLandRoutes-prioritize-GraphT'+str(timeStep)+'.png', layout=layout )#,  **visual_style)
        

#    except: 
#        print 'Exception occured!'
#        print 'There was not a path ', numTimesNoPath, ' times.'
#        pickle.dump( numRefsOverTime, open( 'NoLandRoutes-'+pathPrioritization+".p", "wb" ) )
#        numFailures = numFailures + 1
#        if numFailures >20:
#            print 'Hi'
#            sys.exit('Too many failures occured to proceed. Ended at timestep: '+str(timeStep))


print 'There was not a path ', numTimesNoPath, ' times.'

for vertex in graph.vs :
    vertex["size"] = int( vertex['NumRefs']*.00012 )
layout = graph.layout("kk")
#igraph.plot(graph, \
#    'path-'+pathPrioritization+'--edge-'+endPrioritization+'Graph'+'.png', \
#    layout=layout )#,  **visual_style)

MCM_Graph.plotResultsFromList(numRefsOverTime, ['Syria', 'UK', 'France', 'Sweden', 'Spain'])



