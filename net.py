import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

edgewidth = []
G = nx.DiGraph()
f = open('a22.tyo.20230710', 'r')
for i in f:
    i = i.replace('\', ','\',').split()
    edgewidth.append(int(i.pop(0)))
    path=i[1].replace('[\'','').replace('i\']','').split('\',\'')
    path.pop(-1)
    nx.add_path(G, path)
vmin = np.array(edgewidth).min()
vmax = np.array(edgewidth).max()
b = (edgewidth - vmin).astype(float) / (vmax - vmin).astype(float)
#nx.draw_networkx(G,width = (b+0.1)*10, alpha=0.5)
nx.draw_networkx(G,alpha=0.5)
plt.show()
