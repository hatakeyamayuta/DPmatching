import numpy as np
import time
def min_map(temp):
    x = min(temp)
    #y = [t for t,n in enumerate(temp) if n == x]
    y = temp.index(x)
    return x,y
def DPmatching(d):
    """
    d = np.array([[1,5,2,1,2],
                  [2,2,3,2,2],
                  [2,4,2,1,2],
                  [2,2,3,1,1]])
    """
    #print("map\n",d)      
    h, w = d.shape
    g = np.zeros((h,w))
    road = np.copy(g)
    g[0,0] = d[0,0]
    for t in range(1,w):
        g[0,t] = g[0,t-1]+d[0,t]
    for n in range(1,h):
        g[n,0] = g[n-1,0]+d[n,0]

    for i in range(1,h):    
        for j in range(1,w):    
            temp = [g[i-1,j]+d[i,j],g[i-1,j-1]+d[i,j]*2,g[i,j-1]+d[i,j]]
            number ,step = min_map(temp)
            g[i,j] = number
            road[i,j] = step
    score = float(g[h-1,w-1])
    #print(g)
    #print(road)
    #print("sum",score)
    return score

def main():
    DPmatching()

if __name__=="__main__":
    main()

