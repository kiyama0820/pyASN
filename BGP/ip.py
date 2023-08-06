import ipaddress
import csv

aspath=[]
with open('best_path.aspath') as f:
    for l in f:
        aspath.append([l[0:16].replace(' ', ''),0,l[18:].replace('\n', '')])

with open('ip.txt') as f:
    for ip in f:
        for n,nw in enumerate(aspath):
            if ipaddress.ip_address(ip.replace('\n', '')) in ipaddress.ip_network(nw[0]): 
                aspath[n][1]+=1
                break

with open('data.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(aspath)
print(aspath)