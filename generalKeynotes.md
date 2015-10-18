Chapter 10: Key Notes.

ZIP: Can mix arrays in tuples for make a parallel iteration
EXAMPLES:
===================================================
>>> L1 = [1,2,3,4]
>>> L2 = [5,6,7,8]

>>> zip(L1,L2)
[(1, 5), (2, 6), (3, 7), (4, 8)]

>>> for (x,y) in zip(L1, L2):
...     print x, y, '--', x+y
...
1 5 -- 6
2 6 -- 8
3 7 -- 10
4 8 -- 12

This can be useful for maps:
When we already have a list of keys and values, and we just want to
build a map with those values, we can use the ZIP function to bind
them and assign them into a map

keys = ["super","man"]
uperMap = values = [1,2]

superMap = {}
for (k,v) in zip(keys, values): superMap[k] = v

OR THERE IS SOMETHING SOOOO BEAUTIFUL!
D3 = dict(zip(keys, vals))


===================================================
Structure of a for loop

for <target> in <object>:   # Assign object items to target.
    <statements>            # Repeated loop body: use target
else:
    <statements>            # If we didn't hit a 'break

A string can be iterable

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chapter 11 - Functions

About functions:
  Arguments are passed by assignment (object reference)
    
  global declares module-level variables that are to be assigned.
    With global, we can do an assignment to a module level instead to a function level
 
  Arguments, return values, and variables are not declared.
    

Structure:
  def <name>(arg1, arg2,... argN):
    <statements>

=============================================================
def in runtime:
  def executes in run time, it can be run from any part of a module


using this schema can amplify our polymorphism scope to any project using a multicase functional function (lol)


Chapter 13 - Scopes and Arguments

Scope are the visibility of your vars inside a program

Hierarchy of scope:
Module --- world level (files, packages, folders, etc)
  Global --- file level
    Function call (each of them has an own namespace) --- function level
            

Summary: 
    Name references search at most four scopes: local, then enclosing functions (if any), then global, then built-in.
    Name assignments create or change local names by default.
    Global declarations map assigned names to an enclosing modules scope.


========================================================================
  Examples:

x = 3

def method():
  x = 4

print x
==================  result : 3
x = 3

def method(): 
  global x 
  x = 4

print x

==================  result : 4


Special argument matching modes:
 
  In traditional programming languages, we match the arguments we introduce in our function calls with the order of the arguments
  in the function definition, but in Python there are more ways to match the parameters with the arguments, these are:

  1. Positionals: matched left to right (the classic one)
  2. Keywords: matched by argument name
    >>> f(c=3, b=2, a=1)
    1 2 3

     NOTE: Using this kind of matching allows the programmer to document the code (using better vars and stuff). A clear example of this:
     func(name='Bob', age=40, job='dev')


  3. Varargs: catch unmatched positional or keyword arguments
  4. Defaults: specify values for arguments that arent passed

Examples: 

  func( *name )
  Function
  Matches remaining positional args (in a tuple)

  def func( **name )
  Function
  Matches remaining keyword args (in a dictionary)


IMPORTANT RULES:
    In a call, all keyword arguments must appear after all non-keyword arguments.

    In a function header, the *name must appear after normal arguments and defaults, and **name must appear last.


Chapter 14 - Advanced function topics

map() built-in doesnt truncate data
zip() does (random post)

============Lambda Expressions====================

  lambda is an expression, not a statement
  lambda bodies are a single expression, not a block of statements

These are used in a lot of contexts, where we dont wanna waste our time building an entire function because it will only be used one
See more examples in 





