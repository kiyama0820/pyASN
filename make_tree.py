import glob
import pytricia


def main():
    # test for glob
    for f in glob.glob('../../query-ip/*'):
        if 'tyo' in f and 'a' in f:
            print('A_TYO',f)
        if 'tyo' in f and 'g' in f:
            print('G_TYO',f)
        if 'osa' in f and 'a' in f:
            print('A_OSA',f)
"""
    for f in glob.glob('../../query-ip/*'):
        if 'tyo' in f and 'a' in f:
            pyt=pytri("'/tmp/BGP/") # Write additional paths with asapath
            update_pyt(pyt,file_path=f)
        if 'tyo' in f and 'g' in f:
            pyt=pytri("'/tmp/BGP/") # Write additional paths with asapath
            update_pyt(pyt,file_path=f)
        if 'osa' in f and 'a' in f:
            pyt=pytri("'/tmp/BGP/") # Write additional paths with asapath
            update_pyt(pyt,file_path=f)
        
"""
def pytri(aspath):
    # Takes aspath file path and returns pytricia
    list=[]
    pyt = pytricia.PyTricia(128)
    with open(aspath) as f: # line break correction
        p_l=''
        for l in f:
            if '*' in l:
                p_l=l
            else:
                if list!=[]:
                    list.pop(-1)
                p_l = p_l.replace('\n', '') + ' ' + l

            list.append(p_l.replace('* i', '*').replace('*>i', '*>').split())
    f.close
    list.pop(0)

    p_l=''
    for n, l in enumerate(list):
        if l[0]=='*>':
            p_l=l[1]
        else:
            list[n].insert(1,p_l) # Network address completion
        if l[0]=='*>': 
            path=l[4:]
            pyt[l[1]]=[0,path[path.index('0'):]] # Remove unnecessary elements and put them in pytricia
    return pyt 

def update_pyt(pyt,file_path):
    # Receives pytricia and IP list path.
    # Output updated pytricia.
    with open(file_path) as f:
        for ip in f:
            ip = ip.split()
            key=pyt.get_key(ip[1])
            pyt.insert(key,[pyt[key][0]+int(ip[0]),pyt[key][1]])
    f.close

    #f=open(file_path.replace('../../query-ip/', ''), 'w') # The file name of the output should be the same as iplist
    f=open('new.txt', 'w')
    for prefix in pyt:
        count_path = pyt[prefix]
        if count_path[0]!=0: # Output only paths used more than once
            print(str(count_path[0])+ ' '+str(prefix)+' '+str(count_path[1]))
            f.write(str(count_path[0])+ ' '+str(prefix)+' '+str(count_path[1])+'\n')
    f.close

if __name__ == "__main__":
    main()
