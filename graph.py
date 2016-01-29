import igraph
import countries as COS


countryDict = COS.countries()
countryKeys = countryDict.keys()
contiguousBorders = COS.contiguousBorders(countryDict)
waterRoutes = COS.waterRoutes(countryDict)


graph = igraph.Graph()
## graph.is_directed()
graph.add_vertices( len(countryDict) )

## Add vertex labels:
for key in countryKeys:
    graph.vs[countryDict[key]]['label'] = key
    graph.vs[countryDict[key]]['p_death'] = 4

graph.vs['label_size'] = 45 ## Set fount size
graph.vs['shape'] = 'circle'

## Add edges for borders and boats:
graph.add_edges( contiguousBorders )
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


graph.es['weight'] = range(0,40)
#graph.es['edge_arrow_size'] = .2
#graph.es['edge_arrow_width'] = .2

layout = graph.layout("auto")

graph = graph.as_directed()
visual_style = { "edge_width":6,
#    'edge_arrow_size':.2,
#    'edge_arrow_width':.2,
    "vertex_size": 255, 
    'bbox':(0, 0, 3300, 3300),
    'layout': layout,
    'margin': 168 }

#layout = graph.layout("kamada_kawai")
#graph.es[4].draw_directed_edge()

igraph.plot(graph,  **visual_style)
