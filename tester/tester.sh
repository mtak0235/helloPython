#!/bin/bash

for user in $*
do
commit_count = 0
git checkout $user
git log --since=1.weeks --pretty=format:"%cr : %s" --grep "\[" | sort -k 3 > log.txt
cat log.txt
$commit_count $(cat log.txt | wc -l)
if `cat log.txt | wc -l` > 5
then
	echo -e "\033[32m$user passed over $commit_count\033[0m"
else
	echo -e "\033[35m$user goes vacation\033[0m"
fi
done
rm log.txt

