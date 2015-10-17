def main():
    #There is no such a thing as switch in python, so there are at least two ways to
    #perform a multioption desition
   
    #Lets say we have a value 
    value = int(raw_input())

    #First scheme: if elif 
    if_elif(value)

    #Second scheme: maps
    maps(value)
    
    #Additional: You can put more than 1 statements in one line, just in the case they are separated by ;
    x = 1; x = 2; x = 3
    
    #Whiles can have an optional else
    while 0:
      print x
    else:
      print value
    
    #Weird sentence to do nothing: pass
    pass

#Boring stuff
def if_elif(value):
    if value == 3:
      print "Super 3"
    elif value == 4:
      print "Fucking 4"
    else:
      print "Go fuck yourself"
    
def maps(value):
  print {3:"Super 3",
         4:"Super 4"}.get(value)

main()
