from tqdm import tqdm
import csv
import numpy as np
from sklearn.cluster import SpectralClustering

def main():
  file_name='out.csv'
  as_matrix=make_matrix(file_name)

  num_clusters = 2  # クラスタの数を指定
  sc = SpectralClustering(n_clusters=num_clusters, affinity='precomputed', random_state=0)
  labels = sc.fit_predict(as_matrix)
  print("クラスタリング結果:", labels)
  with open('out.csv', 'w',  newline='') as f:
    writer = csv.writer(f)
    writer.writerow(labels)
    writer.writerows(as_matrix)

def make_matrix(file_name):
  #as_matrix=np.zeros((2**16,2*16))
  as_matrix=np.zeros((16,16))
  with open(file_name) as f:
    reader = csv.reader(f)
    for row in reader:
      for i in range(1,len(row)-1):
        as_matrix[int(row[i])][[int(row[i+1])]]+=int(row[0])
        as_matrix[int(row[i+1])][[int(row[i])]]+=int(row[0])
  return as_matrix

if __name__ == "__main__":
    main()