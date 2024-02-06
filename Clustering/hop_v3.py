from tqdm import tqdm
import csv

def main():
  file_name='out.csv'
  min_hop=0
  as_list=[]
  with open(file_name) as f:
    reader = csv.reader(f)
    for row in reader:
      min_hop+=(len(row)-2)*int(row[0])
      for as_n in row[2:]:
        if as_n not in as_list:
          as_list.append(as_n)
          
  print('raw_hop:',min_hop)
  for as_n in tqdm(as_list):
    hop=0
    with open(file_name) as f:
      reader = csv.reader(f)
      for row in reader:
        if as_n in row[1:]:
          hop+=(len(row)-row.index(as_n)-1)*int(row[0])
        else:
          hop+=(len(row)-2)*int(row[0])
    if hop<min_hop:
      min_hop=hop
      min_as=as_n
  print('min_as:',min_as,' min_hop:',min_hop)

if __name__ == "__main__":
    main()