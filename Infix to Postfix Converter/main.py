'''
Construct a function that, when given a string containing an expression in infix notation, 
will return an identical expression in postfix notation.
The operators used will be +, -, *, /, and ^ with standard precedence rules and
left-associativity of all operators but ^.
The operands will be single-digit integers between 0 and 9, inclusive.
Parentheses may be included in the input, and are guaranteed to be in correct pairs.
'''
def toPostfix(expr):
    result = ''
    stack = []
    
    for c in expr:
      if c.isdigit():
        result = result + c
      elif  c == "(":
        stack.append(c)
      elif  c == ")":
        result = processClosingBracket(result, stack)
      else:
        result = process(c, result, stack)      
    while len(stack) != 0:
      result = result + stack.pop()
    return result

def processClosingBracket(result, stack):
  flag = True
  while(flag):
    symbol = stack.pop()
    if symbol != "(":
      result = result + symbol
    else: 
      flag = False
  return result

def process(c, result, stack):
  precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
  flag = True  
  while(flag and len(stack) > 0):
    operation = stack[len(stack)-1]
    if precedence[operation] >= precedence[c]:
      result = result + stack.pop()
    else:
      flag = False
  stack.append(c)
  return result

def main():
  print(toPostfix("(5-4-1)+9/5/2-7/1/7"))
 
main()