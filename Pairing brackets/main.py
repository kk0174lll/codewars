'''
Write a function which outputs the positions of matching bracket pairs. The output should be a dictionary with keys the positions of the open brackets '(' and values the corresponding positions of the closing brackets ')'.
For example: input = "(first)and(second)" should return {0:6, 10:17}
If brackets cannot be paired or if the order is invalid (e.g. ')(') return False. In this kata we care only about the positions of round brackets '()', other types of brackets should be ignored.
'''


def bracket_pairs(string):  
  stack = []
  result = {}
  for i, c in enumerate(string):
    if c == "(":
      stack.append(i)      
    elif c == ")":
      if len(stack) > 0:
        result[stack.pop()] = i
      else:
        return False 
   
  if  len(stack) > 0:         
    return False
  else:
    return result
def main():  
  print(bracket_pairs("(a(b)c()d)"))
 
main()