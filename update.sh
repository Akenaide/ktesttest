#!/bin/sh

echo "yay"

sleep 2
MYDATE=`date -I`
git checkout -b $MYDATE
git add .
git commit -m $MYDATE
git push
hub pull-request -m $MYDATE

echo "end"
