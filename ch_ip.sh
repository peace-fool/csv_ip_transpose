#!/bin/bash

#Grepping all the IP addresses from the file
grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' ./test.csv > ./orig_ip

#Getting unique IPs
uniq ./orig_ip > ./u_ip
#Transposing the new IPs
tr 0-9 1-90 < ./u_ip > ./r_ip
#making a new csv file out of unique and transposed IPs files
paste -d ',' u_ip r_ip > fin.csv
#Adding headers for the csv file
sed -i '1i FIND,REPLACE' fin.csv
#Removing the temperory files
rm u_ip r_ip orig_ip
#Running python3 script
python3 rep.py
#Removing Temporary files
rm fin.csv
