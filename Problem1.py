import snap

# Load the Wiki Vote Graph
WikiG = snap.LoadEdgeList(snap.PNGraph,"C:\Users\manas\Downloads\wiki-Vote\Wiki-Vote.txt", 0, 1)

# 1. Count the number of nodes
count = 0
for NI in WikiG.Nodes():
    count = count + 1

print "Problem 1 : node count :%d" %(count)

#2 . Count the number of nodes with self Edges
count = 0
add = 0
for NI in WikiG.Nodes() :
    for Id in NI.GetOutEdges():
        if NI.GetId() == Id:
            add = 1
    if add == 1:
	count = count + 1
	add = 0

print "Problem 2 : self loop count :%d" %(count)

#3. Count the direct edges

count = 0
for NI in WikiG.Nodes() :
    for Id in NI.GetOutEdges():
        if NI.GetId() <> Id:
            count = count + 1

print "Problem 3 : direct edges count :%d" %(count)

#4. Count undirected edges in network
WikiUNG = snap.ConvertGraph(snap.PUNGraph, WikiG)

count = 0
for NI in WikiUNG.Nodes() :
    for Id in NI.GetOutEdges():
        if NI.GetId() < Id:
            count = count + 1

print "Problem 4 : undirect edges count :%d" %(count)

#5. Count the number of reciprocated edges
count = 0
for NI in WikiG.Nodes() :
    for Id in NI.GetOutEdges():
        if NI.GetId() < Id and WikiG.IsEdge(Id, NI.GetId()):
            count = count + 1

print "Problem 5 : reciprocated edges count :%d" %(count)


#6. Count nodes with zero out degree
count = 0
for NI in WikiG.Nodes() :
    if NI.GetOutDeg() == 0:
        count = count + 1

print "Problem 6 : zero out degree node count :%d" %(count)

#7. Count nodes with zero in degree
count = 0
for NI in WikiG.Nodes() :
    if NI.GetInDeg() == 0:
        count = count + 1

print "Problem 7 : zero in degree node count :%d" %(count)


#8. Count nodes with out degree > 10
count = 0
for NI in WikiG.Nodes() :
    if NI.GetOutDeg() > 10:
        count = count + 1

print "Problem 8 : out degree > 10 node count :%d" %(count)

#9. Count nodes with in degree < 10
count = 0
for NI in WikiG.Nodes() :
    if NI.GetInDeg() < 10 :
        count = count + 1

print "Problem 9 : in degree < 10 node count  :%d" %(count)