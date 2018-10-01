#!/bin/sh

echo "Hello! Let's get started!"

# To make sure fping works, the user must know the range of the IP addresses they want to ping
read -p "Enter the starting IP you want to ping: " start
read -p "Enter the ending IP you want to ping: " end

fping -a -r 0 -g $start $end > test_fping.txt

# the code for switch.py is available in the repository
python switch.py
