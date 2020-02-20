'''
Sequence
Consider an integer sequence U(m) defined as:

m is a given non-empty set of positive integers.
U(m)[0] = 1, the first number is always 1.
For each x in U(m), and each y in m, x * y + 1 must also be in U(m).
No other numbers are in U(m).
U(m) is sorted, with no duplicates.
Sequence Examples
U(2, 3) = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
1 produces 3 and 4, since 1 * 2 + 1 = 3, and 1 * 3 + 1 = 4.

3 produces 7 and 10, since 3 * 2 + 1 = 7, and 3 * 3 + 1 = 10.

U(5, 7, 8) = [1, 6, 8, 9, 31, 41, 43, 46, 49, 57, 64, 65, 73, 156, 206, ...]
1 produces 6, 8, and 9.

6 produces 31, 43, and 49.

Task:
Implement n_linear or nLinear: given a set of postive integers m, and an index n, find U(m)[n], the nth value in the U(m) sequence.

Tips
Tests use large n values. Slow algorithms may time-out.
Tests use large values in the m set. Algorithms which multiply further than neccessary may overflow.
Linear run time and memory usage is possible.
How can you build the sequence iteratively, without growing extra data structures?
'''
import time
def n_linear(m,n):
  print(m)
  print(n)
  l = len(m)
  idx = [0]*l
  q = list()
  res = list()
  for i in range(l):    
    q.append([])
    q[i].append(m[i]+1)
  cnt = 0
  while(cnt != n):
    min = 9223372036854775807
    for i in range(l):
      if (q[i][0]<min):
        min=q[i][0]
    res.append(min)
    for i in range(l):
      if (q[i][0]==min):
        q[i].pop()
        idx[i] = idx[i]+1
        q[i].append(res[idx[i]-1] * m[i] + 1)
    cnt = cnt+1
  if(len(res)==0):
      return 1
  else:
      return res.pop()


def main():  
  print(n_linear([2,3], 0))
  #8671468 should equal 7202134
start_time = time.time()  
main()
print("--- %s seconds ---" % (time.time() - start_time))

'''
inefficient

def n_linear(m,n):
  print(m)
  print(n)
  m.sort()
  list = []
  list.append(1)
  for i in range(n):           
    x = list[i]
    for y in m:      
      value =   x * y + 1      
      len_list = len(list)
      if len_list>n:
        if (list[n]>value):          
          insert(value, list,i, n)          
      else:
        insert(value, list,i, len_list)   
            
  return list[n]


def insert(value, list, left, right):  
  mid = 0  
  while(not left>=right):
    mid = left + (right-left)//2
    if(list[left]==value or list[mid]==value):      
      return False    
    if list[mid]>value:
      right = mid
    else:
      left = mid+1
  list.insert(left, value)
'''