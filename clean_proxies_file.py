import os
import csv

file = "proxies.csv"
port_col = 26
ip_col = 34

with open(file, "r") as inFile, open("cleaned_proxies.txt", "w") as outFile:
    rows = csv.reader(inFile, delimiter=",", quotechar='"')
    
    for row in rows:
        ip = row[ip_col]
        port = row[port_col]
        outFile.write(f"{ip}:{port}\n")
        