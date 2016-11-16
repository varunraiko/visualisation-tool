import re

g=  open("temp.gexf",'w')


with open("Graph1.gexf") as f:
    for line in f:
        matches = re.findall(r'<viz:position(.+?)></viz:position>', line)
        if matches == []:
            continue
        else:
          a= '<viz:position '+matches[0] +'></viz:position>\n'
          g.write(a)

g.close()
f.close()

g = open("temp.gexf",'r')
li= g.readlines()

print len(li)
h = open("final_graph.gexf",'w')
i=0
with open("new.gexf") as f:
    for line in f:
        matches = re.findall(r'<viz:position(.+?)></viz:position>', line)
        if matches == []:
            h.write(line);
        else:
           if i < len(li):
              h.write(li[i])
           else:
               h.write(line)

