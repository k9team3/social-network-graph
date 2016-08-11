import networkx as nx
import matplotlib.pyplot as plt
import os, sys
upath = input("Logs Directory: ")
qw = input("Include Text Labels (Y/N): ")
ns = int(input("Node Size: "))
no = float(input("Node Opacity: "))
ew = float(input("Edge Width: "))
w_l = False
if qw.lower() in "y":
  w_l = True
if w_l is True:
  fs = int(input("Font Size: "))
G = nx.Graph()
dirs = os.listdir(upath + "/")
files = []
for file in dirs:
  if '.' in str(file):
    files.append(file)
for f in files:
  q = open("logs/" + f,"r")
  t = q.read().replace(",undefined","").split(",")
  G.add_nodes_from(t)
  q.close()
  for n in t:
    G.add_edge(f.replace(".log",""),n)
if w_l is True:
  nx.draw_networkx(G,pos=nx.spring_layout(G),with_labels=w_l,node_size=ns,alpha=no,width=ew,font_size=fs)
else:
  nx.draw_networkx(G,pos=nx.spring_layout(G),with_labels=w_l,node_size=ns,alpha=no,width=ew)
i = 0
while os.path.exists("graphs/graph" + str(i) + ".png"):
  i += 1
fname = "graphs/graph" + str(i) + ".png"
plt.savefig(fname)
os.system('start ' + "graphs/graph" + str(i) + ".png")
