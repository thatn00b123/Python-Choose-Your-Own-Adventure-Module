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
:raw-html:`<br />`
``Test ()``: Test class, nothing to see here!
:raw-html:`<br />`
:raw-html:`<br />`
``ChoiceError(Exception) (obj, message="is not a valid choice, text or ending object!")``: Custom error for Choice related things.
:raw-html:`<br />`
:raw-html:`<br />`
``Choice (name: str, txt: str, onchoose: callable, children: list)``: Class for making choices.
    ARGS:
        - name:string: Name of choice that appears when its parent choice's ``run(self)`` function is called.
        :raw-html:`<br />`
        - txt:string: Text that appears when the choice is selected.
        :raw-html:`<br />`
        - onchoose:function: Function that is ran when the choice is selected.
        .. note::
            Set to ``None`` or ``pass`` if you don't want to call a function!
        :raw-html:`<br />`
        - children:list: List of child Choices, Texts or Endings that can be chosen from.
    VARIABLES:
        - name: set to {ARG:'name'}
        - txt: set to {ARG:'txt'}
        - funct: set to {ARG:'onchoose'}
        - children: set to {ARG:'children'}
        - parent: set to ``None`` (for every object in its "children" list, it sets their parent to itself)
        :raw-html:`<br />`
    FUNCTIONS:
        - ``run(self)``: Is called when it is selected, and causes the pointer to move foreward.
:raw-html:`<br />`
``Text (name: str, txt: str, nxtobj)``: Class for text buffers.
    ARGS:
        - name:string: Name of text that appears when its parent choice's ``run(self)`` function is called.
        - txt:string: Text that appears when the choice is selected.
        - nxtobj: Object that pointer is passed to after text is printed.
    VARIABLES:
        - txt: set to {ARG:'txt'}
        - nxt: set to {ARG:'nxtobj'}
    FUNCTIONS:
        - ``run(self)``: Is called when it is selected, and causes the pointer to move foreward.
:raw-html:`<br />`
``Ending (name: str, endname: str, txt: str, sayend = False)``: Class for making endings.
    ARGS:
        - name:string: Name of ending that appears when its parent choice's ``run(self)`` function is called.
        - endname:string: Name of ending that appears in endings list and at end.
        .. note::
            ("The" and "Ending" are automatically appended to the beggining and end of endname, so endname only has to be the name (ex: endname = Good, output: You Have Achived: The Good Ending!)
        - txt:string: Text that appears when the ending is selected.
        - sayend(False):boolean: determines if "[ENDING]" is appended to the begining of the ending's name (NAME not ENDNAME!)
    VARIABLES:
        - name: set to {ARG:'name'}
        - sayend: set to {ARG:'sayend'}
        - endname: set to {ARG:'endname'}
        - txt: set to {ARG:'txt'}
    FUNCTIONS:
        - ``run(self)``: Is called when it is selected, and causes the game to end, adds the ending to ``gotendings[]``, and asks the player if they want to play again.
