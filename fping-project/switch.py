#!/usr/bin/python
import csv
from prettytable import PrettyTable
from collections import defaultdict

columns = defaultdict(list) # value in each column is appended to a list

# test_fping.txt contains a list of IP addresses that are considered active from the fping command
# done before switch.py runs
read_this = open("test_fping.txt", "r")
file_ip = read_this.read().split('\n')
read_this.close()

# inputs are used so that any csv file containing the needed information can be used so long 
# as the name of the columns are known by the user
file_csv = raw_input("Enter the file name (must be a spreadsheet converted into a csv file):     ")
first_c = raw_input("Enter the name of the column that the IP Addresses are stored in the sheet:        ")
second_c = raw_input("Enter the name of the column that the switches are stored in the sheet:   ")

# returns csv file as a dictionary where column names are keys and items in the column are values put into a list
with open(file_csv + '.csv') as f:
        reader = csv.DictReader(f) # read rows in dictionary format
        for row in reader:
                for (k,v) in row.items(): # goes over each column name and value
                        if not '' in columns[k]:
                                columns[k].append(v)

sheet_ip = columns[first_c]
sheet_switch = columns[second_c]

active_switch = []

# assuming that all IPs in the file have one switch, whether it is publicly assigned, 'unused', or reserved
for s in sheet_ip:
        if s in file_ip:
                active_switch.append(sheet_switch[sheet_ip.index(s)])

# used to print results in a more readable format
x = PrettyTable(["Active Switches"])
for switch in active_switch:
        x.add_row([switch])
print(x)
