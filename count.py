def main():
  file_name='a22.tyo.20230710.ip'
  clist = []
  counter,path=make_list(file_name)
  for n,pa in enumerate(path):
    for m,p in enumerate(pa):
      a=0
      for l in clist:
        if ((l[1])==m)and(l[2]==p):
          l[0]+=counter[n]
          a=1
          break
      if a==0:
        clist.append([counter[n],m,p])
  clist=sorted(clist,reverse=True)
  clist.pop(0)
  for l in clist:
    print(l)



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