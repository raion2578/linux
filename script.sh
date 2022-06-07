#!/bin/bash

if [ "$#" -ne 4 ]
then
    echo "$0 <Height> <Weight> <fill or not (0\1)> <Char>"
    exit 1
fi

Height=$1
Weight=$2

if [ $3 -eq 0 ]
then
    sym=' '
else
    sym=$4
fi

for (( i = 1; i <= $Height; i++ )); do
  for (( j = 1; j <= $Weight; j++ )); do
    if (( 1 == i || $Height == i || 1 == j || $Weight == j )); then
      echo -n $4
    else
      echo -n "$sym"
    fi
  done
  echo
done
