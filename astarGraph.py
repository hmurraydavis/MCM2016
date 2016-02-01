import igraph
import countries as COS
#import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pprint
import tabulate
import math
import random

graph = igraph.Graph()
graph = graph.Read_Pickle('MCM_Graph.p')


#temp = graph.shortest_paths_dijkstra(source=0, target=None, weights=None)
temp2 = graph.get_shortest_paths(0, 20, weights ='Source')
print temp2


