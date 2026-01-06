#!/bin/bash
#$Revision:001$
#$Sun Sep 21 12:37:00 PKT 2025$
#
#
# Variables
BASE=/home/leo/ShellScripting/archive_script
DAYS=10
DEPTH=1
RUN=0

# Check if directoy is present or not
if [[ ! -d $BASE ]]
then
	echo "Directory doesn't exist: $BASE"
	exit 1
fi

# create archive folder if not present
if [[ ! -d $BASE/archive ]]
then
	echo "Creating archive directory"
	mkdir $BASE/archive
fi

#Find the list of files larger than 100MB/100000B or use M for MBs .. G for GBs 
for i in `find . -maxdepth 1 -type f -size +100000`
do
	if [[ $RUN -eq 0 ]]
	then 
		echo "[$(date "+%Y-%m-%d %H:%M:%S")] archiving $i ==> $BASE/archive"
		gzip $i || exit 1
		mv $i.gz $BASE/archive || exit 1
	fi
done

