#!/bin/bash

mkdir txt
for f in ./out/*; do
  f1=`echo "$f" | sed s/out/txt/g | sed s/pcap/txt/g`
  s=$(echo "$f1")
  touch $s
  tshark -r $f | cut -b 18-60 | cut -f 1 -d " " | sort | uniq -c | sort -nr >> $s
done
