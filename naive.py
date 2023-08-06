import numpy  as np 
from collections import deque


def maximumMatch(G,A):
    M={}
    for v in range (len(G)):
        M[str(v)]=-1
    has_aug=True
    it=0
    while has_aug:
        print ("iter ",it)
        it+=1
        has_aug=False 
        visit={}
        for v in range(len(G)):
            visit[str(v)]=0
        for v in range(A):
            if M[str(v)]==-1 and visit[str(v)]==0:
                if aug(v,G,A,M,visit):
                    has_aug=True
    return M
def aug(v,G,A,M,visit):
    # print ("v",v,"\n", "M",M,"visit",visit)
    visit[str(v)]=1
    for u in range(A,len(G)):
        if G[v,u]==1: ## neighbor of u
            if visit[str(u)]==0 and M[str(u)] ==-1:
                visit[str(u)]=1
                M[str(u)] =v 
                M[str(v)] =u 
                return True 
            else:
                if visit[str(u)]==0:
                    visit[str(u)]=1
                    if aug( M[str(u)],G,A,M,visit):
                        M[str(u)] =v 
                        M[str(v)] =u 
                        return True 
    return False

def generateM(G,A ,match):
        M={}
        for v in range(len(G)):
            M[str(v)]=-1
        for (u,v) in match:
            assert 0<=u<A and len(G)>v >=A, "invalid match"
            G[u,v]=1
            M[str(u)]=v
            M[str(v)]=u 
        return M     
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
        
if __name__=="__main__":  
    G2=genGraph(mode="random")
    printGraph(G2,len(G2)//2)
    M=maximumMatch(G2,len(G2)//2)
    print ("M",M)
    


    


    

