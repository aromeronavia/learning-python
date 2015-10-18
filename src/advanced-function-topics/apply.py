"""
Apply command: it is used to call functions with two parameters:
  The Name
  The arguments of the function
"""

def function(x):
  print "rofl", x

def main():
  x = 3
  apply(function,(x,))
  pargs = (1,2)
  kargs = {'a':3, 'b':4}

  #One way:
  apply(echo, pargs, kargs)

  #The easiest
  echo(0, *pargs, **kargs)

def echo(x, *pargs, **kargs):
  print x, pargs, kargs

main()
