# Bucket file created, needed to find the association rules

import os
import re
import Orange.orange

li_edges={}
node_number={}
rev_node_num={}
entries=[]
dirname="i2b22010_train/rel/"
files= os.listdir(dirname)

flag =1

for name in files:
    f= open(dirname+name,'r')
    for line in f:
       edge=re.findall('c=\"(.*?)\"', line)
       
       if edge[0] in li_edges.keys():
        li_edges[edge[0]].append(edge[1])
       
       else:
        li_edges[edge[0]]=[]
        li_edges[edge[0]].append(edge[1])
       
       if edge[0] not in node_number.keys():
       	     val= len(node_number.keys())
       	     node_number[edge[0]]=val;
             rev_node_num[val]=edge[0]
       if edge[1] not in node_number.keys():
       	     val= len(node_number.keys())
       	     node_number[edge[1]]=val;
             rev_node_num[val]=edge[1]
       
       node1= str(node_number[edge[0]])
       node2= str(node_number[edge[1]])
       string= node1 +", "+ node2
       string2= edge[0]+"   -> "+edge[1]
       if flag:
        fp = open("graph.basket",'w')
        fp2 = open("edges.txt",'w')
       else:    
         fp = open("graph.basket",'a')
         fp2 = open("edges.txt",'a')
       fp.write(string+"\n")
       fp2.write(string2+"\n")
       flag =0

items = Orange.orange.ExampleTable("graph")

val = raw_input("enter the value of support: ")
val = float(val)
print len(files)
val  = (val*1.0)/len(files)
# support values to be decided
rules = Orange.orange.AssociationRulesSparseInducer(items, support = val,max_item_sets = 60000000)

for r in rules:
    rule= str(r)
    rule= rule.split("->")
    left = rule[0]
    right = rule[1]
    left = left[:-1]
    right = right[1:]
    st=""
    left = left.split(" ")
    
    
    for i in xrange(len(left)):
      st=st+(rev_node_num[int(left[i])])+"? "
    st=st[:-2]+" -> "
    right = right.split(" ")
    for i in xrange(len(right)):
      st=st+(rev_node_num[int(right[i])])+"? "  
    st=st[:-2]
    print st
    print "%5.6f" % (r.support*len(files))









