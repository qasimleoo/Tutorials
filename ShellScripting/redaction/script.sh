#!/bin/bash

FILE_NAME=$1
TOKEN="9Xxx6qsa4yfR8z7H"
URL="https://whois.whoisfreaks.com/add-to-reducted-domains?token=$TOKEN&domain="

if [[ $# -lt 1 ]]
then
	echo "Please pass file path containing domains in argument with one domain per line"
	echo "Usage: ./script.sh FILE_CONTAINING_DOMAINS"
	exit 1
fi


for DOMAIN in $(cat $FILE_NAME)
do
	echo "------------------------------------------------------------------------------------------------------------------"
	echo "Domain: $DOMAIN"

	$( curl -X PUT "$URL$DOMAIN" -H "Content-Type: application/json" -d "{\"domain\": \"$DOMAIN\", \"token\": \"$TOKEN\"}"  )
	
	if [[ $? -eq 0 ]]
	then
		echo "WHOIS info obfuscated for: $DOMAIN"
	else
                echo "Failed to obfuscate WHOIS for: $DOMAIN"
	fi
	echo "------------------------------------------------------------------------------------------------------------------"
done
