"""
Using lambda expressions


"""

def main():
  square = lambda x: x**2
  print square(5)
  #Nesting lambdas
  nested = (lambda x: (lambda y: x+y))
  nested = nested(2)
  print nested(3)


main()
