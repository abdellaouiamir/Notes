#!/usr/bin/env bash

for i in {1..10}; do
  echo $i
  break 
done

for i in `seq 1 10`; do
  echo $i
done

for i in 1 2 3 4 5 6 7 8 9 10; do
  echo $i
done

for i in {A..D}; do
  echo $i
done

for file in ./*; do
  echo $file
done

for ((i=0;i<10;i++)); do
  echo $i
done
