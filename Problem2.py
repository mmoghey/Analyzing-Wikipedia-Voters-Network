import snap
import numpy as np
import matplotlib.pyplot as plt

# Load the Wiki Vote Graph
WikiG = snap.LoadEdgeList(snap.PNGraph,"C:\Users\manas\Downloads\wiki-Vote\Wiki-Vote.txt", 0, 1)

#find out the max out degree
l1 = []
for NI in WikiG.Nodes():
    l1.append(NI.GetOutDeg())

maxOutDegree = max(l1)


# populate list l2 with the count of nodes with out degree as index ( for eg., l2[outdegree] = count)
l2 = []
#allocate the memory first
for x in range(0, maxOutDegree+1):
    l2.append(0)

for NI in WikiG.Nodes() :
    l2[NI.GetOutDeg()] = l2[NI.GetOutDeg()] + 1

# populate x and y as np array
y = np.array(l2)
x = np.array(list(range(0,maxOutDegree+1)))

#plot loglog 
plt.title ("distribution of out-degrees of nodes")
plt.xlabel ("integer")
plt.ylabel ("number of nodes with out-degree equal to x")
plt.loglog(x,y,basex=10, basey=10, marker='o', linestyle = 'None')
plt.show()





