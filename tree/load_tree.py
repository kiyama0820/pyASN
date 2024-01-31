import joblib
import ipaddress
import networkx as nx
import matplotlib.pyplot as plt
import pytricia

def main():
    pyt = load_tree("test.pkl")
    while True:
        print('入力待ち')
        iplist = input()
        value1=pyt[ipaddress.IPv4Address(iplist.split()[0])]
        value2=pyt[ipaddress.IPv4Address(iplist.split()[1])]
        
        print(iplist.split()[0])
        for value in value1:
            print(value)
        print(iplist.split()[1])
        for value in value2:
            print(value)
        Make_Net(value1,value2)

def Make_Net(value1,value2):
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
        shortest_path_peer=[]
        for i in range(0, len(shortest_path)-1):
            shortest_path_peer.append((shortest_path[i],shortest_path[i+1]))
            shortest_path_peer.append((shortest_path[i+1],shortest_path[i]))
        edge_color = ['red' if (n in shortest_path_peer) else 'lightblue' for n in G.edges()]
        node_color = ['red' if (n in shortest_path) else 'lightblue' for n in G.nodes()]
        edge_width = [1 if (n in shortest_path_peer) else 0.3 for n in G.edges()]
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color=node_color,alpha=0.6)
        nx.draw_networkx_labels(G, pos, font_size=10)
        nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width)
        #plt.show()
        plt.savefig("sin.png")
        plt.savefig("sin.svg")
    except:      
        print("No Path")
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        plt.savefig("sin.png")
        plt.show()

def load_tree(file_name):
    tree_saver = joblib.load(file_name)
    tree = pytricia.PyTricia()
    for prefix in tree_saver.keys():
        tree[prefix] = tree_saver[prefix]
    return tree

if __name__ == "__main__":
    main()