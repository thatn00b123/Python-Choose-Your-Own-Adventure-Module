.. role:: raw-html(raw)
    :format: html

*****
**Usage**
*****



Variables
*****
:raw-html:`<br />`
variables:dict: Dictionary for storing variables and their values
:raw-html:`<br />`
:raw-html:`<br />`
endings:list: List for storing possible endings
:raw-html:`<br />`
:raw-html:`<br />`
gotendings:list: :List for storing endings the player has achived
:raw-html:`<br />`
:raw-html:`<br />`
start:choice, text, or ending object: Starter choice, text or ending that will run when ``starter()`` is called.
.. warning::
  (SET THIS BEFORE STARTER FUNCTION OR GAME WILL BREAK!)

:raw-html:`<br />`

Functions
*****
:raw-html:`<br />`
``makevar(varname: str, defaultval = 0, raiseerror = False)``: Create a variable that can be used in a choice object
  ARGS:
    - varname:string: Name of the variable
    - defaultval(0): default value of variable (default is 0)
    - raiseerror(False): determines if an error will be raised if the variable already exists
:raw-html:`<br />`
``setvar(varname: str, value, raiseerror = False)``: Set a variable's value
  ARGS:
    - varname:string: Name of variable
    - value: Value the variable will be set to
    - raiseerror(False): determines if an error will be raised if the variable doesn't exist
:raw-html:`<br />`
``getvar(varname, raiseerror = False)``: Get a variable's value
  ARGS:
    - varname:string: Name of variable
    - raiseerror(False): determines if an error will be raised if the variable doesn't exist
:raw-html:`<br />`
``starter()``: Function that starts the game by running the choice, text or ending object saved in the "start" variable's ``run(self)`` function.
.. warning::
  YOU HAVE TO SET THE "START" VARIABLE BEFORE THE ``starter()`` FUNCTION IS RAN, OR THE GAME WILL NOT RUN!
:raw-html:`<br />`
``getth(n: int)``: simple function to return the "th" of a number (ex 1 = st, 2 = nd, 3 = rd, n>3 = th)
  ARGS:
    - n:integer: Number that the funtion will get the "th" of
    
:raw-html:`<br />`
:raw-html:`<br />`

Objects
*****
