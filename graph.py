import igraph
import countries as COS


countryDict = COS.countries()
countryKeys = countryDict.keys()
contiguousBorders = COS.contiguousBorders(countryDict)
waterRoutes = COS.waterRoutes(countryDict)


graph = igraph.Graph()
graph.add_vertices( len(countryDict) )

## Add vertex labels:
for key in countryKeys:
    graph.vs[countryDict[key]]['label'] = key
    graph.vs[countryDict[key]]['p_death'] = 4

## Add edges for borders and boats:
graph.add_edges( contiguousBorders )
graph.es[0:len(contiguousBorders)]["color"] = "yellow"
graph.add_edges( waterRoutes )

## Color countries by geographical region:
for vertexNumber in range(len(countryDict)):
    if graph.vs[vertexNumber]['label'] == 'Syria':
        graph.vs[vertexNumber]['color'] = 'red'
    elif graph.vs[vertexNumber]['label'] in COS.africaCountries():
        graph.vs[vertexNumber]['color'] = 'orange'
    elif graph.vs[vertexNumber]['label'] in COS.middleEastCountries():
        graph.vs[vertexNumber]['color'] = 'yellow' 
    elif graph.vs[vertexNumber]['label'] in COS.centralEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'blue' 
    elif graph.vs[vertexNumber]['label'] in COS.southernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'pink' 
    elif graph.vs[vertexNumber]['label'] in COS.westernEuropeCountries():
        graph.vs[vertexNumber]['color'] = 'purple' 
    elif graph.vs[vertexNumber]['label'] in COS.nordicCountries():
        graph.vs[vertexNumber]['color'] = 'green' 
    else:
        print 'WARNING: No color specified for: ',graph.vs[vertexNumber]['label']


graph.es['weight'] = range(0,40)

layout = graph.layout("auto")

visual_style = { "edge_width":6,
    "vertex_size": 95, 
    'bbox':(0, 0, 1300, 1300),
    'layout': layout,
    'margin': 68 }

#layout = graph.layout("kamada_kawai")

igraph.plot(graph, **visual_style)
