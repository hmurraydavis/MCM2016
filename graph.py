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

## Add edges for borders and boats:
graph.add_edges( contiguousBorders )
graph.add_edges( waterRoutes )




layout = graph.layout("kamada_kawai")
igraph.plot(graph, layout = layout)
