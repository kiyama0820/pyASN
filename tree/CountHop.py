import pytricia
import joblib
import ipaddress
import networkx as nx
import matplotlib.pyplot as plt
import pytricia

    
def main():
    pyt = load_tree("test.pkl")
    input='txt_00000_20231019211011.txt'
    dns_ip='203.119.1.0'
    hop_countr,query_countr=Count_Hop(pyt,input,dns_ip)
    print('hop_countr:',hop_countr,'\nhop per query:',hop_countr/query_countr)

def Shortest_Path(value1,value2):
    G = nx.Graph()
    for value in value1:
        source=value[-1]
        nx.add_path(G, value)
    for value in value2:
        target=value[-1]
        nx.add_path(G, value)

    try:
        shortest_path=nx.shortest_path(G, source=source, target=target)
        print("shortest_path",shortest_path)
        return len(shortest_path)-1
    except:      
        print("No Path")
        return 0
    
def Count_Hop(pyt,input,dns_ip):
    hop_countr=0
    query_countr=0
    value1=pyt[ipaddress.IPv4Address(dns_ip.split()[0])]
    with open(input) as f:
        for i in f:
            ip=i.split()[1]
            if type(ipaddress.ip_address(ip)) is ipaddress.IPv4Address:
                value2=pyt[ipaddress.IPv4Address(ip)]
                hop=Shortest_Path(value1,value2)
                #print(hop)
                if hop!=0:
                    hop_countr += int(i.split()[0])*hop
                    query_countr += int(i.split()[0])
    return hop_countr,query_countr

def load_tree(file_name):
    tree_saver = joblib.load(file_name)
    tree = pytricia.PyTricia()
    for prefix in tree_saver.keys():
        tree[prefix] = tree_saver[prefix]
    return tree

if __name__ == "__main__":
    main()