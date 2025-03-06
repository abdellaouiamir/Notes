#!/usr/bin/env bash

os=/etc/os-release
logfile=./log
errorfile=./error

check() {
  if [ $? -eq 0 ]; then
    echo "nice" 
    return 0
  else
    echo "sad"
    return 1
  fi
}
bad() {
  return 1
}
if grep -q "CachyOS" $os; then
  echo "this is cachyos" >>$logfile 2>>$errorfile
  #bad
  check
elif grep -q "Ubuntu" $os; then
  sudo apt update >>$logfile 2>>$errorfile
  check
else
  echo "unsupported os"
fi
