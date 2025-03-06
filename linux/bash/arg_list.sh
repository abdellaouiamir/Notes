#!/usr/bin/env bash

if [ $# -eq 1 ]; then
  echo "one argument"
fi

echo $#
for i in $@
do
  echo "$i"
done

list=("a" "b" "c" )
for i in ${list[@]}; do
  echo $i
done
echo ${list[0]}
echo "///////////////////////////////////////"
for ((i = 0; i < 10; i++)); do
  echo "$i"
done
echo $((3+3))
