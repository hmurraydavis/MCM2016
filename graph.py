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
    

if __name__ == '__main__':
    costFuncCalculate( graph.es[50] )    
    print '\n'
    costFuncCalculate( graph.es[20] ) 
    
    for edge in graph.es :
        costFuncCalculate(edge)
    
    if 0: ## Edges
        for i in range(45):
            print graph.es[i]
    
    if 0: ## Vertexes:
        for i in range(30):
            print graph.vs[i]
        
    

igraph.plot(graph)#,  **visual_style)
