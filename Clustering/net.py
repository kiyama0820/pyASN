import networkx as nx
import matplotlib.pyplot as plt
import csv

def main():
    file_name='out.csv'
    len=50
    c=[]
    as_n=[]
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            for a in row[2:]:
                if a not in as_n:
                    as_n.append(a)
                    c.append(int(row[0]))
                else:
                    c[as_n.index(a)]+=int(row[0])

    c,as_n = zip(*sorted(zip(c,as_n),reverse=True))
    as_n=(list(as_n[:len]))


    G = nx.DiGraph()
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            #l = row[1:2]+list(set(as_n) & set(row[1:]))
            l=row[1:2]
            for r in row[2:]:
                if r in as_n:
                    l.append(r)
            nx.add_path(G, l) 
            print(l)

    keys=list(G._node.keys())
    node_color=[e_color(1,1)] + [e_color(c[0],c[as_n.index(k)]) for k in keys[1:]]
    #pos = nx.spring_layout(G)
    pos = nx.planar_layout(G) # Edgeが交差しないように配置
    nx.draw_networkx(G, pos, alpha=0.5, font_size=10, node_color=node_color)
    plt.show()
    #plt.savefig(file_name+".svg") 

def e_color(max_co,counter):
   co_ratio=counter/max_co
   c = int(((-co_ratio / 2) + 0.5) * 255)
   if co_ratio >= 0.75:
     return get_colocode(255-c, c, 0)
   elif co_ratio >= 0.5:
     return get_colocode(c, 255-c, 0)
   elif co_ratio >= 0.25:
     return get_colocode(0, 255-c, c)
   else:
     return get_colocode(0, c, 255-c)

def get_colocode(r,g,b):
    return '#%02X%02X%02X' % (r,g,b)

def Make_Net(value1,value2):
    G = nx.Graph()
    for value in value1:
        source=value[-1]
        nx.add_path(G, value)
    for value in value2:
        target=value[-1]
        nx.add_path(G, value)

if __name__ == "__main__":
    main()