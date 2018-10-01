#!/usr/bin/python

print "--- Welcome to Fibbonacci Time! ---"
looper = True
while looper:

        f = raw_input("Please enter the number you want to go up to or press 'q' to quit:       ")
        if f == 'q':
                looper = False
        else:
                print "Here are your number(s): "
                print "------------------------------------------------------------------"
                if int(f) == 0:
                        print "0"
                elif int(f) == 1:
                        print "0 \n1 \n1"
                else:
                        a = b = temp = 1

                        print 0
                        print 1
                        for a in range(int(f)):
                                a = b
                                b = temp + b
                                temp = a
                                if a > int(f):
                                        break
                                else:
                                        print a
