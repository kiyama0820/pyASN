input,output=input().split()
output_file = open(output, 'a')
with open(input) as f:
    p_ip=''
    for i, l in enumerate(f):
        if i > 6:
            ip=l[3:19]
            if ip=='                ':
                ip=p_ip
            else:
                p_ip=ip
            if l[:2]=='*>':
                out = ip + ' ' +l[59:]
                output_file.write(out)