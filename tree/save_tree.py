import pytricia
import joblib
import mrtparse
import ipaddress

def main():
    pyt = pytricia.PyTricia(128)
    pyt = Make_Tree(pyt)
    save_tree(pyt, "test.pkl")

def save_tree(tree, file_name):
    tree_saver = {}
    for prefix in tree:
        tree_saver[prefix] = tree[prefix]
    joblib.dump(tree_saver, file_name)

def Make_Tree(pyt):
    for entry in mrtparse.Reader("rib.20230830.0000.bz2"):
        try:
            net=ipaddress.IPv4Network(str(entry.data['prefix'])+'/'+str(entry.data['length']))
            values=[]
            for i in range(0,entry.data['entry_count']):
                list=str(entry.data['rib_entries'][i]['path_attributes'][1]['value'][0]['value'])
                list=list.replace('[','').replace(']','').replace(',','').replace('\'','').split()
                values.append(list)
            pyt.insert(net,values)
        except:
            pass
    return pyt

if __name__ == "__main__":
    main()