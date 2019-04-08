#! /bin/bash

problem=("a" "b" "c" "d" "e" "f" "g" "h" "i")


if [ $# -ne 2 ]; then
  echo "指定された引は$#個です" 1>&2
  echo "実行するには2個の引数が必要です" 1>&2
  exit 1
fi

mkdir $1;
for i in `seq 0 $(($2-1))`
  do
    touch $1/"${problem[i]}".py
    cat template.py >> $1/"${problem[i]}".py
  done

