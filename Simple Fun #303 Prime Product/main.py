'''
We know that some numbers can be split into two primes. ie. 5 = 2 + 3, 10 = 3 + 7. But some numbers are not. ie. 17, 27, 35, etc..

Given a positive integer n. Determine whether it can be split into two primes. If yes, return the maximum product of two primes. If not, return 0 instead.

Input/Output
[input] integer n

A positive integer.

0 ≤ n ≤ 100000

[output] an integer

The possible maximum product of two primes. or return 0 if it's impossible split into two primes.

Example
For n = 1, the output should be 0.

1 can not split into two primes

For n = 4, the output should be 4.

4 can split into two primes 2 and 2. 2 x 2 = 4

For n = 20, the output should be 91.

20 can split into two primes 7 and 13 or 3 and 17. The maximum product is 7 x 13 = 91
'''
import math
def prime_product(n):
  if n<4:
    return 0
  left = 0
  result = 0
  right = 1
  while right <= n/2:
    left = n - right
    if is_prime(left) and is_prime(right):
      if left*right>=result:
        result = left*right
    right=right+1
  return result
def is_prime(n):
  if n == 0 or n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0 and n > 2: 
    return False  
  if n<200 :
    prims = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
    137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    return n in prims
  a = int(math.sqrt(n))
  for i in range(3,  a + 1, 2):
    if n % i == 0:
      return False
  return True

def main():  
  print(prime_product(6))
 
main()  