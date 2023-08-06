import numpy  as np 
from collections import deque
import math
from utils import genGraph, printGraph,printGraphWithMatching
def hopcroft(G,A):
    M={}
    visit={}
    for i in range(len(G)):
        M[str(i)]=-1     
    has_aug_path=True
    it=0
    while has_aug_path:
        it+=1
        print("iter :",it)
        if it==3: break
        for u in range(len(G)):
            visit[str(u)]=0
        has_aug_path=False
        l=math.inf
        L=bfs(G,A,M)
        print(L)
        for u in L.keys():
            if int(u)>=A and M[str(u)]==-1 and  L[u]!=math.inf:
                has_aug_path=True
                l=min(l,L[u]) # shortest augmenting path to free vertex in B
        print(l)
        for u in range(A):
            if visit[str(u)]==0 and M[str(u)]==-1:
                aug(u,G,A,L,M,l,visit)
        # has_aug_path=False

    return M
def bfs(G,A,M=None):
    q = deque()
    L={}
    bfsvisit={}
    for v in range(len(G)):
        bfsvisit[str(v)]=0
        L[str(v)]=math.inf
    # visit is a dictionary, which key is vertice,
 #value is  0 if unvisited, and 1  if visited
    for v in range(A):
        if M[str(v)]==-1:
            q.append(v)
            L[str(v)]=1
    while len(q)>0:
        v=q.popleft()
        bfsvisit[str(v)]=1
        if v < A:
            for u in range(A,len(G)):
                if G[v,u]==1:
                    if bfsvisit[str(u)]==0:
                        L[str(u)]= L[str(v)]+1
                        q.append(u)
        else:
            if M[str(v)]!=-1:
                L[str(M[str(v)])]= L[str(v)]+1
                q.append ( M[str(v)])
    return L
def aug (u,G,A,L,M,l,visit):
    # print("u",u,"L",L,"visit",visit)
    visit[str(u)]=1
    for v in range(A,len(G)):
        if G[u,v]==1:
            print ("u,v",u,v)
            if M[str(v)]==-1:
                visit[str(v)]=1
                M[str(v)]=u 
                M[str(u)]=v 
                return True 
            elif visit[str(v)]==0 and L[str(v)]==L[str(u)]+1:
                visit[str(v)]=1
                if   L[str(v)] <l and visit[str(M[str(v)])]==0 and aug(M[str(v)],G,A,L,M,l,visit):
                    M[str(v)]=u 
                    M[str(u)]=v 
                    return True 
    return False



if __name__=="__main__":
   
    G2=genGraph(mode="random")
    A=len(G2)//2
    printGraph(G2,A)
    M=hopcroft (G2,A)
    printGraphWithMatching(G2,A,M)
    



