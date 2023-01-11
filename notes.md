# Notes for Automate the Boring Stuff

## Intro & Resources

Automate the boring stuff teaches you to use Python to write programs that do in minutes what would take you hours to do by hand. Use python to:

- Search for text in a file or across multiple files
- Create, update, move, and rename files and folders
- Search the Web and download online content
- Update and format data in Excel spreadsheets of any size
- Split, merge, watermark, and encrypt PDFs
- Send reminder emails and text notifications
- Fill out online forms
**Resources**
- Book Link: [Automate The Boring Stuff](https://automatetheboringstuff.com/#toc)
- Notes: [Markdown Guide](https://daringfireball.net/projects/markdown/)
- Markdown: [Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- Python Style Guide: [Python Style Guide](https://peps.python.org/pep-0008/)
- VisualStudioCode
- Scripts Directory on my MAC
- mu text editor

---

## Markdown

Markdown Extended syntax extension added to visual studio code: [Markdown Extended Readme](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended)

## Virtual Environment Setup for Python Projects

Information gained from working with Nick Moore on a Marco project. Set up a virtual env for installing requirements and running a script.

1. Create a project folder directory for a new project.
2. Under a project folder run command to create the virtual environment `python -m venv .venv/[projectName]`
3. After running the command should see .venv folder in the project directory.
4. To use the virtual environment in PS, run `.\.venv\[projectName]\Scripts\activate.ps1` to get to the directory.
5. Run `pip install -r requirements.txt` to install all the requirements in the virtual environment (assuming there was a requirements.txt installed otherwise justrun all the module installs manually).
6. In visual studio code, open the `..\[projectName]` directory and open a python file.
7. In the bottom right of VS code, select the Python version and the top middle should open ability to select 'enter interpreter path' and file browse into the `.\.venv\[projectName]\Scripts\python.exe` and select interpreter. Visual Studio Code should now switch bottom right value initially clicked on.

---

## CH1-2 Python Basics and Flow Control

---

### Math

| Operator | Operation                         | Example | Evaluates to . . . |
| -------- | --------------------------------- | ------- | ------------------ |
| **       | Exponent                          | 2 ** 3  | 8                  |
| %        | Modulus/remainder                 | 22 % 8  | 6                  |
| //       | Integer division/floored quotient | 22 // 8 | 2                  |
| /        | Division                          | 22 / 8  | 2.75               |
| *        | Multiplication                    | 3 * 5   | 15                 |
| -        | Subtraction                       | 2-May   | 3                  |
| +        | Addition                          | 2 + 2   | 4                  |

### Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

**The `and` Operator's Truth Table**
| Expression      | Evaluates to . . . |
| --------------- | ------------------ |
| True and True   | TRUE               |
| True and False  | FALSE              |
| False and True  | FALSE              |
| False and False | FALSE              |

**The `or` Operator's Truth Table**
| Expression     | Evaluates to . . . |
| -------------- | ------------------ |
| True or True   | TRUE               |
| True or False  | TRUE               |
| False or True  | TRUE               |
| False or False | FALSE              |

**The `not` Operator's Truth Table**
| Expression | Evaluates to . . . |
| ---------- | ------------------ |
| not True   | FALSE              |
| not False  | TRUE               |

### Loops

**Break**
Stops execution within the loop and exits the loop.
**Continue**
Stops executing the current loop and continues from the start of the loop.

```python3
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. Enter password: ')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```

Example above: while True is an infinite loop that only exits upon Joe entering correct name to continue to the password prompt and the loop will break if the password evaluates correctly.

Note: `0, 0.0,` and `''` will evaluate to `False`, while other values are considered True

```python3
name = ''
while not name:
    print('Enter name:')
    name = input()
print('How many guests will you have?')
numofGuests - int(input())
if numofGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')
```

Line 2 `while not name:` will evaluate to True when name is `''`. When a user enters any value at the prompt then the `name` variable will equate to false.
Line 7 `if numofGuests:` will be False if there are no guests `numofGuests=0` and the line will not be printed. If there is any number other than 0 then `numofGuests==True` the line will print.

`break` and `continue` can only be used inside `while` and `for` loops.

### for Loops and `range()`

`for i in range(5):` will loop 5 times (i.e., from 0 to 4). The variable i will go up to, but will not include, the integer passed to `range()`

**Start and Stop `range()`**
`for i in range(12, 16):` will loop for numbers `12, 13, 14, 15`

**Step `range()`**
The third argument `for i in range(0,10,2)` will indicate the amount that the variable is increased after each iteration. To decrease from high to low, use a negative number `for i in range(10,0,-1)` will decreate from 10 to 1. To include 0 use the stop number `-1`.

### Importing Modules

Python comes with a set of modules called the *standard library*. Each module is a python program that contains a related group of functions that can be imbeded in your program.
`import [moduleName], [moduleName2]`
Example: `import random, sys, os, math`
*Dont save python scripts with a name used by a python module*

**`from` `import` statements**
Alternative to `import` is `from [moduleName] import *`. Using `from random import *` will allow calls to functions in `random` to not need the `random` prefix.
Using the full name makes for more readable code.
*It is better to use the* `import random` *form of the statement vs* `import from random`.

### Ending a Program `sys.exit()`

Programs always terminate if the program execution reaches the bottom of the instructions. `sys.exit()` will allow program termination before the last instruction. `exit()` is in the `sys` module, so it has to be imported.
Example

```python3
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

### Summary Example Program: Rock, Paper, Scissors

```python3
import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables kep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop. Infinite loop.
    print('%s Wins, $s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playMove == 'p':
        print('PAPER versus...')
    elif playerMove =='s':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber ==1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber ==3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1'
```

---

## CH3 Python Functions

---

### A function definition `def`

Function is like a mini program within a program

```python3
def hello():
    print('Howdy!')
    print('Hi')
    print('Hello There.')

hello()
hello()
hello()
```

`def` defines the function named `hello()`
Code does not run until the function `hello()` is called on the last 3 lines.  When the function reaches the end of the function, it returns to the line that called the function and continues moving through the code as before.

Functions are necessary whenever you find yourself copy+paste code in multiple sections. It will be common to find yourself *deduplicating* code to get rid of duplicated or copy-and-paste code.

### `def` statements with Parameters

Functions can be passed values.

```python3
def hello(name):
    print('Hello, ' + name)

hello('Alice')
hello('Bob')
```

Output will be:

```python3
Hello, Alice
Hello, Bob
```

The value stored in parameters are forgotten when the function returns. Adding `print(name)` after `hello('Bob')` will return a `NameError` because there is no variable named `name` after the function returned.

### Define, Call, Pass, Argument, Parameter

**Define**: To *define* a function is to create it. `def` statement. Ex `def sayHello(name)`
**Call**: A function *call*s the created function and sends execution to the top of that *defined* function.
**Pass**: *Passing* a value to a function within a function call. `name` is passed to the function `sayHello()` with the function *call* `sayHello(name)`. *Passing* a value is the same as a function *call*.
**Argument**: The actual value being *passed* to a function is the *argument*. Variables that have arguments assigned to them are parameters.

### `None` Value Type

`None` (capital 'N' required) represents the absence of a value. It is the only value of the `NoneType` DataType. In other languages: `null` `nil` or `undefined`.
The `None` value-without-a-value is helpful when needing to store something that won't be confused for a real value in a variable. `None` is the return value of `print()`.
Python will add `return None` to the end of any function definition with no `return` statement or if `return` is used without a value. Similar how `while` or `for` loops end with a `continue` statement.

### Keyword Arguments and the `print()` Function

*Keyword arguments* are identified by the keyword put fefore them in the function call. They are often *optional parameters*
Example: `print()` function has optional parameters `end` (what should be printed at the end of its arguments) and `sep` (printed between arguments).

```python3
print('Hello')
print('World')
```

outputs:

```python3
Hello
World
```

But using the `end` optional parameter allows

```python3
print('Hello', end='')
print('World')
```

outputs:

```python3
HelloWorld
```

When passing multiple string values, the default is to separate with spaces, but you can change to commas like so:

```python3
>>> print('cats', 'dogs', 'mice')
cats dogs mice
```

vs using the `sep` keyword argument:

```python3
>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice
```

Keyword arguments can be added to functions I write, but list and dictionary data types are used (see next 2 chapters).

### The Call Stack

The current 'conversation' or execution is always at the top of the stack.
The *call stack* is how Python remembers where to return execution after each function call. Python creates a *frame object* on the top of the call stack. Frame objects store line number of original function call so Python knows where to return.
Visualize code with call stack behavior at [pythontutor.com](https://pythontutor.com/visualize.html#mode=display)
*Call Stacks* are important to remember when reviewing local and global scopes (in the next section).

### Local and Global Scopes

Parameters and variables assigned in a called function are said to exist in that function's *local scope* and called *local variables*. Variables assigned outside all functions are said to exist in the *global scope* and called *global variables*. A variable cannot be both local and global.
*scope* is a container for variables. When a *scope* is destroyed all values stored in the scope's variables are forgotten. There is only one global scope, and it is created when program begins. When global scope is destroyed, all its variables are forgotten.
Things to remember about *scopes*:

- Code in global scope, outside of all functions, cannot use any local variables.
- Code in a local scope can access global variables
- Code in a function's local scope cannot use variables in any other local scope
- You can use the same name for different variables if they are in different scopes. A local variable named `spam` and a global variable also named `spam`.

The reason for scopes: instead of just making everything a global variable is so when variables are modified by code in a particular call to a function, the function interacts with the rest of the program only though its parameters and the return value.
It is a bad habit to rely on global variables when programs get large.
It is best practice to use separate variable names in different scopes even if it is allowed. This makes troubleshooting easier and code more readable.

### Scopes: The `global` Statement

To tell a function to use the global instance of a variable vs creating a local instance of that variable, use

```python3
def spam():
    global eggs
    eggs = 'spam'

eggs = 'eggs global value'
spam()
print(eggs)
```

Eggs is set to `global value set` in the global scope, but then the `spam()` function uses the `global eggs` variable and changes it to `spam`. When eggs is printed, is used the global variable that the local function `spam()` changed and prints `eggs global value`.

A variable with either always be local or global. A function cannot create a local instance of the variable and then later use the global instance.
A global variable cannot just be used in a function without defining it with the global statement. If you try it will error:

```python3
def spam():
       print(eggs) # ERROR!
    ➊ eggs = 'spam local'

➋ eggs = 'global'
   spam()
```

This program will error as:

```python3
Traceback (most recent call last):
  File "C:/sameNameError.py", line 6, in <module>
    spam()
  File "C:/sameNameError.py", line 2, in spam
    print(eggs) # ERROR!
UnboundLocalError: local variable 'eggs' referenced before assignment
```

Writing functions without global variables is encouraged. That way each function can be treated like a 'black box'. You just feed it input and it gives you output.

### Exception Handling

Without exception handling, a Python program with an error with crash. Instead, write programs to detect errors, handle them, and continue to run.
Errors and handled with `try` and `except` statements.

---

## CH4 Lists

---

This chapter discusses lists and methods, which are functions tied to values of a certain data type. Lastly the sequence data types (lists, tuples, and strings) are covered and shown how they compare with each other. Next chapter is Dictionaries.

### List Data Type

*list* is a value that contains multiple values in an ordered sequence. The term *list value* referes to the list itself (a value stored in a variable or passed to a function), but not the values inside the list value.
*list value* looks like `['cat', 'bat', 'rat', 'elephant']`
Lists begin and end with square brackets `[]`
Values inside the list are also called *items*
*Items* are separated with commas (i.e., *comma-delimited*)

### List Indexes

`spam[0]` will evaluate to `'cat'` and `spam[1]` evaluates to `'bat'`
`spam = ['cat', 'bat', 'rat', 'elephant']`
Also `['cat', 'bat', 'rat', 'elephant'][3]` would be 'elephant'
**Lists can include other lists** as in a list of lists:

```python3
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```

### List Negative Indexes

`-1` references the last item in a list.
`-2` references the 2nd to last item in a list.
...and so on.

### Getting a List form Another List with Slices

A *slice* will get multiple values from a list using 2 values separated with a colon such as `spam[0:4]`. 1st iteger is the start index and the 2nd is where the slice ends (i.e., does not include that integer). `spam[0:4]` would return the full list of the 4 items `'cat', 'bat', 'rat', 'elephant'`
Leaving out an integer will indicate the start or end. `[:3]` is start of list and include indexes `0,1,2`. `[3:]` would start at the 3 index and return all values to the end of the list.

### List length with `len()`

`len()` will return the number of values that are in a list value passed to it, just as it can count number of characters in a string value.

```python3
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

### Changing Values in a List with Indexes

```python3
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]
```

### List Concatenation and List Replication

List concatenation and replication operates just like strings.
`+` operator combines 2 lists. `*` will replicate a list

```python3
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
```

### Remove Values from Lists with `del` Statements

`del` statement will delete values at an index in a list. Other values in the list will be moved up one index.

```python3
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
```

### List Best Practice

When using variables that could be grouped together, consider using a list to store the variables.

### `for` loops with Lists

```python3
for i in range(4):
    print(i)
```

output:

```python3
0
1
2
3
```

Python considers `range(4)` return value similar to `[0, 1, 2, 3]`. The following has the same output:

```python3
for i in [0, 1, 2, 3]:
    print(i)
```

Common List iteration technique: `for range(len(someList)):` to iterate over the indexes of a list.
Interactive shell example:

```python3
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for i in range(len(supplies)):
...     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

Using range(len(supplies)) is in example `for` loop is handy because the code in the loop can access the index (as the variable i) and the value at the index (as supplies[i]).

### `in` and `not in` Operators

`in` and `not in` are boolean values to determine is values are in a list.

```python3
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

### Multiple Assignment

*tuple unpacking* is a shortcut to assign multiple variables with the values in a list in one line.

```python3
projects = ['planning stage', 'in progress', 'complete']
new_project = projects[0]
current_project = projects[1]
old_project = projects[2]
```

The assignments above can be completed using `tuple unpacking`

```python3
new_project, current_project, old_project = projects
```

Number of vaiables and the length of the list must be exactly equal.

### `enumerate()` Function with Lists

`enumerate()` can be used instead of `range(len(someList))`
On each iteration of a `loop`, `enumerate()` will return
[1] The index of the item in the list
[2] The item in the list itself

```python3
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
... for index, item in enumerate(supplies):
...     print('Index ' + str(index) + ' in supplies is: ' + item)
```

`enumerate()` function is useful if you need both the item an dthe item's index in the loop's block.

### `random.choice()` and `random.shuffle()` Functions with Lists

`random.choice()` takes a list and returns a random element from the list.
`random.shuffle()` function will reorder the items in a list.

### Augmented Assignment Operators

| Augmented assignment statement | Equivalent assignment statement |
| ------------------------------ | ------------------------------- |
| spam += 1                      | spam = spam + 1                 |
| spam -= 1                      | spam = spam - 1                 |
| spam *= 1                      | spam = spam * 1                 |
| spam /= 1                      | spam = spam / 1                 |
| spam %= 1                      | spam = spam % 1                 |

### Methods

A *method* is the same as a function, except it is "called on" a value. For example, if a list value were stored in `spam`, you would call the `index()` list method like: `spam.index('hello')`. The method comes after the value, separated by a period.
Each data type has its own set of methods. The *list* data type has several methods for finding, adding, removing, and manipulating values in a list.

### `index()` Method

A value can be passed to a list and if the value matches, the index of that value will be returned.
Example:

```python3
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
```

*If there are duplicates, then the index for the 1st match will be returned.*

### Adding Values to Lists: `append()` and `insert()` Methods

`append` adds to the end of the list

```python3
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```

`insert()` receives the index location and the value to add to the list

```python3
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```

The **return** value of `append()` and `insert()` methods are `none`. The code does not assign method retuns to a variable. Do not use `spam = spam.append('moose')` because the list is modified in place.

Methods belong to a single data type. So `append()` and `insert()` are list methods and cannot be called on other values such as strings or integers.

### Removing Values from Lists: `remove()` Method

`remove()` method is passed the value to be removed from the list it is called on.

```python3
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```

*If the value appears, only the 1st instance will be removed.*

`del` keyword deletes all the elements in range starting from the index 'a' till 'b'. `del[a:b]`

```python3
mylist = list(range(10))
print('list is: ', mylist)
del mylist[3:5]
print('list after delete is: ',mylist)
```

will remove elements from index 3 up to but not including 5.

```python3
list is:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list after delete is:  [0, 1, 2, 5, 6, 7, 8, 9]
```

If you know the index of the element, it is good to use the keyword `del`. Use `remove()` method when you know the value you want to remove.

### Sorting Values in a List: `sort()` Method

Sort numberical or alphabetical order.

```python3
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

Keyword `reverse` can sort values in reverse order.

```python3
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

3 things to remember about `sort()`
[1] `sort()` method sorts items in place. Don't capture in return value.
[2] number values and string values cannot be sorted together
[3] `sort()` uses "ASCIIbetical order" rather than actual alphabetical order. Uppercase comes before lowercase (i.e., 'a' comes after 'Z')

```python3
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

Sorting values in regular alphabetical order, pass `str.lower` for the `key` keyword argument in the `sort()` method call:

```python3
 >>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```

Above, `str.lower` causes the `sort()` function to treat all items in the list as if they were lowercase without acually changing the values in the list.

### Reversing Values in a List: `reverse()` Method

Quickly reversing the order of the items in a list, you can call the `reverse()` list method.

```python3
>>> spam = ['cat', 'dog', 'moose']
>>> spam.reverse()
>>> spam
['moose', 'dog', 'cat']
```

`reverse()` also does not return a value.

### Exceptions to Indentation Rules for Lists

Python knows that a list is not finished until it sees the ending square bracket.

```python3
spam = ['apples',
    'oranges',
                    'bananas',
'cats']
print(spam)
```

A single instruction accross multiple lies can be done using the \ line continuation character

```python3
print('Four score and seven ' + \
      'years ago...')
```

### Example Program: Magic 8 Ball with a List

```python3
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
```

Using lists, the Magic 8 ball program can be written without all the elif statements.
The expression you use as the index for the list `messages` is `[random.randint (0, len(messages) -1)]` which produces a random number to use for hte index, regardless of the size of `messages`.

### Sequence Data Types

Lists are only 1 version of sequenced values. Strings can be considered a list of single text characters.
Python sequence data types include lists, strings, range objects returned by `range()`, and tuples. Many of the things you do with lists can also be done with strings and other values of sequence types: indexing; slicing; and using them with `for` loops, with `len()`, and with the `in` and `not in` operators.
String Example:

```python3
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
...     print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
```

### Mutable and Immutable Data Types

Lists and Strings are different in that a list is *mutable* data type: it can have values added, removed, or changed.
A string is *immutable*: it cannot be changed.
*Mutable* strings need to be changed by building a new string by copying the parts of the old string.

```python3
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```

Lists can be either changed or overwritten since lists are mutable.
List Example where an entirely new and different list value is overwriting the old list value:

```python3
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
```

To modify the original list, would have to do:

```python3
>>> eggs = [1, 2, 3]
>>> del eggs[2]
>>> del eggs[1]
>>> del eggs[0]
>>> eggs.append(4)
>>> eggs.append(5)
>>> eggs.append(6)
>>> eggs
[4, 5, 6]
```

Mutable versus immutable types are important with reviewing 'Passing References'

### Tuple Ummutable Data Type

A tuple is identical to the list data type, except in 2 ways.
[1] tuples use () vs []
[2] tuples cannot have their valued modified, appended, or removed.
If only one value in a tuple, put a comma after the 1st value:

```python3
>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>
```

Tuples are used to convey in code that you don't intend for that sequence of values to change.
**Tuple Benefits** include Python's implementation of optimizations that make code using tuples slightly faster than code using lists.

### Converting Types with the `list()` and `tuple()` Functions

Just like str(42) will return the string representation of the integer 42, the functions list() and tuple() will reurn the list and tuple versions of the values passed to them.

```python3
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```

### References to Values

**Strings and Integer References**
Variables "store" strings and integer values... But Python is actually using variables to store references to the computer memory locations where the values are stored.

```python3
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
```

When creating `spam` variable. 42 is created in memory and `spam` is a reference to the location in memory where `42` is located. When `spam` is assigned to `cheese`, the reference to the memory location of `42` is copied to `cheese`. Later when changing the value of spam to 100, 100 is created in memory and the reference to 100 is stored in `spam`.
Changing variables for strings and integers are not changing values in memory, but making it refer to a completely different value in memory.

**List References**
Lists don't work this way because list values can change (i.e., lists are mutable).

```python3
➊ >>> spam = [0, 1, 2, 3, 4, 5]
➋ >>> cheese = spam # The reference is being copied, not the list.
➌ >>> cheese[1] = 'Hello!' # This changes the list value.
   >>> spam
   [0, 'Hello!', 2, 3, 4, 5]
   >>> cheese # The cheese variable refers to the same list.
   [0, 'Hello!', 2, 3, 4, 5]
```

This code only changed the cheese list, but both `cheese` and `spam` lists changed.
In 1, list is created and reference assigned to the `spam` variable.
In 2, reference in `spam` is copied to `cheese`. Only the reference is copied, not the list value itself.
Now, `spam` and `cheese` refer to the same list values. There is only 1 underlying list.
In 3, so when the first element is modified in `cheese`, the same list is modified that `spam` refers to.

Python technically contain references to values, people often casually say that the variable contains the value.

### Identity and the `id()` Function

`id()` will return the unique identity of each Python value stored in memory.

```python3
>>> id('Howdy') # The returned number will be different on your machine.
44491136
```

Python picks address based on which memory bytes happen to be free on your computer at the time, so it'll be different each time you run code.

Immutable strings `id()`

```python3
>>> bacon = 'Hello'
>>> id(bacon)
44491136
>>> bacon += ' world!' # A new string is made from 'Hello' and ' world!'. 
>>> id(bacon) # bacon now refers to a completely different string.
44609712
```

Mutable lists `id()`

```python3
>>> eggs = ['cat', 'dog'] # This creates a new list.
>>> id(eggs)
35152584
>>> eggs.append('moose') # append() modifies the list "in place".
>>> id(eggs) # eggs still refers to the same list as before.
35152584
>>> eggs = ['bat', 'rat', 'cow'] # This creates a new list, which has a new
identity.
>>> id(eggs) # eggs now refers to a completely different list.
44409800
```

Python *automatic garbage collector* deletes any values not being referred to by any variables to free up memory.

### Passing References

References are important to understand how arguments are passed to functions. When a function is called, the values of the arguments are copied to the parameter variables. For lists (and dictionaries, which I'll describe in the next chanpter), this means a copy of the reference is used for tha parameter.
When passing a list into a function, it is the reference to the list. Both list and dictionary variables will lead to this behavior.

### `copy` Module's `copy()` and `deepcopy()` Functions

To keep a function from modifying the list or dictionary that is passed, use the `copy` module that provides

- `copy.copy()` to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
- `copy.deepcopy()` is used when the list you need to copy contains lists. `deepcopy()` will copy the inner lists as well.

```python3
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> id(spam)
44684232
>>> cheese = copy.copy(spam)
>>> id(cheese) # cheese is a different list with different identity.
44685832
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']
```

### Chapter 4 Practice Problems

**Comma Code**
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

```python3
spam = ['apples', 'bananas', 'tofu', 'cats']

def list_to_string(spam_s):
    string = ''
    for i in range(len(spam)):
        if i == 0:
            string += spam[i]
        elif i == (len(spam)-1):
            string += (', and ' + str(spam[i]))
        else:
            string += (', ' + spam[i])
    return string

list_items_as_string = list_to_string(spam)
print(list_items_as_string)
continue_receitve = input('end')
```

**Coin Flip Streaks**
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating head-tail results like “H T H T H H T H T T,” which looks random (to humans), but isn’t mathematically random. A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. Humans are predictably bad at being random.
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
You can start with the following template:

```python3
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
```

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

```python3
# My first try

import random
numberOfStreaks = 0
h_or_t = ['H', 'T']

for experimentNumber in range(10000):
    flip_register = []
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        flip_register += random.choice(h_or_t)
    print(flip_register)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    sequence = 0
    for c in range(len(flip_register)):
        if c == 0:
            previous_flip = flip_register[c]
        current_flip = flip_register[c]
        if sequence >= 6:
            numberOfStreaks += 1
            print("streak of" + current_flip)
            sequence = 0
        elif previous_flip == current_flip:
            sequence += 1
        if previous_flip != current_flip:
            sequence = 0
        previous_flip = flip_register[c]
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
end = input('end of program ...')
```

```python3
# example from stackoverflow
numberOfStreaks = 0
CoinFlip = []
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(CoinFlip)):
        if i==0:
            pass
        elif CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

    CoinFlip = []

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
stop = input()
```

---

## CH 5 Dictionaries and Structuring Data

---

A *dictionary* is a mutable collection of many values. Unlike indexees for lists, indexes for dictionaries can use many different data types, not just integers.
**Dictionary Index** = **Keys** and a key with its associated value is called a *key-value pair*.
Dictionaries use braces, `{}`
`>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}`
You access the values through their keys:

```python3
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```

### Dictionaries vs Lists

**Order**
Dictionaries are unordered
List order mattered in comparisons, but dictionaries do not.

```python3
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```

Even if dictionaries are unordered, argitrary values for keys allows the organization of data be very flexible. Example program to store friends' birthdays:

```python3
➊ birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

   while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

    ➋ if name in birthdays:
        ➌ print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
        ➍ birthdays[name] = bday
           print('Birthday database updated.')
```

### `keys()`, `values()`, and `items()` Methods

3 dictionary methods return list-like values of the dictionary's keys, values, or both keys and values. Return values are not true lists: they cannot be modified and do not have an `append()` method.
But data types `dict_keys`, `dict_values`, and `dict_items` *can* be used in `for` loops.

```python3
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
...     print(v)

red
42
```

`for` loop iterated over each value in the `spam` dictionary. A `for` loop can also iterate over the keys or both keys and values (`dict_items` value returned by the `items()` method are tuples of the key and value):

```python3
>>> for k in spam.keys():
...     print(k)

color
age
>>> for i in spam.items():
...     print(i)

('color', 'red')
('age', 42)
```

**IF a true list is needed**, pass its list-like return value to the `list()` function.

```python3
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

`list(spam.keys())` lines takes the `dict_keys` value returned from `keys()` and passes it to `list()`, which then returns a list value of `['color','age']`.

### for Key, Value in Dictionary

```python3
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
...     print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42
Key: color Value: red
```

### Check Key Value Existance in Dictionary

`in` and `not in` can check whether a value exists in a dictionary just like in lists.
Returns Boolean.

```python3
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
```

Shorthand for `'color' in spam.keys()` is `'color' in spam`

### `get()` Method

Checking whether a key exists in a dictionary before accessing the key's value is tedious. `get()` method allows a fallback value to be returned if the key does not exist.

```python3
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
```

`get()` will subvert error messages such as:

```python3
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
KeyError: 'eggs'
```

### `setdefault()` Method

If a key dues not have a value `setdefault()` will allow this functionality in 1 line of code
Instead of :

```python3
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
```

The 1st argument passed to the method is the key to check for, and the secuond argument is the value to set at that key if the key does not exist.

```python3
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

`setdefault()` can be used to count the number of occurrences of each letter in a string.

```python3
message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}

for character in message:
➊ count.setdefault(character, 0)
➋ count[character] = count[character] + 1

print(count) 
```

### Pretty Printing

Import the module `pprint` into your programs, you'll have access to the `pprint()` and `pformat()` funtions. This is helpful when dictionaries contain nested lists or dictionaries.

```python3
import pprint
message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
```

`pformat()` will obtain the prettified text as a string value instead of displaying it on the screen

```python3
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```

Those 2 lines are equivalent.

### Nested Dictionaries and Lists

```python3
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
  ➊ for k, v in guests.items():
      ➋ numBrought = numBrought + v.get(item, 0)
     return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
```

You can view the execution of this program at <https://autbor.com/guestpicnic/>. Inside the totalBrought() function, the for loop iterates over the key-value pairs in guests ➊. Inside the loop, the string of the guest’s name is assigned to k, and the dictionary of picnic items they’re bringing is assigned to v. If the item parameter exists as a key in this dictionary, its value (the quantity) is added to numBrought ➋. If it does not exist as a key, the get() method returns 0 to be added to numBrought.
Output:

```python3
 Number of things being brought:
 - Apples 7
 - Cups 3
 - Cakes 0
 - Ham Sandwiches 3
 - Apple Pies 1
```
---

## CH6 Manipulating Strings

---

Working with Strings lets you write, print, and access strings in your code.

### String Literals

Use single quote `' '`
Using a quote within a string requires double and single quotes.

```python3
>>> spam = "That is Alice's cat."
```

To use both single and double quotes in a string requires escape Characters

### Escape Characters

`\` *escape character* lets you use characters otherwise impossible for put into a string.
Single Quote = `\'`
Double quote = `\"`
Tab = `\t`
Newline = `\n`
Backslash = `\\`

### Raw Strings

Place `r` before the beginning quotation mark of a string to ignore all escape characters:

```python3
>>> print(r'The is \n Carol\'s cat.')
```

will output:

```python3
That is \n Carol\'s cat.
```

Windows file paths or regular expressions are useful to use *raw strings*
`r'C:\Users\Josh\Desktop'`

### Multiline Strings with Triple Quotes

`\n` puts newline into a string, but using multipline strings `''' string '''` (can also use 3 double quotes) allow any quotes, tabs, or newlines in between the "triple quotes" to be part of the string.
Python's indentation rules for blocks do not apply to lines inside a multiline string.

```python3
 print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Ouput:

```python3
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

Escaping single and double quotes is optional in multiline strings.
The following `print()` call produces identical output:
`print('Dear Alice,\n\nEve\'s cat has been arrested for catnipping, cat burglary, and extortion.\n\nSincerely,\nBob')`

### Multiline Comments

Hash character (#) marks the beginning of a comment for the rest of the line.

```python3
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')
```

### Indexing and Slicing Strings

Strings use indexes and slices same a lists. Strings are a list and each character in the string is an item with a corresponding index.

```python3
>>> spam = 'Hello, world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[7:]
'world!'
```

For index range, start is included, end is not.
Slicing dos not modify the original string. Slices can be stored in a separate variable.

### The `in` and `not in` operators with Strings

Evaluates to Boolean `True` or `False`
Expressions test exact string and is case-sensitive.

```python3
>>> 'Hello' in 'Hello, World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello, World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
```

### Strings Inside Other Strings: *String Interpolation*

Instead of concatentation:

```python3
>>> name = 'Al'
>>> age = 4000
>>> 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
'Hello, my name is Al. I am 4000 years old.'
```

Use ***String Interpolation*** where `%s` operator inside strings is a marker replaced by values following the string.

```python3
>>> name = 'Al'
>>> age = 4000
>>> 'My name is %s. I am %s years old.' % (name, age)
'My name is Al. I am 4000 years old.'
```

`str()` does not have to be called to convert values to strings.
Python 3.6 introduced ***f-string***, similar to interpolation except braces `{}` are used instead of `%s`.

```python3
>>> name = 'Al'
>>> age = 4000
>>> f'My name is {name}. Next year I will be {age + 1}.'
'My name is Al. Next year I will be 4001.'
```

### String Methods

**`upper()` `lower()`**
Return a new string where all letters in original string are converted to uppercase or lowercase.
Nonletter characters remain unchanged.
To alter the original string, call `upper()` or `lower()` on the string and then assign the new string to the variable where the original was stored.
`spam = spam.upper()`

**`isupper()` `islower()`**
will return `True` value if string has at least one letter and all the letters are uppercase or lowercase, respectively. Otherwise, `false`.

```python3
>>> spam = 'Hello, world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

**`isX()`**

- isalpha() Returns True if the string consists only of letters and isn’t blank
- isalnum() Returns True if the string consists only of letters and numbers and is not blank
- isdecimal() Returns True if the string consists only of numeric characters and is not blank
- isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
- istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
`isX()` is useful when needing to validaete user input.

```python3
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

```

**`startswith()`** and **`endswith()`**
Returns `true` if the string value they are called on begins or ends with the string passed to the method.

```python3
>>> 'Hello, world!'.startswith('Hello')
True
>>> 'Hello, world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello, world!'.startswith('Hello, world!')
True
>>> 'Hello, world!'.endswith('Hello, world!')
True
```

**`join()`** and **`split()`**
`join()` method joins a list of strings together into a single string value.
`join()` method called on a string, gets passed a list of strings, and returns a string.

```python3
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

`split()` method is called on a string and returns a list of strings.
Default split character is whitespace (space, tab, or newline characters)

```python3
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

Delimiter strings can be passed to `split()`

```python3
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

**`partition()`**
`partition()` string method can split a string into the text before and after a separator string. Returns a tuple of 3 substrings.
Will only find the 1st occurance:

```python3
>>> 'Hello, world!'.partition('o')
('Hell', 'o', ', world!')
```

If not found, 1st full string returned, other 2 strings empty:

```python3
>>> 'Hello, world!'.partition('XYZ')
('Hello, world!', '', '')
```

Multiple assignment can ssign 3 returned strings to 3 variables:

```python3
>>> before, sep, after = 'Hello, world!'.partition(' ')
>>> before
'Hello,'
>>> after
'world!'
```

**`rjust()`, `ljust()`, and `center()`**

```python3
>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'              Hello'
>>> 'Hello, World'.rjust(20)
'         Hello, World'
>>> 'Hello'.ljust(10)
'Hello     '
```

`center()` is great for section headings in output

```python3
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

### Printing Tables Example

```python3
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

```python3
Output:
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
```

**`strip()`, `rstrip()`, and `lstrip()`**
Removes whitespace characters at the beginning or end. l for left, r for right.

```python3
>>> spam = '    Hello, World    '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'    Hello, World'
```

String argument can be passed into `strip()`

```python3
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs'
```

Middle did not get removed. Only end characters.
Order of string passed in does not matter.

### `ord()` and `char()` Functions

Numeric Values of Characters
Every text character has a corresponding numeric value in *Unicode code point*
`ord()` returns the code point of a one-character string. `chr()` functions gets one-character string of an integer code point.

```python3
>>> ord('A')
65
>>> ord('4')
52
>>> ord('!')
33
>>> chr(65)
'A'
```

Ordering or mathematical operation on characters:

```python3
>>> ord('B')
66
>>> ord('A') < ord('B')
True
>>> chr(ord('A'))
'A'
>>> chr(ord('A') + 1)
'B'
```

More on this: Ned Batchelder’s 2012 PyCon talk, [“Pragmatic Unicode, or, How Do I Stop the Pain?”](https://youtu.be/sgHbC6udIqc) <https://youtu.be/sgHbC6udIqc>

### Copy and Paste with `pyperclip` Module

`pyperclip` module has `copy()` and `paste()` functions that can send text to and receive text from your computer's clipboard. Sending output of your program to the clipboard will make it east to paste it into an email, word processor, or some other software.
`pyperclip` module does not come with Python. Install it.

```python3
>>> import pyperclip
>>> pyperclip.copy('Hello, world!')
>>> pyperclip.paste()
'Hello, world!'
```

### Running python Scripts Outside of MU (or other editors)

More info in ToC Appendix B of Automate the boringstuff
MacOS -> create a shell script to run Python scripts by creating a text file with the *.command* file extension. Createa  new file in a text editor and add the following contrnet:

```python3
#!/usr/bin/env bash
python3 /path/to/your/pythonScript.py
```

Save file with the *.command* file extension in home folder. In terminal window, make the shell script executable by running `chmod u+x yourScript.command`. Now you'll be able to click the Spotlight icon (command-SPACE) and enter *yourScript.command* to run the shell script, which with run the Python script.

Windows -> Create a *batch script* with *.bat* file extension like the shell script in macOS and Linux. To make a batch file:

```python3
@py.exe C:\path\to\your\pythonScript.py %*
@pause
```

@ sign at the start of each command prevents it from beign displayed in the terminal window.
%* forwards any command line arguments entered after the batch filename to the Python script. The python script in turn reads the command line arguments in the `sys.argv` list. @pause will add `"Press any key to continue..."` after the end of the Python script to prevent the program's window from disappearing too quickly.
Recommend to place all batch and .py files in a single folder that already exists in the `PATH` environment variable, such as C:\Users\<USERNAME>.

### Project: Multi-Clipboard Automatic Messages

Automate responding to large number of emails with similar phrasing. Process is made easier with a program that stores multiple phrases.

Run program with a command line argument that is a short key phrase - for instance, *agree*, or *busy*.

The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email.



```python3
#! python3
# mclip.py - A multiclipboard program.

TEXT = {'free': """Sounds great. My calendar is up to date. Pick time at your convenience and send me an invite. \n\nThanks,\n-Josh""",
        'kickoff': """I look forward to working with you on the assessment next week. Please let me know if you have any questions about the document request or remote access details. On kickoff we will . . .""",
        'complete': """Thank you for the opportunity to work with you on this assessment project. As you review report details, reach out with any questions. The reports have been uploaded to \n\nThanks,\n-Josh"""
        }

import sys, pprintpp, pyperclip

if len(sys.argv) > 1:
    keyphrase = sys.argv[1]

if len(sys.argv) < 2:
    print('CLIPBOARD SCRIPT'.center(80, '='))
    print('='.center(80, '='))
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    keyphrase = 'No Argument Received in sys.argv[1]'

while True:
    if keyphrase not in TEXT:
        print('\n')
        print('KEYPHRASE OPTIONS'.center(80, '='))
        pprintpp.pprint(TEXT)
        print('There was no input text during script call. ' + keyphrase)
        keyphrase = input('Enter Keyphrase or (e) for exit: ')
        if keyphrase.lower() == 'e':
            break
    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
        break
```
---

## CH7 Pattern Matching with Regular Expressions

---

This chapter includes:

- Programs to find text patterns without using regular expressions
- Then adds regular expressions to show their power.
- Shows String substitution and creating character classes

### Finding Patters of Text Without Regular Expressions

Goal: find american phone number in a string.
Example: 415-555-4242
Function: `isPhoneNumber()` checks whether a string matches this pattern
Returns: `True` or `False`.

```python3
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
```

To find a phone number within a larger string, add more code to find the phone number pattern.

```python3
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    print('Done')
```

### Finding Patters of Text with Regular Expressions

The above code will fail for other phone number formats such as 415.555.4242 or (415) 555-4242. More code is required for these additional patterns, but using *regexes* is an easier method.

*Regexes* (regular expressions) are descriptions for a pattern of text. Example: \d stands for a digit character(1-9).

The regex \d\d\d-\d\d\d-\d\d\d\d is used by python to match the same text pattern the previous `isPhoneNumber()` function did.

Other sophisticated descriptions are used such as `{3}` for "Match this pattern three times". `isPhoneNumber()` could also be replaced with regex \d{3}-\d{3}-\d{4} to match the phone number.

### Creating Regex Objects

regex functions in Python are in the re module:

```python3
>>> import re
```

Passing a regular expression to `re.compile()` returns a Regex pattern object (or simply, a Regex object).

Phone number example again:

```python3
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```

Now the phoneNumRegex variable contains a Regex object.

### Matching Regex Objects

Regex object's `search()` method searches the string it is passed for any matches to the regex. `search()` returns `None` if regex pattern is not found in the string.

```python3
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Mu number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

### Review of Regular Expression Matching

Python steps to using regular expressions:

- Import the regex module with `import re`
- Create a Regex object with the `re.compile(r'regexPatternString')` function. (Remember to use a raw string.)
- Pass the string you want to search into the `Regex` object's `search()` method. This returns a `Match` object.
- Call the `Match` object's `group()` method to return a string of the actual matched text.

Web-based regular expression testers can show exactly how a regex matches a piece of text: [https://pythex.org/](https://pythex.org/)

### More Pattern Matching with Regex

### *Grouping with Parentheses*

Adding parentheses will create *groups* in the regex: `(\d\d\d)-(\d\d\d-\d\d\d\d)`. Then you can use the `group()` match object method to grab the matching text from just one group.

1st set of parentheses in regex string is group 1.
2nd set of parentheses is regex string is group 2.
Set the group by passing integer 1 or 2 to the `group()`

```python3
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'
```

Plural `groups()` method will return all the groups at once.

```python3
>>> mo.groups()
('415', '555-4242')
>>> areaCode, mainNumber = mo.groups()
>>> print(areaCode)
415
>>> print(mainNumber)
555-4242
```

`mo.groups()` returned a tuple of multiple values, so multiple assignment can be used.
To match special meaning characters in regex like paranthesis, use escape character `\(`

Regular Expression Special Meaning Characters:

```Text
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
```

To detect the characters in text patterns, escape them with a backslash:

```Text
\.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)
```

### *Matching Multiple Groups with a Pipe `|`*

`r'Batman|Tina Fey'` will match either `'Batman'` or `'Tina Fey'`
When both occur in a string, only the first occurance will match.

`all` matching occurrences can be found with `findall()` method.

Matching any string beginning with same pattern: example `'Batman', 'Batmobile', 'Batcopter',` and `'Batbat'`. Specify prefix `bat` only once like:

```python3
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
```

`mo.group()` returns the full matched text `'Batmobile'` while `mo.group(1)` returns just the part matched text inside the first parentheses group, `'mobile'`.

### *Optional Matching with `?`*

For patterns that you want to match only optionally. i.e., find the match regardless of whether that bit of text is there.

```python3
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
```

The next IP address example doesn't check that the IP address is valid, but it gives the idea of 4 octets with between 1-3 digits.

```python3
ipAddress = re.compile(r'\d(\d)?(\d)?\.\d(\d)?(\d)?\.\d(\d)?(\d)?\.\d(\d)?(\d)?)
```

Using earlier phone number example, we can make a regex look for phone numbers that do or do not have an area code.

```python3
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242')
>>> mo2.group()
'555-4242'
```

`?` means "Match zero or one of the group preceding this question mark."

### *Matching Zero or More with the Star*

`*` called *star* or *asterisk* means "match zero or more" - the group that precedes the star can occcur any number of times in the text. It can be completely absent or repeated over and over again.
Batman Example:

```python3
>>> batRegex = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowowoman'
```

To match an actual *star* prefix the star in the regular expression with a backslash, `\*`

### *Matching One or More with the Plus*

While `*` means "zero or more", `+` means "match one or more"
`+` requires that the group preceding a plus must occur at least once.

```python3
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True
```

### *Matching Specific Repetitions with Braces*

group to repeat a specific number of times, follow the group in the regex with a number in braces: `(Ha){3}` will match string `'HaHaHa'`.

Specify a Range like: `(Ha){3,8}`
Range "3 or more": `(Ha){3,}` - leave the last number blank. Similarly leaving out the furst or second number in the braces will specify the minimum or maximum unbounded range. `(Ha){,5}` is "zero to five instances of Ha"

These 2 range regular expressions match identical patterns:

```text
(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
```

### Greedy and Non-Greedy Matching

Notice range matches return the longest match.
`(Ha){3,5}` can match three, four, or five instances of Ha... but `Match` object's call to `group()` returns the logest string. 

Python's regular expressions are *greedy* by default, which means that in ambiguous situations they match the longest string possible. The *non-greedy* (lazy) version of the braces, match shortest, has closing brace followed by question mark.

```python3
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```

`?` in regex has 2 meanings

- declaring a non-greedy match
- flagging an optional group

### The `findall()` Method

While `search()` will return a `match` object of the *first* matched text in a searched string, `findall()` method returns strings of *every* match in the searched string.

Example with `search()`

```python3
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
>>> mo.group()
'415-555-9999'
```

Example with `findall()`

```python3
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
```

If there are groups in the regular expression, `findall()` with groups will return a list of tuples.
Example of `findall()` with regular expression being compiled with groups in parentheses:

```python3
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

### `findall()` Summary

- when called on regex with no groups, `\d\d\d-\d\d\d-\d\d\d\d`, the method `findall()` returns a list of string matches `['415-555-9999', '123-444-5555']`
- When called on a regex that has groups, `(\d\d\d)-(\d\d\d)-(\d\d\d\d)`, the method `findall()` returns a list of tuples of strings (one string for each group), such as `[('415', '555', '9999'), ('123', '444', '5555')]`

### Character Classes

`\d` is shorthand for the regular expression `(0|1|2|3|4|5|6|7|8|9)`. Other *shorthand character classes* include:

| Shorthand character class | Represents |
| ------------------------- | ------------------------------ |
| \d | Any numeric digit from 0 to 9. |
| \D | Any character that is not a numeric digit from 0 to 9. |
| \w | Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.) |
| \W | Any character that is not a letter, numeric digit, or the underscore character. |
| \s | Any space, tab, or newline character. (Think of this as matching “space” characters.) |
| \S | Any character that is not a space, tab, or newline. |


```python3
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```

### Making your Own Character Classes

If shorthand character classes are too broad, use `[]` to create your own character class.

Example, character class `[aeiouAEIOU]` will match any vowel, both lowercase and uppercase.

```python3
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

Inside `[]` normal regular expression symbols are not interpreted as such. No need to escape.
(^) after opening bracket, you make a *negative character class*, matching all characters not in the character class.
Negative Character Class Example:

```Python3
>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

### Caret and Dollar Sign Characters

Use (^) at the start of a regex = "match must occur at *beginning* of searched text."
Use ($) at the end of a regex = "match must *end* with the regex pattern."
Using ^ and $ together requires the entire string to match - not just a subset of a string.

`r'^Hello'` to begin with Hello

```python3
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> beginsWithHello.search('He said hello.') == None
True
```

`r'\d$'` strings that end with a number 0 to 9:

```python3
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<re.Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None
True
```

`r'^\d+$'` matches strings that both gegin and end with 1 or more numeric characters:

```python3
>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringIsNum.search('1234567890')
<re.Match object; span=(0, 10), match='1234567890'>
>>> wholeStringIsNum.search('12345xyz67890') == None
True
>>> wholeStringIsNum.search('12  34567890') == None
True
```

### The Wildcard Character

The `.` (or dot) character in regular expression is a *wildcard* and matched any character except for a newline.

`.` Example:

```python3
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```

The dot will match only 1 character, so `'flat'` returns only `'lat'`.

### Matching everything with a `.*`

`.` = "any single character except the newline"
`*` = "zero or more of the preceding character"
So, together `.*` = "Every single character except the newline"

```python3
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
```

`.*` uses *greedy* mode, it will always try to match as much text as possible. Fo *non-greedy*, use the dot, star, and question mark `.*?`

Greedy vs Non-Greedy Mode `.*`

```python3
>>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'

>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'
```

### Matching Newlines with the Dot Character

dot-star matches everything except a newline. By passing `re.DOTALL` as 2nd argument to `re.compline(), dot character matches *all* characters including newline.

```python3
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.'


>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```

### Review of Regex Symbols

- `?` Matches zero or one of the preceding group.
- `*` matches zero or more of the preceding group.
- `+` Matches one or more of the preceding group.
- `{n}` matches exactly *n* of the preceding group.
- `{n,}` Matches *n* or more of the preceding group.
- `{,m}` matches 0 to *m* of the preceding group.
- `{n.m}` matches *n* to *m* of the preceding group.
- `{n,m}?` or `*?` or `+?` performs a non-greedy match of the preceding group.
- `^spam` means the string must begin with *spam*
- `spam$` means the string must end with *spam*
- The `.` matches any character, except newline characters.
- `\d`, `\w`, and `\s` match a digit, word, or space character, respectively.
- `\D`, `\W`, and `\S` match anything except a digit, word, or space character, respectively.
- `[abc]` matches any charactyer between the brackets (such as *a, b* or *c*).
- `[^abc]` matches any character that isn't between the brackets. 

### Case-Insensitive Matching

Regular Expressions match text exact casing you specify. T make regex case-insensitive, pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`.

```python3
>>> robocop = re.compile(r'robocop', re.I)
>>> robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'

>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'
```

### Substituting Strings with the `sub()` Method

Regular Expressions can substitute new text in place of patterns matched. The `sub()` method for `Regex` objects is passed two arguments. First string to replace any matches and second string for regular expression:

```python3
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

If needing to use the matched text as part of the substitution, in 1st argument type \1 \2 \3 etc to mean "Enter the text of group 1,2,3,etc in the substitution."

Example, regex `Agent (\w)\w*)` passed with `r'\1*****'` as the first argument to `sub()`. The  `\1` in the string will be replaced by whatever text was matched by group 1 - that is, the `(\w)` group of the regular expression.

```python3
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
Eve knew Agent Bob was a double agent.')
A**** told C**** that E**** knew B**** was a double agent.'
```

### Managing Complex Regexes

Use `re.VERBOSE` to spread regular expressions over multiple lines with comments like:

```python3
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')
```

Becomes:

```python3
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

Use triple-quote syntax `'''` to create the multipline string and spread over many lines.

### Combining `re.IGNORECASE` `re.DOTALL` and `re.VERBOSE`

`re.compile()` function takes only a single value as its second argument.

To get around this, use pipe `|` with both arguments within a single `re.compile()`

```python
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```

### Project: Phone Number and Email Address Extractor

Say there is a task to find every phone number and email address in a long web page or document. To avoid manual review, a program could allow you to copy text to a clipboard and search text in clipboard for phone numbers and email addresses. Manual work turns to CTRL-A and CTRL-C then run the program.

Start a new project by considering the bigger picture and drawing high-level plan for what the program needs to do.

This phone and email address extractor needs to do the following:

- Get the text off the clipboard.
- Find all phone numbers and email addresses in the text.
- Paste them onto the clipboard

Now think what the code needs to do:

- Use the `pyperclip` module to copy and paste strings.
- Create two regexes, one for matching phone numbers and the other for matching email addresses.
- Find all matches, not just the first match, of both regexes.
- Neatly format the matched strings into a single string to paste.
- Display some kind of message if no matches were found in the text.

Organize the objectives into Steps:

### *Step 1: Create a Regex for Phone Numbers*

First, create regular expression to search for phone numbers. Example python file: *phoneAndEmail.py*

```python3
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
```

### *Step 2: Create a Regex for Email Addresses*

```python3
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
--snip--

# Create email regex.
emailRegex = re.compile(r'''(
  ➊ [a-zA-Z0-9._%+-]+      # username
  ➋ @                      # @ symbol
  ➌ [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
```

### *Step 3: Find All Matches in the Clipboard Text*

```python3
 #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Find matches in clipboard text.
   text = str(pyperclip.paste())

➊ matches = []
➋ for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
➌ for groups in emailRegex.findall(text):
       matches.append(groups[0])

   # TODO: Copy results to the clipboard.
```

### *Step 4: Join the Matches into a String for the Clipboard*

```python3
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

--snip--
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
```

---

## CH8 Input Validation

---

*Input Validation* checks the values entered by the user.

Instead of using `while` and `for` loops for validation, this chapter shows 3rd party module PyInpuPlus Module

### `PyInputPlus` Module

`PyInputPlus` contains functions similar to `input()` for several kinds of data: numbers, dates, email addresses, and more.

**Install** `pip install --user pyinputplus`

**Import** `>>> import pyinputplus`

**Documentaiton** [https://pyinputplus.readthedocs.io/](https://pyinputplus.readthedocs.io/)

PyInputPlus has functions for different kinds of input:

- `inputStr()` Is like the built-in input() function but has the general PyInputPlus features. You can also pass a custom validation function to it
- `inputNum()` Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it
- `inputChoice()` Ensures the user enters one of the provided choices
- `inputMenu()` Is similar to inputChoice(), but provides a menu with numbered or lettered options
- `inputDatetime()` Ensures the user enters a date and time
- `inputYesNo()` Ensures the user enters a “yes” or “no” response
- `inputBool()` Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value
- `inputEmail()` Ensures the user enters a valid email address
- `inputFilepath()` Ensures the user enters a valid file path and filename, and can optionally check that a file with that name exists
- `inputPassword()` Is like the built-in input(), but displays * characters as the user types so that passwords, or other sensitive information, aren’t displayed on the screen

Functions will automatically repormpt user for as long as they enter invalid input:

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum()
five
'five' is not a number.
42
>>> response
42
```

Python's `help()` function finds out more about each of these functions. Example: `help(pyip.inputChoice)` displays help information for the `inputChoice()` function.

### Keyword Arguments: min, max, greaterThan, lessThan

The `inputNum()` `inputInt()` and `inputFloat()` functions accept int and float numbers, also have min,max,greaterThan, and lessThan keyword arguments for specifying a range of valid values:

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ', min=4)
Enter num:3
Input must be at minimum 4.
Enter num:4
>>> response
4
>>> response = pyip.inputNum('Enter num: ', greaterThan=4)
Enter num: 4
Input must be greater than 4.
Enter num: 5
>>> response
5
>>> response = pyip.inputNum('>', min=4, lessThan=6)
Enter num: 6
Input must be less than 6.
Enter num: 3
Input must be at minimum 4.
Enter num: 4
>>> response
4
```

### *blank Keyword*

blank input is not allowed unless blank keyword is set to `True`

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter num: ')
Enter num:(blank input entered here)
Blank values are not allowed.
Enter num: 42
>>> response
42
>>> response = pyip.inputNum(blank=True)
(blank input entered here)
>>> response
''
```

### *limit, timeout, and default Keywords*

To keep invalid input from being an endless loop,

`limit` and `timeout`

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(limit=2)
blah
'blah' is not a number.
Enter num: number
'number' is not a number.
Traceback (most recent call last):
    --snip--
pyinputplus.RetryLimitException
>>> response = pyip.inputNum(timeout=10)
42 (entered after 10 seconds of waiting)
Traceback (most recent call last):
    --snip--
pyinputplus.TimeoutException
```

`default` example

```python3
>>> response = pyip.inputNum(limit=2, default='N/A')
hello
'hello' is not a number.
world
'world' is not a number.
>>> response
'N/A'
```

### The allowRegexes and blockRegexes Keyword Arguments

`allowRegexes` and `blockRegexes` keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
XLII
>>> response
'XLII'
>>> response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
xlii
>>> response
'xlii'
```

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(blockRegexes=[r'[02468]$'])
42
This response is invalid.
44
This response is invalid.
43
>>> response
43
```

If both are specified, allow will override block

```python3
>>> import pyinputplus as pyip
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'
```

For more on pyinputplus, see online documentation: [https://pyinputplus.readthedocs.io/](https://pyinputplus.readthedocs.io/)

### Passing a Custom Validation Function to inputCustom()

A custom input function can be written and used with pyinputplus.inputCustom(). The custom written function must:

- Accept a single string argument of what the user entered
- Raise an exception if the string fails validation
- Return `None` (or has no `return` statement) if `inputCustom()` should return the string unchanged.
- Return a non-`None` Value if `inputCustom()` should r4eturn a different string from the one the user entered
- Pass the custom function as the first argument to `inputCustom()`

Example for `addsUpToTen()` function:

```python3
>>> import pyinputplus as pyip
>>> def addsUpToTen(numbers):
...   numbersList = list(numbers)
...   for i, digit in enumerate(numbersList):
...     numbersList[i] = int(digit)
...   if sum(numbersList) != 10:
...     raise Exception('The digits must add up to 10, not %s.' %
(sum(numbersList)))
...   return int(numbers) # Return an int form of numbers.
...
>>> response = pyip.inputCustom(addsUpToTen) # No parentheses after
addsUpToTen here.
123
The digits must add up to 10, not 6.
1235
The digits must add up to 10, not 11.
1234
>>> response # inputStr() returned an int, not a string.
1234
>>> response = pyip.inputCustom(addsUpToTen)
hello
invalid literal for int() with base 10: 'h'
55
>>> response
```

---

## CH9 Reading and Writing Files

---

Use Python to create, read, and save files on the hard drive.

### Files and File Paths

| file property example | description |
| --- | ---- |
| C:\  | windows root folder |
| /  | macOS and Linux root folder |
| D:\ or E:\ | Additional volumes on Windows |
| /Volumes folder | Additional volumes in Linux |
| /mnt ("mount") folder | Where additional volumes appear in Linux |
| C:\Users\AL\Documents  | file path |
| project.docx  | file name |

Windows file and folder names are not case-sensitive.
Linux and macOS files an folder names are case-sensitive.

### Backslash on Windows and Forward Slash on macOS and Linux

Windows = paths use `\` as separator between folder names.
macOS and Linux = paths use `/` as path separator.

Python scripts should be written to work on both operating systems.

`Path()` function in `pathlib` module. Passing string values of individual file and folder names returns a string with a file path using correct path separators.

```python3
>>> from pathlib import Path
>>> Path('spam', 'bacon', 'eggs')

WindowsPath('spam/bacon/eggs')
>>> str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'
```

interactive shell on Windows will return Linux style patchs with forward slash in the interactive shell due to developers historically favoring Linux operating system.
A returned string contained the excape character with the Windows separator `\\`

On Windows backslash separates directories, so you can't use it in filenames. On macOS and Linux, you can. `Path(r'spam\eggs\')` refers to two separate folders on Windows, but the same command in macOS and Linux refers to a single folder or file named *spam\eggs*. **Always use forward slashes in your Python code.** `pathlib` module will ensure that is always works on all operating systems. 

### Using the `/` Operator to Join Paths

`+` operator usually adds two integers or floating-point numbers, but `+` can also be used to concatenate two strings.

Similarly, `/` operator usually divides, but `/` is also used to combine `Path` objects and strings.

```python3
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
```

Using `/` to join paths is safer than using string concatenation or `join()` methods such as

```python3
>>> homeFolder = r'C:\Users\Al'
>>> subFolder = 'spam'
>>> homeFolder + '\\' + subFolder
'C:\\Users\\Al\\spam'
>>> '\\'.join([homeFolder, subFolder])
'C:\\Users\\Al\\spam'
```

The 2nd example would only work on Windows.
The correct way to do it would be:

```python3
>>> homeFolder = Path('C:/Users/Al')
>>> subFolder = Path('spam')
>>> homeFolder / subFolder
WindowsPath('C:/Users/Al/spam')
>>> str(homeFolder / subFolder)
'C:\\Users\\Al\\spam'
```

### Current Working Directory

Any filenames or paths that do not begin with root folder are assumed to be under the *current working directory* or `cwd` 

`Path.cwd()` function returns the current working directory as a string value.
`os.chdir()` will change the current working directory.

```python3
>>> from pathlib import Path
>>> import os
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'
>>> os.chdir('C:\\Windows\\System32')
>>> Path.cwd()
WindowsPath('C:/Windows/System32')
```

Python will error if you try to change to a directory that does not exist.

```python3
>>> os.chdir('C:/ThisFolderDoesNotExist')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 2] The system cannot find the file specified:
'C:/ThisFolderDoesNotExist'
```

`Pathlib` does not contain a function for changing working directory because it can create bugs.

### The Home Directory

All users have a folder for their own files called the *home directory* or *home folder*

`Path` object is returned by calling `Path.home()`

```python3
>>> Path.home()
WindowsPath('C:/Users/Al')
```

| OS | Home Directory Location |
| -- | ----------------------- |
| Windows | C:\Users |
| Mac | /Users |
| Linux | /home |

Read and write permissions for users in home directories make it an ideal place to put files that programs will work with.

### Absolute vs. Relative Paths

2 ways to specify a file path:

- *absolute path* always begins with the root folder
- *relative path* is relative to the program's current working directory

`.` folder is shorthand for "this directory"
`..` folder is shorthand for "the parent folder"

`.\` at the start of a relative path is optional. Example `.\spam.txt` and `spam.txt` refer to the same file.

### Creating New Folders Using the `os.makedirs()` Function

```python3
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```

`os.makedirs()` will create folders and all subfolders.

Making a directory from a `Path` object, call `mkdir()` method. For example creating spam under the User Al's home folder:

```python3
>>> from pathlib import Path
>>> Path(r'C:\Users\Al\spam').mkdir()
```

`mkdir()` can only make one directory at a time.

### Handling Absolute and Relative Paths

`pathlib` module provides methods for checking whether a given path is an absolute path or returning the absolute path of a relative path.

`is_absolute()` returns `True` if it represents an absolute path or `False` if it represents a relative path.

```python3
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
>>> Path.cwd().is_absolute()
True
>>> Path('spam/bacon/eggs').is_absolute()
False
```

To get an absolute path from a relative path, you can put  `Path.cwd() /` in front of the relative `Path` object. 

```python3
>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.cwd() / Path('my/relative/path')
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37/my/relative/
path')
```

Getting absolute path from relative path and home directory

```python3
>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.home() / Path('my/relative/path')
WindowsPath('C:/Users/Al/my/relative/path')
```

`os.path` module useful functions related to absolute and relative paths:

- Calling `os.path.abspath(path)` will returns a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
- Calling `os.path.isabs(path)` will return `True` if the argument is an absolute path and `False` if it is a relative path.
- Calling `os.path.relpath(path, start)` will return a stirng of a relative path from the `start` path to `path`. If `start` is not provided, the current working directory is used as the start path.

```python3
>>> os.path.abspath('.')

'C:\\Users\\Al\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.path.abspath('.\\Scripts')
'C:\\Users\\Al\\AppData\\Local\\Programs\\Python\\Python37\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True
```

When relative path is within the same parent folder as the path, but is within subfolders of a different path - use "dot-dot":

```python3
>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
```

### Getting the Parts of a File Path

Parts of a file path include:

- The *anchor*, which is the root folder of the filesystem
- On Windows, the *drive*, is the single letter that often denotes a physical hard drive or other storage device.
- The *parent* is the folder that contains the file
- The *name* of the file, made up of the *stem* (or *base name*) and the *suffix* (or *extension*)

```python3
>>> p = Path('C:/Users/Al/spam.txt')
>>> p.anchor
'C:\\'
>>> p.parent # This is a Path object, not a string.
WindowsPath('C:/Users/Al')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
'C:'
```

All return strings, except `parent`, which returns another `Path` object.
`parents` (plural) evaluates to an ancestor folder of the `Path` object:

```python3
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')
>>> Path.cwd().parents[0]
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python')
>>> Path.cwd().parents[1]
WindowsPath('C:/Users/Al/AppData/Local/Programs')
>>> Path.cwd().parents[2]
WindowsPath('C:/Users/Al/AppData/Local')
>>> Path.cwd().parents[3]
WindowsPath('C:/Users/Al/AppData')
>>> Path.cwd().parents[4]
WindowsPath('C:/Users/Al')
>>> Path.cwd().parents[5]
WindowsPath('C:/Users')
>>> Path.cwd().parents[6]
WindowsPath('C:/')
```

`os.path.basename()` example:

```python3
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(calcFilePath)
'calc.exe'
>>> os.path.dirname(calcFilePath)
'C:\\Windows\\System32'
```

`os.path.split()` returns a tuple of 2 strings:

```python3
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')
```

Same tuple can be created using `os.path.dirname()` and `os.path.basename()`

```python3
>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe')
```

`os.sep` returns a list of individual folders:

```python3
>>> calcFilePath.split(os.sep)
['C:', 'Windows', 'System32', 'calc.exe']
```

### Finding File Sizes and Folder Contents

`os.path` module provides functions for finding size of file in bytes, and the file and folders inside a given folder

- `os.path.getsize(path)` returns size in bytes of the file in the `path` argument.
- `os.listdir(path)` returns list of filename strings for each file in the `path` argument.

```python3
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
27648
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
```

To total size of all files in a directory:

```python3
>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
>>> print(totalSize)
2559970473
```

### Modifying a List of Files Using Glob Patterns

`glob()` method is simpler to use than `listdir()`. Glob patterns are like a simplified form of regular expressions often used in command line commands. `glob()` returns a generator object that you need to pass to `list()` to easily view in the interactive shell.

```python3
>>> p = Path('C:/Users/Al/Desktop')
>>> p.glob('*')
<generator object Path.glob at 0x000002A6E389DED0>
>>> list(p.glob('*')) # Make a list from the generator.
[WindowsPath('C:/Users/Al/Desktop/1.png'), WindowsPath('C:/Users/Al/
Desktop/22-ap.pdf'), WindowsPath('C:/Users/Al/Desktop/cat.jpg'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
```

`*` stands for "multiple of any characters" so `p.glob('*')` returns a generator of all files inthe path stored in `p`.

To list all text files:

```python3
>>> list(p.glob('*.txt') # Lists all text files.
[WindowsPath('C:/Users/Al/Desktop/foo.txt'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
```

`?` stands for "any single character"

```python3
>>> list(p.glob('project?.docx')
[WindowsPath('C:/Users/Al/Desktop/project1.docx'), WindowsPath('C:/Users/Al/
Desktop/project2.docx'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/project9.docx')]
```

Combining characters in `glob()` such as `*.?x?`

```python3
>>> list(p.glob('*.?x?')
[WindowsPath('C:/Users/Al/Desktop/calc.exe'), WindowsPath('C:/Users/Al/
Desktop/foo.txt'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]
```

The glob expression '*.?x?' will return files with any name and any three-character extension where the middle character is an 'x'.

`for` loops can iterate over the generator that `glob()` returns:

```python3
>>> p = Path('C:/Users/Al/Desktop')
>>> for textFilePathObj in p.glob('*.txt'):
...     print(textFilePathObj) # Prints the Path object as a string.
...     # Do something with the text file.
...
C:\Users\Al\Desktop\foo.txt
C:\Users\Al\Desktop\spam.txt
C:\Users\Al\Desktop\zzz.txt
```

To perform an operation on every file in a directory, use `os.listdir(p)` or `p.glob('*')`.

### Checking Path Validity

Assume `p` holds a `Path` object:

- `p.exists()` returns `True` if the path exists or returns `False` if not.
- `p.is_file()` returns `True` if exists and is a file, returns `False` otherwise.
- `p.is_dir()` returns `True` if path exists nd is a directory, or returns `False` otherwise.

```python3
>>> winDir = Path('C:/Windows')
>>> notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
>>> calcFile = Path('C:/Windows
/System32/calc.exe')
>>> winDir.exists()
True
>>> winDir.is_dir()
True
>>> notExistsDir.exists()
False
>>> calcFile.is_file()
True
>>> calcFile.is_dir()
False
```

### The File Reading/Writing Process

`pathlib` module's `read_text()` returns a string of the full contents of a text file.
`write_text()` creates a new text file (or overwrites and existing one) with the string passed to it.

```python3
>>> from pathlib import Path
>>> p = Path('spam.txt')
>>> p.write_text('Hello, world!')
13
>>> p.read_text()
'Hello, world!'
```

`Path` only provides basic interactions with files. More common way of writing to a file uses `open()` function and file objects.

### Opening Files with the `open()` function

`open()` function opens a file of the relative or absolute path passed to it. Returns a `File` object.

```python3
>>> helloFile = open(Path.home() / 'hello.txt')
```

`open()` will accept strings.
On Windows:

```python3
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')
```

On macOS

```python3
>>> helloFile = open('/Users/your_home_folder/hello.txt')
```

Python default is to open the file in 'r' read mode.
So open('/Users/Al/hello.txt', 'r') and open('/Users/Al/hello.txt') do the same thing.

### Reading the Contents of Files

Using `File` object's `read()` method will read entire contents:

```python3
>>> helloContent = helloFile.read()
>>> helloContent
'Hello, world!'
```

`readlines()` returns a *list* of string values from the file, one string for each line.

```python3
>>> sonnetFile = open(Path.home() / 'sonnet29.txt')
>>> sonnetFile.readlines()
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
look upon myself and curse my fate,']
```

Notice the last line does not end with a newline character `\n`.

### Writing to Files

Writing requires files to be opened in "write plaintext" `'w'` or "append plaintext" `'a'` mode. Pass mode as 2nd argument to `open()`

```python3
>>> baconFile = open('bacon.txt', 'w')   
>>> baconFile.write('Hello, world!\n')
13
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello, world!
Bacon is not a vegetable.
```

### Saving Variables with the Shelve Module

`shelve` module allows variables saved to binary shelf files so program can restore data to variables from the hard drive. The `shelve` module lets you add Save and Open features to a program.

```python3
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

After running the previous code on Windows, you will see three new files in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On macOS, only a single mydata.db file will be created.

`shelve` module is used to later reopen and retrieve data from shelf files. Read/write modes don't apply.

```python3
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```

Shelf files are like dictionaries, they have `keys()` and `values()`.

```python3
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```

Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, but if you want to save data from your Python programs, use the shelve module.

### Saving Variables with the `pprint.pformat()` Function

`pprint.pformat()` function will return a string formatted and syntactically correct Python code. Dictionaries can be stored in a variable and stored in a .py file for future use after a shell is closed.

```python3
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()
```

The list named `cats` was saved to a python file `myCats.py`. This file can be imported.

```python3
>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'
```

The benefit of creating a .py file (as opposed to saving variables with the shelve module) is that because it is a text file, the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using the shelve module is the preferred way to save variables to a file. Only basic data types such as integers, floats, strings, lists, and dictionaries can be written to a file as simple text. File objects, for example, cannot be encoded as text.

---

## CH10 Organizing Files

---

copying, renaming, moving, or compressing files

### The Shutil Module

`shutil` or shell utilities module has functions to copy, move, rename, and delete files in Python programs.

`import shutil` to use the functions

### Copying Files and Folders

`shutil.copy(source, destination)` will copy the file at the path `source` to the folder at the path `destination`. IF `destination` is a filename, it will be used as the new name of the copied file. Returns a string or `Path` object of the copied file.

Example `shutil.copy()`:

```python3
>>> import shutil, os
>>> from pathlib import Path
>>> p = Path.home()
>>> shutil.copy(p / 'spam.txt', p / 'some_folder')
 'C:\\Users\\Al\\some_folder\\spam.txt'
>>> shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
 WindowsPath('C:/Users/Al/some_folder/eggs2.txt')
 ```

 `shutil.copytree()` copies an entire folder and every folder and file contained in it.

 ```python3
 >>> import shutil, os
>>> from pathlib import Path
>>> p = Path.home()
>>> shutil.copytree(p / 'spam', p / 'spam_backup')
WindowsPath('C:/Users/Al/spam_backup')
```

### Moving and Renaming Files and Folders

`shutil.move(source, destination)` moves the file or folder at the path `source` to path `destination`. Returns string of the absolute path of the new location. If `destination` is a folder, filename stays the same. If filename exists in the destination, it is overwritten.

```python3
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'
```

If there was no destination folder named `eggs`, then it would create a text file (without .txt extension) and save the file there.

```python3
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'
```

If a partent folder does not exist Python will throw an exception:

```python3
>>> shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
Traceback (most recent call last):
  --snip--
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\does_not_exist\\
eggs\\ham'
```

### Permanently Deleting Files and Folders

`os` module can delete single file or single empty folder.
`shutil` mudle can delete a folder and all of its contents.

- `os.unlink(path)` will delete the file at `path`.
- `os.rmdir(path)` will delete the folder at `path`. Folder must be empty of and files or folders.
- `shutil.rmtree(path)` will remove the folder at `path`, and all the files and folders it contains will also be deleted.

It is safer to first run a program with printing the filenames to delete prior to deleting:

```python3
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)
```

### Safe Deletes with the send2trash Module

Install: `pip install --user send2trash`

```python3
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a')   # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

In general, always use the `send2trash.send2trash()` function to delete files and folders.

send2trash:

- will not free up disk space like permanently deleting
- can only send files to the recycle bin; it cannot pull files out

### Walking a Directory Tree

walk through the directory tree, touching each file for every file in the folder and every file in the every subfolder.

`os.walk()` function is passed a single string value: path of a folder. Use is a for loop statement is like the use of `range()` function to talk over a range of numbers. `os.walk()` returns 3 values on each iteration:

- A string of the current folder's name
- A list of strings of the folders in the current folder
- A list of strings of the files in the current folder

Current folder means the folder for the current iteration of the `for` loop.

```python3
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
```

Output:

```text
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats 
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt.
```

### Compressing Files with the `zipfile` Module

`ZipFile` objects are similar to `File` objects.

`zipfile.ZipFile()` creates a ZipFile object.

`zipfile` = the python module. `ZipFile()` = name of the function.

```python3
   >>> import zipfile, os

   >>> from pathlib import Path
   >>> p = Path.home()
   >>> exampleZip = zipfile.ZipFile(p / 'example.zip')
   >>> exampleZip.namelist()
   ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
   >>> spamInfo = exampleZip.getinfo('spam.txt')
   >>> spamInfo.file_size
   13908
   >>> spamInfo.compress_size
   3828
➊ >>> f'Compressed file is {round(spamInfo.file_size / spamInfo
   .compress_size, 2)}x smaller!'
   )
   'Compressed file is 3.63x smaller!'
   >>> exampleZip.close()
```

A ZipFile object has a namelist() method that returns a list of strings for all the files and folders contained in the ZIP file. These strings can be passed to the getinfo() ZipFile method to return a ZipInfo object about that particular file. ZipInfo objects have their own attributes, such as file_size and compress_size in bytes, which hold integers of the original file size and compressed file size, respectively. While a ZipFile object represents an entire archive file, a ZipInfo object holds useful information about a single file in the archive.

### Extracting from ZIP Files

`extractall()` method for `ZipFile` objects extracts all the files and folders from a ZIP file into the curernt working directory.

```python3
   >>> import zipfile, os
   >>> from pathlib import Path
   >>> p = Path.home()
   >>> exampleZip = zipfile.ZipFile(p / 'example.zip')
➊ >>> exampleZip.extractall()
   >>> exampleZip.close()
```

After run, contents of *example.zip* will be extracted to C:\. An optional foldername can be passed to `extractall()`.

```python3
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```

### Creating and Adding to ZIP Files

