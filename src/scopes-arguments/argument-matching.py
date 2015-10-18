"""
Examples of special argument matching modes

"""
def main():
  #Keywords
  sum(b=2, a=1)
  #Default values
  sum2() 
  #Varargs
  vararg(1,2,3,4,5)  

#Keywords: matched my argument name
def sum(a, b):
  print a, b,
  return a+b

def vararg(*args):
  print args



def sum2(a=1, b=2, c=3):
  print a, b, c,
  return a+b+c

main()
