import igraph
import countries as COS
import pprint


countryDict = COS.countries()
contiguousBorders = COS.contiguousBorders(countryDict)
waterRoutes = COS.waterRoutes(countryDict)
countryList = COS.coList()


graph = igraph.Graph(vertex_attrs={"label": countryList}, edges=contiguousBorders, directed=True)
for i, edge in enumerate( graph.es ):
    edge['Source']=contiguousBorders[i][0]
    edge['SourceCo']=countryList[ contiguousBorders[i][0] ]
    edge['Target']=contiguousBorders[i][1]
    edge['TargetCo']=countryList[ contiguousBorders[i][1] ]
    edge['TransitMethod']='land'




### Add edges for boats:
graph.es[0:len(contiguousBorders)]["color"] = "yellow"
for edge in waterRoutes:
    source, target = edge
    kwds = {'Source':source,
        'Target':target,
        'TargetCo':countryList[target],
        'SourceCo':countryList[source],
        'TransitMethod':'sea' }
    graph.add_edge( source, target, **kwds )
    
graph.vs['label_size'] = 8 ## Set fount size
graph.vs['shape'] = 'circle'

## Color countries by geographical region:
vertexOpacity = .5
for vertexNumber in range(len(countryDict)):
    if graph.vs[vertexNumber]['label'] == 'Syria':
        graph.vs[vertexNumber]['color'] = 'rgba(78,0,18, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 3000000000
    elif graph.vs[vertexNumber]['label'] in COS.africaCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(156, 52, 76, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 5000
    elif graph.vs[vertexNumber]['label'] in COS.middleEastCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(170, 95, 57, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 5000
    elif graph.vs[vertexNumber]['label'] in COS.centralEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(0,0,100, '+str(vertexOpacity)+')' 
        graph.vs[vertexNumber]['NumRefs'] = 6000
    elif graph.vs[vertexNumber]['label'] in COS.southernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(38, 113, 88, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 3000
    elif graph.vs[vertexNumber]['label'] in COS.westernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(87,49,50, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 3000
    elif graph.vs[vertexNumber]['label'] in COS.nordicCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(0,57,38, '+str(vertexOpacity)+')'
        graph.vs[vertexNumber]['NumRefs'] = 3000
    else:
        print 'WARNING: No color specified for: ',graph.vs[vertexNumber]['label']



    

## Place edge properties on edges
countryDistances = COS.distanceBetweenCountries()
for edge in graph.es:
    edge['Cost'] = 1 ## Initialize each edge w/ cost function
    for xCo in countryList:
        for yCo in countryList:
            if (edge['SourceCo']==xCo) and (edge['TargetCo']==yCo):
                edge['Distance'] = countryDistances[(countryDict[xCo],countryDict[yCo])]


nativePopulation = COS.nativePopulationCountries()
for country in countryList:
    graph.vs[countryDict[country]]['natPop'] = nativePopulation[country]
    

#layout = graph.layout("auto")

#graph = graph.as_directed()
#visual_style = { "edge_width":6,
#    'edge_arrow_size':.2,
#    'edge_arrow_width':.2,
#    "vertex_size": 255, 
#    'bbox':(0, 0, 3300, 3300),
#    'layout': layout,
#    'margin': 168 }

##layout = graph.layout("kamada_kawai")

#print graph.vs[4], '\n'

def costFuncCalculate(edge, update=True):
    ''' 
    Calculate the cost for a given edge.
    Option to automatically update the "Cost" attribute for the edge. Default behavior.
    
    INPUT: edge : indivigual igraph edge object.
        *update : Boolian. If True, execution will update the Cost attribute of the given edge.
    
    RETURNS: cost : The evaluated value of the cost function.
    '''
    source = edge['Source']
    target = edge['Target']

    popS = graph.vs[source]['natPop']
    popT = graph.vs[target]['natPop']
    dist = edge['Distance']
    
    cost = popS * popT / dist
    
    if update:
        edge['Cost'] = cost
    return cost
    
def popFlowCalculate(edge):
    source = edge['Source']
    target = edge['Target']  
    
    costSelf = 1.0#graph.vs[source]['CostSelf']  ##CostSelf
    print 'Country is: ', edge['SourceCo']
    print 'Self cost: ', costSelf
    
    adjacents = graph.adjacent( graph.vs[source] )
    
    costs = [ graph.es[i]['Cost'] for i in adjacents]
    adjNames = [ graph.es[i]['TargetCo'] for i in adjacents]
    print 'adj: ', zip(adjNames, costs)
    
    frac = edge['Cost']/(sum(costs)+costSelf)

    print 'frac: ', frac
    print 'chilling refs: ', graph.vs[source]['NumRefs']
    popFlow = graph.vs[source]['NumRefs'] * frac
    
    print 'numerator cost: ', edge['Cost']
    print 'pop flow: ', popFlow
    
#    for index in adjacents:
#        print index, graph.es[index]['Cost']
    
    

if __name__ == '__main__':
    
    ## Update self cost functions (cost function for staying 
    ## in the same place) For every vertex in the graph:
    graph.vs['CostSelf'] = [ (i**2)/.15 for i in graph.vs['natPop'] ]
    
    
    #costFuncCalculate( graph.es[50] )    
    #print '\n'
#    popFlowCalculate( graph.es[20] ) 
    
    for edge in graph.es :
        #costFuncCalculate(edge)
        popFlowCalculate(edge)
    
    if 0: ## Edges
        for i in range(45):
            print graph.es[i]
    
    if 0: ## Vertexes:
        for i in range(30):
            print graph.vs[i]
        
    

igraph.plot(graph)#,  **visual_style)
