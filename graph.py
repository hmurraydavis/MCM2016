import igraph
import countries as COS
#import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pprint


countryDict = COS.countries()
contiguousBorders = COS.contiguousBorders(countryDict)
waterRoutes = COS.waterRoutes(countryDict)
countryList = COS.coList()

numRefsOverTime = { country:[0] for country in countryList }


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
        graph.vs[vertexNumber]['NumRefs'] = 3000000
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
       
    ## Set Safety values for edges based on routes:        
    if ( (edge['TargetCo'] == 'Italy') or (edge['TargetCo'] == 'Malta') ) and ( edge['TransitMethod'] == 'sea' ):
        #Central Mediterranean routes
        edge['Safety'] = 0.3
        edge['MoneyCost'] = 0.8
    elif ( (edge['TargetCo'] == 'Spain') or (edge['TargetCo'] == 'France') ) and ( edge['TransitMethod'] == 'sea' ):
        #Western Mediterranean routes
        edge['Safety'] = 0.4
        edge['MoneyCost'] = 1.0
    elif ( (edge['TargetCo'] == 'Greece') ) and ( edge['TransitMethod'] == 'sea' ):
        #Eastern Mediterranean routes
        edge['Safety'] = 0.8
        edge['MoneyCost'] = 0.6
    elif ( (edge['TargetCo'] in COS.middleEastCountries() ) ) and ( edge['TransitMethod'] == 'land' ):
        #Middle East land routes
        edge['Safety'] = 0.7
        edge['MoneyCost'] = 0.2
    elif ( (edge['TargetCo'] in COS.africaCountries() ) ) and ( edge['TransitMethod'] == 'land' ):
        #Northern Africa land routes
        edge['Safety'] = 0.9
        edge['MoneyCost'] = 0.2
    elif ( (edge['TargetCo'] in COS.centralEuropeCountries() ) ) and ( edge['TransitMethod'] == 'land' ):
        #Eastern Europe land routes
        edge['Safety'] = 0.9
        edge['MoneyCost'] = 0.2
    elif ( (edge['TargetCo'] in COS.southernEuropeCountries() ) ) and ( edge['TransitMethod'] == 'land' ):
        #Southern Europe land routes
        edge['Safety'] = 0.9
        edge['MoneyCost'] = 0.2
    elif ( (edge['TargetCo'] in COS.nordicCountries() ) ):
        #Nordic Country routes
        edge['Safety'] = 1.0
        edge['MoneyCost'] = 0.5
    elif ( (edge['TargetCo'] in COS.westernEuropeCountries() ) ):
        #Western Europe routes
        edge['Safety'] = 1.0
        edge['MoneyCost'] = 0.5
    else:
        print 'WARNING: Unspecified edge safety for: ', edge
        


## Place vertex properties on verticies:
nativePopulation = COS.nativePopulationCountries()
refugeeApplications = COS.refugeeApplicationsCountries()
safetyCountries = COS.safetyCountries()
gniCountries = COS.gniPerCapitaCountries()
unemploymentCountries = COS.unemploymentCountries()
for country in countryList:
    graph.vs[countryDict[country]]['natPop'] = nativePopulation[country] 
    graph.vs[countryDict[country]]['refApps'] = refugeeApplications[country] 
    graph.vs[countryDict[country]]['SafetyCo'] = safetyCountries[country] 
    graph.vs[countryDict[country]]['GNI'] = gniCountries[country] 
    graph.vs[countryDict[country]]['Unemployment'] = unemploymentCountries[country] 

    
for vertexNumIndex in range( len(graph.vs) ):
    numRefsOverTime[ graph.vs[vertexNumIndex]['label'] ] = [ graph.vs[vertexNumIndex]['NumRefs'] ]



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
    
