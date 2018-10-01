""" Program is tested using decimal to binary converter
    https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=69 
    Program is based on 
    https://www.geeksforgeeks.org/program-decimal-binary-conversion/ """

binary = input("Please enter a number:      ")
countOne = 0
countZero = 0
b = int(binary)

while b != 0:
    if b % 2 == 0:
        countZero += 1
        b = b/2
    else:
        countOne += 1
        b = b//2

print("There are " + str(countOne) + " ones and " + str(countZero) + " zeros in this number's 
       binary form, which is "+ str(bin(int(number))[2:].zfill(1)))
