import re
import networkx as nx
import os
dic1 = {}
dic2 = {}
counter = 1
dic = {}
edges={}
def node_color(node):
    if(dic[node] == "treatment"):
        return 'blue'
    if(dic[node] == "problem"):
        return 'yellow'
    if(dic[node] == "test"):
        return 'red'
    return 'pink'


def edge_color(edge):
    if(edges[edge][0] == "PIP"):
        return "orange"
    if (edges[edge][0] == "TrCP"):
        return "green"
    if (edges[edge][0] == "TrAP"):
         return "purple"
    return "brown"

G = nx.Graph()
l=0
with open("input_relation.txt") as f:
    for line in f:
     matches=re.findall(r'\"(.+?)\"',line)
     l=l+1;
     if matches[0].strip() not in dic1.keys():
          dic1[matches[0].strip()] = [counter,0]
          dic2[counter] = [matches[0].strip()]
          counter = counter + 1

     if matches[2].strip() not in dic1.keys():
        dic1[matches[2].strip()] = [counter,0]
        dic2[counter] = [matches[2].strip()]
        counter = counter + 1

f.close()

with open("input_concept.txt") as f:
    for line in f:
        matches=re.findall(r'\"(.+?)\"',line)
        dic[matches[0].strip()] = matches[1].strip()
f.close()

with open("input_relation.txt") as f:
    for line in f:
        matches = re.findall(r'\"(.+?)\"', line)
        l = (matches[0].strip(), matches[2].strip())
        if l not in edges.keys():
            edges[l] = [matches[1].strip(), 1]
        else:
            edges[l][1] = int(edges[l][1]) + 1

#print len(edges.keys())
dirname="i2b22010_train/rel/"
files= os.listdir(dirname)
for name in files:
    freq = {}
    f= open(dirname+name,'r')
    for line in f:
        edge=re.findall('c=\"(.*?)\"', line)
        s= edge[0].strip()
        d= edge[1].strip()
        if s != '' and s not in freq.keys():
          freq[s]=1
          dic1[s][1]=dic1[s][1]+1

        if d != ' ' and d not in freq.keys():
            freq[d]=1
            dic1[d][1]= dic1[d][1]+1


for key in dic1.keys():
    print key, " ", dic1[key][1]


for key in edges.keys():
    col = edge_color(key)
    # there are functions also by which we can add attributes to the edges, can be done later
    G.add_edge(dic1[key[0]][0],dic1[key[1]][0],freqency=int(edges[key][1]),rel=edges[key][0],color=col)


for key in dic1.keys():
    col= node_color(key)
    # there are functions also by which we can add attributes to the edges, can be done later
    G.add_node(dic1[key][0],color=col,baseColour=col,label= key,type=dic[key],size=2,degree= G.degree(dic1[key][0]),freqency=dic1[d][1])

nx.write_graphml(G, "test1.graphml")










