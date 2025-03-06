#!/usr/bin/env bash

finished=0
while [ $finished -ne 1 ]; do
  echo "Enter your linux distro"
  read distro

  case $distro in
    1)
      echo "numvber";;
    'Arch')
      echo "I am using arch by the way";;
    "Fedorea")
      echo "Red hat slave's";;
    "CachyOS")
      echo "U are the best"
      echo "cool";;
    0) finished=1;;
    *)
      echo " windows is trash"
  esac
done

