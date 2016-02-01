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

print graph

for vertex in graph.vs:
    print vertex
    
