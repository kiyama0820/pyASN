import geoip2.database

input,output=input().split()
reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')
output_file = open(output, 'a')
with open(input) as f:
    for i, l in enumerate(f):
        target = str(reader.asn(l.replace(' ', '').replace('\n', '')).autonomous_system_number)+"\n"
        output_file.write(target)
