import glob
#import pytricia

def pytri(aspath):
    list=[]
    pyt=pytricia.pytricia(128)
    with open(aspath) as f:#line break correction
        p_l=''
        for l in f:
            if l[1]=='*':
                list.append(p_l.replace('* i', '*').replace('*>i', '*>').split())
                p_l=l
            else:
                p_l = p_l.replace('\n', '') + ' ' + l
    f.close
    list.pop()
    lp_l=''
    for n, l in enumerate(list):
        if l[0]=='*>':
            p_l=l[1]
        else:
            list[n].insert(1,p_l)
       # if n<2000030 and n>2000000:
       #     print(list[n])
        if l[0]=='*>':
            pyt[l[1]]=[0,l[4:]]
    #retrun pyt

def asip(pyt,file):
    with open(file) as f:
        for ip in f:
            ip = ip.split()
            key=pyt.get_key(ip[1])
            pyt.insert(key,[pyt[key][0]+ip[0],pyt[key][1]])
    f.close
    with open(file.replace('../../query-ip/', ''), 'w') as f:
        for p in pyt:
            f.write(p,pyt[p])
    f.close
