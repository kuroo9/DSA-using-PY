#reversing a number>> the hard way
n=12345
num=n
while(num>0):
    dig=num%10 #remainder dega ye ie.the last number.
    print(dig)
    num=num//10 #flor div to avoid decimal

