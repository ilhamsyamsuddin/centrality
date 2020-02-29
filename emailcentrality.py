import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def getList(dict_value): 
    return list(dict_value)

def draw(G, pos, measures, measure_name):
    
    nodes = nx.draw_networkx_nodes(G, pos)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma, 
                                   node_color=getList(measures.values()),
                                   nodelist=getList(measures.keys()))
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    
    labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

G = nx.read_edgelist('email.txt',create_using=nx.Graph(),nodetype=int) #Graph() untuk undirected graph
#G = nx.karate_club_graph()
pos = nx.spring_layout(G)
print(nx.info(G))

#Degree centrality
draw(G, pos, nx.degree_centrality(G), 'Degree Centrality')

#Betweenness Centrality
draw(G, pos, nx.betweenness_centrality(G), 'Betweenness Centrality')
#Closeness Centrality
draw(G, pos, nx.closeness_centrality(G), 'closeness Centrality')
#Eigenvector Centrality
draw(G, pos, nx.eigenvector_centrality(G), 'Eigenvector Centrality')
#pageRank = nx.pagerank(g, alpha=0.3)
draw(G, pos, nx.pagerank(G, alpha=0.3), 'Page Rank')
"""
degcen = nx.degree_centrality(G)
measure = degcen.values()
print(getList(measure)) """