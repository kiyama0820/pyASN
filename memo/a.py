import glob
import os
import pytricia

pyt = pytricia.PyTricia(128)
for l in glob.glob('txt/*.txt'):
    with open(l) as f:
        for line in f:
            line=line.split()
            try:
                if pyt.has_key(line[1])==False:
                    pyt[line[1]]=int(line[0])
                else:
                    pyt[line[1]]+=int(line[0])
            except:
                pass

f=open('new.txt', 'w')
for prefix in pyt:
    f.write(str(pyt[prefix])+' '+str(prefix)+'\n')
f.close()
