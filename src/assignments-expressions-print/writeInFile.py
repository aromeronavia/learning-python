#There are several ways
import sys

def main():
  #print in console
  print "stufferino"
  #Open a file
  file = open("file.txt","a")
  temp = sys.stdout
  sys.stdout = file
  #Print in a file
  print "stufferino in a file"
  sys.stdout = temp
  
  #print again in console
  print "hello moto"

  #The other way is to specify with >> the object where you are gonna
  #print (The object must have a write method because of polymorphism)
  
  #print >> open, "Hello motorola from >>"

main()
