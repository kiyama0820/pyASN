import joblib
import ipaddress
import networkx as nx
import matplotlib.pyplot as plt
import pytricia
import glob
import csv

class HopPath:    
    def __init__(self,pyt,dpath,dns_ip):
        self.pyt = pyt
        self.dpath = dpath
        self.dns_ip = dns_ip

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
            return shortest_path
        except:      
            print("No Path")
            return 0
        
    def make_list(self,input_file):
        list=[]
        value1=self.pyt[ipaddress.IPv4Address(self.dns_ip)]
        with open(input_file) as f:
            for i in f:
                ip=i.split()[1]
                if type(ipaddress.ip_address(ip)) is ipaddress.IPv4Address:
                    value2=self.pyt[ipaddress.IPv4Address(ip)]
                    print(value1,value2)
                    shortest_path=self.Shortest_Path(value1,value2)
                    #print(hop)
                    if shortest_path!=0:
                        shortest_path.insert(0,i.split()[0])
                        list.append(shortest_path)
        return list.append(shortest_path)

    def glob_dns_a(self):
        for d in glob.glob(self.dpath):
            fpath=d+'/*.txt'
            for input_file in glob.glob(fpath):
                list=self.make_list(input_file)
                s_name=d
                with open(s_name, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(list)