import matplotlib.pyplot as plt
from utils import genGraph, printGraph
def printGraph(G,A):
    ls=[]
    for i in range (A):
        for j in range(A,len(G)):
            if G[i,j]==1:
                ls.append((i,j))
    print (ls)


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
        