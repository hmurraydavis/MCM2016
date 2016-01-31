import igraph
import countries as COS
#import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pprint
import tabulate
import math


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
lifeExpectanciesCountries = COS.lifeExpCountries()
educationCountries = COS.educationCountries()
healthCountries = COS.healthCountries()
healthGDPCountries = COS.healthGDPCountries()
for country in countryList:
    graph.vs[countryDict[country]]['natPop'] = nativePopulation[country] 
    graph.vs[countryDict[country]]['refApps'] = refugeeApplications[country] 
    graph.vs[countryDict[country]]['SafetyCo'] = safetyCountries[country] 
    graph.vs[countryDict[country]]['GNI'] = gniCountries[country] 
    graph.vs[countryDict[country]]['Unemployment'] = unemploymentCountries[country]
    graph.vs[countryDict[country]]['LifeExp'] = lifeExpectanciesCountries[country] 
    graph.vs[countryDict[country]]['Education'] = educationCountries[country] 
    graph.vs[countryDict[country]]['Health'] = healthCountries[country] 
    graph.vs[countryDict[country]]['GDPHealth'] = healthGDPCountries[country] 
    graph.vs[countryDict[country]]['RefCap'] = graph.vs[countryDict[country]]['natPop']/1000 ## TODO: Replace with actual refugee quotas!!
    

    



def costFuncGravityCalculate(edge, update=True):
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
    if edge['TransitMethod']=='land': landval = 1.0
    elif edge['TransitMethod']=='sea': landval = 0.75 
    else: print 'WARNING: No transit method defined for: ', edge
    
    if edge['TargetCo'] in COS.endCountryList():
        ## Equation D case (end countries):
        pt1 = edge['Safety'] * \
            graph.vs[target]['SafetyCo'] * \
            graph.vs[target]['Resources'] * \
            graph.vs[target]['NumRefs'] * \
            graph.vs[target]['natPop'] * \
            landval
            
        
        
        den = ( math.log( edge['Distance'] ) + 2 ) * \
            edge['MoneyCost'] * \
            graph.vs[source]['Resources'] *\
            graph.vs[source]['natPop'] * \
            graph.vs[source]['SafetyCo']
        
            
        endmult = 1 - \
            ( graph.vs[target]['NumRefs'] / \
            float( graph.vs[target]['RefCap'] ) )
        val = pt1 * endmult / den
        edge['Cost'] = val
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
        edge['Cost'] = val
        return val
            
            
            
    
    
    
    
    
    
    
    
    
        
    
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
    
#    print 'costs denom: ', (sum(costs)+costSelf), '\n', graph.vs[source]
    frac = edge['Cost']/(sum(costs)+costSelf)
    popFlow = graph.vs[source]['NumRefs'] * frac
    #print popFlow, 'refugees from: ', edge['SourceCo'], ' to ', edge['TargetCo']
    if update == True:
        edge['PopFlow'] = popFlow
    #print 'Self Cost: ', graph.vs[source]['CostSelf']
    return popFlow
    
    
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

def selfCostMSIMcalculate(vertex, update=True):
    if vertex['label'] in COS.originCoList():
        cost = .3
    else: 
        n1 = 2 * vertex['SafetyCo'] * \
            vertex['Resources'] * \
            vertex['NumRefs']**2
        
        adjacents = graph.adjacent( target ) #returns edge labels
        
        adjTargets = graph.vs[ graph.es[adjacents]['Target'] ]

        
        ## Do the weird pi cumulitive product thing:     
        distProd = 1
        for distance in graph.es[adjacents]['Distance']:
            distProd = distProd * distance
            
        lnPi = math.log(distProd)
        
        numeratorMoneySigma = sum( graph.es[adjacents]['MoneyCost'] )
        denomSafetySigma = sum( graph.es[adjacents]['Safety'] ) + \
            sum( adjTargets['SafetyCo'] )

        denomResourceSigma = sum( adjTargets['Resources'] )
        
        cost = n1 * distProd * numeratorMoneySigma / \
            vertex['RefCap'] / denomSafetySigma / denomResourceSigma
    if update==True:
        vertex['CostSelf'] = cost
    return cost
    
    
##Depricated gravity cost function:
#graph.vs['CostSelf'] = [ (i**2)/.15 for i in graph.vs['natPop'] ]             


def updateRefugeePopulations(edge):
    popFlow = edge['PopFlow']
    source = edge['Source']
    target = edge['Target'] 
        
    graph.vs[target]['NumRefs'] = graph.vs[target]['NumRefs'] + popFlow
    graph.vs[source]['NumRefs'] = graph.vs[source]['NumRefs'] - popFlow


def runModel(timeSpan):
    numRefsOverTime = { country:[0] for country in countryList }
    costSelfOverTime = { country:[0] for country in countryList }
    resourcesOverTime = { country:[0] for country in countryList }
    
    for vertexNumIndex in range( len(graph.vs) ):
        numRefsOverTime[ graph.vs[vertexNumIndex]['label'] ] = [ graph.vs[vertexNumIndex]['NumRefs'] ]
        costSelfOverTime[ graph.vs[vertexNumIndex]['label'] ] = [ graph.vs[vertexNumIndex]['CostSelf'] ] 
        resourcesOverTime[ graph.vs[vertexNumIndex]['label'] ] = [ graph.vs[vertexNumIndex]['Resources'] ]   
    
    ## Simulate n time units through model: 
    for timeStep in range(timeSpan):
        ## Update self cost function on each vertex:
        for vertex in graph.vs: selfCostMSIMcalculate(vertex)
        
        for vertex in graph.vs:
            resourcesCalculate(vertex)
        
        
        for edge in graph.es :
            costFuncMSIMCalculate(edge)
            #costFuncGravityCalculate(edge)
            popFlowCalculate(edge)
            
        for edge in graph.es :
            updateRefugeePopulations(edge)
            
        for vertex in graph.vs:
            resourcesCalculate(vertex)
            

        
        for vertexNumIndex in range( len(graph.vs) ):
                numRefsOverTime[ graph.vs[vertexNumIndex]['label'] ].append( graph.vs[vertexNumIndex]['NumRefs'] )
                costSelfOverTime[ graph.vs[vertexNumIndex]['label'] ].append( graph.vs[vertexNumIndex]['CostSelf'] )
                resourcesOverTime[ graph.vs[vertexNumIndex]['label'] ].append( graph.vs[vertexNumIndex]['Resources'] )

        
    #hijessie = numRefsOverTime.keys()   
    #pprint.pprint( zip( numRefsOverTime.keys(), [numRefsOverTime[co][0] for co in hijessie] ) )
    #print( numRefsOverTime )
    return {'NumRefs':numRefsOverTime, 
        'CostSelf':costSelfOverTime, 
        'Resources':resourcesOverTime}
        



