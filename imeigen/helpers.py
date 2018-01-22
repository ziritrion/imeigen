#!/usr/bin/python3

#import sys
from luhn import *

#'Static' vars
MAXIMEIAMOUNT = 1000000
TACLENGTH = 8
TAILLENGTH = 6

#gets TAC from user and validates input
def checktac():
    while True:
        try:
            tac = input('TAC: ')
        except ValueError:
            print('Invalid input; try again.')
            continue
        if len(tac)!=TACLENGTH or not(tac.isdigit()):
            print('The TAC value must be 8 digits long.')
            continue
        else:
            break
    return tac

#generates imei list from tac. Size of list equals amount. Startvalue points to the first 'tail' to be generated. If the amount is too much, it will reduce the final amount.
def generateimeilist(tac, amount, startvalue):
    i = 0
    ret = list()
    #print('Amount: ', amount)
    #print('Start at: ', startvalue)
    #print('Formula: ', MAXIMEIAMOUNT-startvalue)
    if (MAXIMEIAMOUNT-startvalue)<amount:
        print('Amount is too big; setting amount to max possible')
        amount=MAXIMEIAMOUNT-startvalue
    while i < amount:
        imei = append(tac + createnumberwithzeros(startvalue))
        ret.append(imei)
        print(imei)
        startvalue+=1
        i+=1
    return ret

#creates a number with zeroes to the left
#TODO: tail control is awful and should probably be redone
def createnumberwithzeros(number):
    #maxlength = 6
    ret = str(number)
    i = len(ret)
    print('Number: ', number)
    print('Length: ', i)
    if i> TAILLENGTH:
        print('Tail is longer than 6 digits; setting tail to zero.')
        i = 1
        ret="0"
    while i < TAILLENGTH:
        ret = "0"+ret
        i+=1
    return ret

#--------
# TESTING STUFF BELOW
#--------
#tac = checktac()
#print('TAC is ', tac)
#print('IMEI list:')
#generateimeilist(str(12345678), 5, 999996)
#print(generateimeilist(str(12345678), 100001, 0))
