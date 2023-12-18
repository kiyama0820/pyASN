import matplotlib.pyplot as plt
import networkx as nx

def main():
  file_name='input'
  raw_counter,raw_path=make_list(file_name)
  max_l=0
  for pa in raw_path:
    if max_l<len(pa):
      max_l=len(pa)
      
  for layer in range(0,max_l-1):
    print('layer',layer)
    G = nx.DiGraph()
    counter,path=re_sort(raw_counter,raw_path,layer)
    if layer==0:
      max_co=counter[-1]
    for i,pa in enumerate(path):
      #print(counter[i],pa)
      nx.add_path(G, pa,color=e_color(max_co,counter[i]))

    edge_color = [edge["color"] for edge in G.edges.values()]
    node_size=[1]*len(G._node)
    font_size=5
    nx.draw_networkx(G,alpha=0.5, edge_color=edge_color, node_size = node_size, font_size=font_size)
    plt.title("hop "+str(layer)+" to "+str(layer+1))
    plt.savefig(file_name+".hop"+str(layer)+"to"+str(layer+1)+".svg") 
    plt.show()

def e_color(max_co,counter):
   co_ratio=counter/max_co
   c = int(((-co_ratio / 2) + 0.5) * 255)
   if co_ratio >= 0.5:
     return get_colocode(255-c, c, 0)
   elif co_ratio >= 0.1:
     return get_colocode(c, 255-c, 0)
   elif co_ratio >= 0.05:
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
      p=list(filter(lambda x: x!='90', p))
      p=list(filter(lambda x: x!='?', p))
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

def re_sort(counter,path,layer):
  new_counter =  []
  new_path=[]
  for i,p in enumerate(path):
    if len(p)>layer+1:
      if p[layer:layer+2] in new_path: # Combine duplicate routes
        new_counter[new_path.index(p[layer:layer+2])]+=counter[i]
      else:
        new_path.append(p[layer:layer+2])
        new_counter.append(counter[i])

  zip_lists = zip(new_counter, new_path)
  zip_sort = sorted(zip_lists)
  new_counter, new_path = zip(*zip_sort)
  return new_counter,new_path

if __name__ == "__main__":
    main()
