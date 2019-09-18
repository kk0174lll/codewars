'''
A generalization of Bézier surfaces, called the S-patch, uses an interesting scheme for indexing its control points.
In the case of an n-sided surface of degree d, each index has n non-negative integers that sum to d, and all possible configurations are used.
For example, for a 3-sided quadratic (degree 2) surface the control points are:
indices 3 2 => [[0,0,2],[0,1,1],[0,2,0],[1,0,1],[1,1,0],[2,0,0]]
Given the degree and the number of sides, generate all control point indices. The order of the indices in the list can be arbitrary, so for the above example
[[1,1,0],[2,0,0],[0,0,2],[0,2,0],[0,1,1],[1,0,1]]
is also a good solution.
'''

def indices(n, d):
  if d == 0:
    return [[0] * n]
  elif n == 1:
    return [d]   
  elif d == 1:
    result=[]
    for i in range(0, n):
      element = [0] * n
      element[i] = 1
      result.append(element) 
    return result   
  elif n == 2:
    return [[i, d-i] for i in range(0, d+1)]    
  elif n > 2:
    result =[]    
    for i in range(0, d+1):          
      lower_dim = indices(n-1, d-i)                
      for element in lower_dim:
        element.extend([i])            
        result.append(element)            
  return result

def main():  
  print(indices(3, 4))  
main()