import matplotlib.pyplot as plt
import os
import networkx as nx
import numpy as np
from networkx.algorithms import bipartite

def printGraph(G,A):
    save_path=os.path.join(os.path.dirname(__file__),"visualize","graph.png")
    B=nx.Graph()
    B.add_nodes_from(range(A))
    B.add_nodes_from(range(A,len(G)))
    edges=[]
    for i in range (A):
        for j in range(A,len(G)):
            if G[i,j]==1:
                edges.append((i,j))
 
    B.add_edges_from(edges)  
    X=range(A)
    Y=range(A,len(G))
    pos = dict()
    pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
    pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
    nx.draw(B, pos=pos,with_labels=True)        
    plt.show()
    plt.savefig(save_path)
    plt.clf()
def printGraphWithMatching(G,A,M):
    save_path=os.path.join(os.path.dirname(__file__),"visualize","matching.png")
    B=nx.Graph()
    B.add_nodes_from(range(A))
    B.add_nodes_from(range(A,len(G)))
    edges=[]
    for i in range (A):
        for j in range(A,len(G)):
            if G[i,j]==1:
                edges.append((i,j))
    match=[]
    for u in  M.keys() :
        if M[u]!=-1:
            match.append((int(u),M[u]))          
    B.add_edges_from(match, weight=15)
    X=range(A)
    Y=range(A,len(G))
    pos = dict()
    pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
    pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
    nx.draw(B, pos=pos,with_labels=True)  
    plt.show()
    plt.savefig(save_path)
    plt.clf()


def genGraph(mode="fix",size=8):
    A=size//2
    if mode=="fix":
        pairs=[(0, 6), (0, 7), (1, 4), (1, 5), (2, 4), (2, 5), (2, 7), (3, 4), (3, 5), (3, 6)]
        G=np.zeros((size,size))
        for r in range (len(G)):
            G[r,r]=1
        for (u,v) in pairs:
            assert 0<=u<A and len(G)>v >=A, "invalid match"
            G[u,v]=1
        return G 
    elif mode=="random":
        G=np.zeros((size,size))
        for r in range (len(G)):
            G[r,r]=1
        for i in range (A):
            for j in range(A,len(G)):
                    G[i,j]=np.random.randint(0,2)     
        return G
    else:
        print ("invalid mode")
        return None
        