def popFlowCalculate(edge, update=True):
    ''' 
    Calculate the flow of refugees along a given edge.
    Option to automatically update the "PopFlow" attribute for the edge. Default behavior.
    
    INPUT: edge : indivigual igraph edge object.
        *update : Boolian. If True, execution will update the "PopFlow" attribute of the given edge.
    
    RETURNS: popFlow : The number of refugees flowing along an edge.
    '''
    source = edge['Source']
    target = edge['Target']  
    
    costSelf = graph.vs[source]['CostSelf']
    
    
    adjacents = graph.adjacent( graph.vs[source] )
    
    costs = [ graph.es[i]['Cost'] for i in adjacents]
    
    frac = edge['Cost']/(sum(costs)+costSelf)
    popFlow = graph.vs[source]['NumRefs'] * frac
    #print popFlow, 'refugees from: ', edge['SourceCo'], ' to ', edge['TargetCo']
    if update == True:
        edge['PopFlow'] = popFlow
    #print 'Self Cost: ', graph.vs[source]['CostSelf']
    return popFlow

    
    

if __name__ == '__main__':
    timeStep = 0

    ## Simulate n time units through model: 
    for timeStep in range(90):
        ## Update self cost function on each vertex:
        graph.vs['CostSelf'] = [ (i**2)/.15 for i in graph.vs['natPop'] ] 
        
        
        for edge in graph.es :
            costFuncCalculate(edge)
            popFlowCalculate(edge)
            
        for edge in graph.es :
            popFlow = edge['PopFlow']
            source = edge['Source']
            target = edge['Target'] 
                
            graph.vs[target]['NumRefs'] = graph.vs[target]['NumRefs'] + popFlow
            graph.vs[source]['NumRefs'] = graph.vs[source]['NumRefs'] - popFlow

        
        for vertexNumIndex in range( len(graph.vs) ):
                numRefsOverTime[ graph.vs[vertexNumIndex]['label'] ].append( graph.vs[vertexNumIndex]['NumRefs'] )

        
    hijessie = numRefsOverTime.keys()   
    pprint.pprint( zip( numRefsOverTime.keys(), [numRefsOverTime[co][0] for co in hijessie] ) )
    #print( numRefsOverTime )


    plotList = ['Sweden','Italy', 'Greece', 'France', 'Germany', 'UK', 'Syria']#['Turkey', 'Serbia', 'Hungary', 'Poland', 'Austria', 'France', 'UK']#['Algeria', 'Greece', 'Italy', 'Germany', 'Sweden', 'UK', 'Portugal']#['Sweden','Norway','Finland' ,'Italy', 'Austria', 'Greece', 'Syria','Poland', 'France', 'Germany', 'UK', 'Portugal']
    for country in plotList:
        plt.plot(numRefsOverTime[country], linewidth=6, alpha=.75, label=country) 
#    plt.plot(numRefsOverTime['Syria'], linewidth=25, alpha=.9, color='#2F4172', label='Syria' ) 
#    plt.plot(numRefsOverTime['Norway'],  linewidth=11, alpha=.8, color='#2C8437', label='Norway' ) 
#    plt.plot(numRefsOverTime['Finland'], linewidth=3, alpha=1, color='#AA6E39', label='Finland' ) 
    plt.xlabel('Time', fontsize = 18)
    plt.ylabel('Number of Refugees', fontsize = 18)
    plt.suptitle('Diaspora over Time', fontsize = 20)
    plt.title('cost function: '+r'$\frac{pop_S * pop_T}{dist}$', y=.9,fontsize = 15)
    plt.legend()
    #plt.show()
    
#    historicalNumOfRefugees = []
#    numRefs = 0
#    for timestep in range( len( numRefsOverTime[country] ) ):
#        for country in countryList:
#            numRefs = numRefs + numRefsOverTime[country][timeStep]
#            #print 'no refs: ', numRefs
#        
#        historicalNumOfRefugees.append(numRefs)
#        numRefs = 0
#    #print 'hist: ',historicalNumOfRefugees
    
    if 0:
        plt.plot(historicalNumOfRefugees)
        plt.show()
        
            #print len( numRefsOverTime[country] )
    
    
    
    if 0: ## Edges
        for i in range(45):
            print graph.es[i]
    
    if 1: ## Vertexes:
        for i in range(30):
            print graph.vs[i]
        
for vertex in graph.vs :
    vertex["size"] = int( vertex['SafetyCo']*26 )

#for edge in graph.es:
#    edge['width'] = edge['MoneyCost']*10
#    edge['name'] = str( edge['MoneyCost'] )
    
layout = graph.layout("kk")
igraph.plot(graph, layout=layout )#,  **visual_style)
