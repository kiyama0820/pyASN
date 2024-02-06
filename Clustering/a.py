import joblib
import ipaddress
import networkx as nx
import matplotlib.pyplot as plt
import pytricia
import HopPath

def main():
        pyt = load_tree("test.pkl")
        #dpath='/home/jprs/shinta/k-sugizaki/dnscap/c.dns.jp/*202310*/*'
        dpath='./*/'
        dns_ip='203.119.1.0'
        HopPath.HopPath(pyt,dpath,dns_ip).glob_dns_a()

def load_tree(file_name):
    tree_saver = joblib.load(file_name)
    tree = pytricia.PyTricia()
    for prefix in tree_saver.keys():
        tree[prefix] = tree_saver[prefix]
    return tree

if __name__ == "__main__":
    main()