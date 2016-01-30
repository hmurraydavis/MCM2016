import igraph
import countries as COS
import pprint


countryDict = COS.countries()
contiguousBorders = COS.contiguousBorders(countryDict)
waterRoutes = COS.waterRoutes(countryDict)
countryList = COS.coList()


graph = igraph.Graph(vertex_attrs={"label": countryList}, edges=contiguousBorders, directed=True)
for i, edge in enumerate( graph.es ):
    edge['source']=contiguousBorders[i][0]
    edge['sourceCo']=countryList[ contiguousBorders[i][0] ]
    edge['target']=contiguousBorders[i][1]
    edge['targetCo']=countryList[ contiguousBorders[i][1] ]
    edge['transitMethod']='land'


graph.vs['label_size'] = 8 ## Set fount size
graph.vs['shape'] = 'circle'

### Add edges for boats:
graph.es[0:len(contiguousBorders)]["color"] = "yellow"
graph.add_edges( waterRoutes )

## Color countries by geographical region:
vertexOpacity = .5
for vertexNumber in range(len(countryDict)):
    if graph.vs[vertexNumber]['label'] == 'Syria':
        graph.vs[vertexNumber]['color'] = 'rgba(78,0,18, '+str(vertexOpacity)+')'
    elif graph.vs[vertexNumber]['label'] in COS.africaCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(156, 52, 76, '+str(vertexOpacity)+')'
    elif graph.vs[vertexNumber]['label'] in COS.middleEastCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(170, 95, 57, '+str(vertexOpacity)+')'
    elif graph.vs[vertexNumber]['label'] in COS.centralEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(0,0,100, '+str(vertexOpacity)+')' 
    elif graph.vs[vertexNumber]['label'] in COS.southernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(38, 113, 88, '+str(vertexOpacity)+')'
    elif graph.vs[vertexNumber]['label'] in COS.westernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(87,49,50, '+str(vertexOpacity)+')'
    elif graph.vs[vertexNumber]['label'] in COS.nordicCountries():
        graph.vs[vertexNumber]['color'] = 'rgba(0,57,38, '+str(vertexOpacity)+')'
    else:
        print 'WARNING: No color specified for: ',graph.vs[vertexNumber]['label']

print graph.es.select(_source=1)[0]
## Specify if it's a land or sea route: 
for vertex in waterRoutes:
    #print graph.es['source']#.attributes()
    graph.es[vertex]['transitMethod']='sea'
    

## Place edge properties on edges
countryDistances = COS.distanceBetweenCountries()
for i, xCo in enumerate(countryList):
    for j, yCo in enumerate(countryList):
        vertex = (countryDict[xCo], countryDict[yCo])
#        prior = graph.es[vertex]['transitMethod']
        if (vertex in waterRoutes):
            try:
                graph.es[vertex]['distance'] = countryDistances[vertex]
#                graph.es[vertex]['transitMethod'] = 'sea'+str(i)+' '+str(j)+xCo+yCo
            except: 
                print 'WARNING: Vertex: ', \
                    vertex, ' describing: ', \
                    xCo, yCo, ' does not exist'
        elif (vertex in contiguousBorders): 
            try:
                    graph.es[vertex]['distance'] = countryDistances[vertex]
#                    graph.es[vertex]['transitMethod'] = 'land'+str(i)+' '+str(j)+xCo+yCo
            except: 
                print 'WARNING: Vertex: ', \
                    vertex, ' describing: ', \
                    xCo, yCo, ' does not exist'
#        print prior, graph.es[vertex]['transitMethod']

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

print graph.vs[4], '\n'

igraph.plot(graph)#,  **visual_style)
