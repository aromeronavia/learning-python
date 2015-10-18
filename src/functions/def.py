"""
Purpose:
    understand the def statement in runtime execution

def statement defines a function and assigns it to a name (obviously, the name of a function)

Lets do crazy stuff!
"""
from random import randint

def main():
  be = randint(0,1)
  if be:
    def being():
      print "I decided to be"

  else:
    def being():
      print "I decided to not be"

  being()

main()