def plotResultsFromList(resultsDict, plotList, label=''):
    for country in plotList:
        plt.plot(resultsDict[country], linewidth=6, alpha=.55, label=country) 
    plt.xlabel('Time', fontsize = 18)
    plt.ylabel('Number of Refugees', fontsize = 18)
    plt.suptitle('Diaspora over Time', fontsize = 20)
    plt.title(label, y=1,fontsize = 15)
    plt.legend()
    plt.show()

## Finish instanciating graph:
#Set resources on vertexes
for vertex in graph.vs:
    resourcesCalculate(vertex)
    
#Set cost function on vertexes (cost function depends on resources 
#being throughout)the graph, so it needs to be run after calling 
#resourcesCalculate(vertex) on the whole graph!!:
for vertex in graph.vs:
    selfCostMSIMcalculate(vertex)

    

if __name__ == '__main__':

    
    results = runModel(12)
    numRefsOverTime = results['NumRefs']
    costSelfOverTime = results['CostSelf']
    resourcesOverTime  = results['Resources']
    
    plotList = ['Sweden','Denmark', 'Greece', 'France', 'Germany', 'UK', 'Syria']#['Turkey', 'Serbia', 'Hungary', 'Poland', 'Austria', 'France', 'UK']#['Algeria', 'Greece', 'Italy', 'Germany', 'Sweden', 'UK', 'Portugal']#['Sweden','Norway','Finland' ,'Italy', 'Austria', 'Greece', 'Syria','Poland', 'France', 'Germany', 'UK', 'Portugal']
        
    plotResultsFromList(numRefsOverTime, plotList, label='Number of Refugees')
    plotResultsFromList(costSelfOverTime, plotList, label='Cost Function')
    plotResultsFromList(resourcesOverTime, plotList, label='Resources')
    
    if 0: ## TODO: Delete after Jessie checks math!
        num = 4#50
        print 'Calculated cost is: ', costFuncMSIMCalculate( graph.es[num] )
        print graph.es[num]
        print 'Source: ', graph.vs[ graph.es[num]['Source'] ]
        print 'Target: ', graph.vs[ graph.es[num]['Target'] ]















####    
#####    historicalNumOfRefugees = []
#####    numRefs = 0
#####    for timestep in range( len( numRefsOverTime[country] ) ):
#####        for country in countryList:
#####            numRefs = numRefs + numRefsOverTime[country][timeStep]
#####            #print 'no refs: ', numRefs
#####        
#####        historicalNumOfRefugees.append(numRefs)
#####        numRefs = 0
#####    #print 'hist: ',historicalNumOfRefugees
####    
####    if 0:
####        plt.plot(historicalNumOfRefugees)
####        plt.show()
####        
####            #print len( numRefsOverTime[country] )
####    
####    
####    
####    if 0: ## Edges
####        for i in range(45):
####            print graph.es[i]
####    
####    if 0: ## Vertexes:
####        for i in range(30):
####            print graph.vs[i]
####        
for vertex in graph.vs :
    vertex["size"] = int( vertex['NumRefs']*.00002 )

#for edge in graph.es:
#    edge['width'] = edge['Cost']*10
#    edge['name'] = str( edge['MoneyCost'] )
    
layout = graph.layout("kk")
igraph.plot(graph, layout=layout )#,  **visual_style)


####if 0: 
####    allRows = [ ['Country Name', 'Native Population', 'Refugee Applications', 'Safety', 'GNI per capita', 'Unemployment' ] ]
####    for country in countryList:
####        row = []
####        row = row + [country]
####        row = row + [ str(nativePopulation[country])  ]
####        row = row + [ str(refugeeApplications[country]) ]
####        row = row + [ str(safetyCountries[country]) ]
####        row = row + [ str(gniCountries[country]) ]
####        row = row + [ str(unemploymentCountries[country]) ]
####        
####        allRows.append( row )


####    print tabulate.tabulate( allRows, tablefmt = 'latex')

####if 0: 
####    allRows = [ ['Country Name', 'Time 2', 'Time 5', 'Time 10', 'Time 20', 'Time 50' ] ]
####    for country in countryList:
####        row = []
####        row = row + [country]
####        row = row + [ '{0:.1f}'.format( numRefsOverTime[country][2])  ]
####        row = row + [ '{0:.1f}'.format(numRefsOverTime[country][5]) ]
####        row = row + [ '{0:.1f}'.format(numRefsOverTime[country][10]) ]
####        row = row + [ '{0:.1f}'.format(numRefsOverTime[country][20]) ]
####        row = row + [ '{0:.1f}'.format(numRefsOverTime[country][50]) ]
####        
####        allRows.append( row )


####    print tabulate.tabulate( allRows, tablefmt = 'latex')
