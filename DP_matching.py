import numpy as np
import time
from DP import DPmatching

def read_param(filename):
    with open(filename,"r") as f:
        for i, line in enumerate(f):
            line = line.replace('\n','')
            if i == 0:
                continue
            if i == 1:
                name = line
            elif i == 2:
                number = int(line)
                a = np.zeros((number,15))
            else:
                h  = map(float,line[:-1].split(" "))
                a[i-3] = [t for t in h]
    return name,a
def get_dist_map(a,b):
    
    wide = b.shape[0]
    height = a.shape[0]
    d = np.zeros((height,wide))
    for i in range(height):
        for j in range(wide):
            dist = (a[i]-b[j])**2
            sum_dist = float(np.sqrt(dist.sum()))

            d[i,j] = sum_dist
    return d

def read_files(filename):
    temp = []
    names = {}
    print("____read_file____")
    for i in  range(20): 
        spel,LPC = read_param(filename+"_{0:03d}.txt".format(i+1))
        names[i] = spel
        temp.append(LPC)

    return names,temp

def main():
    tmp_names, temp = read_files("./city022/city022")
    names, tmp = read_files("./city011/city011")
    r = len(temp)
    scores = np.ones((r,r))
    print("___START_DPMATCHING___")
    for i in range(r):
        for j in range(r):
            
            num = np.array(temp[i])
            num2 = np.array(tmp[j])
            t = get_dist_map(num,num2)
            scores[i,j] = DPmatching(t)
    print("__FINISH__")
    print(scores.shape)
    tets = scores.tolist()
    acu = 0
    for n,score in enumerate(tets):
        #y = [t for t,n in enumerate(score) if n == min(score)]
        #y = np.where(score==min(score))
        y = score.index(min(score))
        if tmp_names[y]==names[n]:
            acu = acu + 1
        else:
            print(tmp_names[y],names[n])
        with open("score.txt","a") as f:
            f.writelines(str(score))
        #if n == y[0]:
        #    acu = acu + 1
    print("acurate",acu/(n+1))


if __name__=="__main__":
    main()
