import geoip2.database
import tqdm

input,output=input().split()
reader = geoip2.database.Reader('GeoLite2-ASN_20230609/GeoLite2-ASN.mmdb')
output_file = open(output, 'a')
with open(input) as f:
    #for i, l in tqdm.tqdm(enumerate(f)):
    for i, l in enumerate(f):
        ip = l[63:104][:l[63:104].find("#")]  
        target = str(reader.asn(ip).autonomous_system_number)+"\n"
        #target = str(reader.asn(ip[i]).autonomous_system_number)+"\n"
        output_file.write(target)