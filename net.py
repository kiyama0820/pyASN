import matplotlib.pyplot as plt
import networkx as nx

def main():
  file_name='a22.tyo.20230710.ip'
  G = nx.DiGraph()
  counter,path=make_list(file_name)
  max_co=counter[-1]
  for i,pa in enumerate(path):
    print(counter[i],pa)
    nx.add_path(G, pa,color=e_color(max_co,counter[i]))

  edge_color = [edge["color"] for edge in G.edges.values()]
  nx.draw_networkx(G,alpha=0.5, edge_color=edge_color)
  plt.savefig(file_name+".png") 
  plt.show()

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

def make_list(file):
  f = open(file, 'r')
  counter =  []
  path=[]
  for i in f:
      i = i.replace('\', \'','\',\'').split()
      p=[i[2].replace('[[\'','').replace('\']]','').split('\',\'')]
      p=list(filter(lambda x: x!='i', p[0]))
      p=list(filter(lambda x: x!='100', p))
      p=list(filter(lambda x: x!='0', p))
      p=list(dict.fromkeys(p)) # Duplicate Delete
      p.insert(0, 0) # Initial value insertion
      if p in path: # Combine duplicate routes
        counter[path.index(p)]+=int(i[0])
      else:
        path.append(p)
        counter.append(int(i[0]))
  zip_lists = zip(counter, path)
  zip_sort = sorted(zip_lists)
  counter, path = zip(*zip_sort)
  return counter,path

if __name__ == "__main__":
    main()
