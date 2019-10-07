'''
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
'''
import math

def narcissistic( value ):
  if value//10==0:
    return True
  pow = 0
  digets=[]
  n = value
  while (n>0):
    digets.append(n%10)
    n = n//10
    pow = pow+1
  sum = 0
  for d in digets:
    sum = sum + math.pow(d, pow)
  if sum==value:
    return True
  else:
    return False  
def main():  
  print(narcissistic(4887))
 
main()