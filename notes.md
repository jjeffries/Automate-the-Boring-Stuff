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

```
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

```
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

```
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```

### Summary Example Program: Rock, Paper, Scissors

```
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

### A function definition `def`

Function is like a mini program within a program

```
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

```
def hello(name):
    print('Hello, ' + name)

hello('Alice')
hello('Bob')
```

Output will be:

```
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

```
print('Hello')
print('World')
```

outputs:

```
Hello
World
```

But using the `end` optional parameter allows

```
print('Hello', end='')
print('World')
```

outputs:

```
HelloWorld
```

When passing multiple string values, the default is to separate with spaces, but you can change to commas like so:

```
>>> print('cats', 'dogs', 'mice')
cats dogs mice
```

vs using the `sep` keyword argument:

```
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

```
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

```
def spam():
       print(eggs) # ERROR!
    ➊ eggs = 'spam local'

➋ eggs = 'global'
   spam()
```

This program will error as:

```
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

```
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

```
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

### Changing Values in a List with Indexes

```
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

```
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

```
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

```
for i in range(4):
    print(i)
```

output:

```
0
1
2
3
```

Python considers `range(4)` return value similar to `[0, 1, 2, 3]`. The following has the same output:

```
for i in [0, 1, 2, 3]:
    print(i)
```

Common List iteration technique: `for range(len(someList)):` to iterate over the indexes of a list.
Interactive shell example:

```
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

```
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

```
projects = ['planning stage', 'in progress', 'complete']
new_project = projects[0]
current_project = projects[1]
old_project = projects[2]
```

The assignments above can be completed using `tuple unpacking`

```
new_project, current_project, old_project = projects
```

Number of vaiables and the length of the list must be exactly equal.

### `enumerate()` Function with Lists

`enumerate()` can be used instead of `range(len(someList))`
On each iteration of a `loop`, `enumerate()` will return
[1] The index of the item in the list
[2] The item in the list itself

```
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

```
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

```
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
```

`insert()` receives the index location and the value to add to the list

```
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```

The **return** value of `append()` and `insert()` methods are `none`. The code does not assign method retuns to a variable. Do not use `spam = spam.append('moose')` because the list is modified in place.

Methods belong to a single data type. So `append()` and `insert()` are list methods and cannot be called on other values such as strings or integers.

### Removing Values from Lists: `remove()` Method

`remove()` method is passed the value to be removed from the list it is called on.

```
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
```

*If the value appears, only the 1st instance will be removed.*

`del` keyword deletes all the elements in range starting from the index 'a' till 'b'. `del[a:b]`

```
mylist = list(range(10))
print('list is: ', mylist)
del mylist[3:5]
print('list after delete is: ',mylist)
```

will remove elements from index 3 up to but not including 5.

```
list is:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list after delete is:  [0, 1, 2, 5, 6, 7, 8, 9]
```

If you know the index of the element, it is good to use the keyword `del`. Use `remove()` method when you know the value you want to remove.

### Sorting Values in a List: `sort()` Method

Sort numberical or alphabetical order.

```
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

```
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

3 things to remember about `sort()`
[1] `sort()` method sorts items in place. Don't capture in return value.
[2] number values and string values cannot be sorted together
[3] `sort()` uses "ASCIIbetical order" rather than actual alphabetical order. Uppercase comes before lowercase (i.e., 'a' comes after 'Z')

```
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
```

Sorting values in regular alphabetical order, pass `str.lower` for the `key` keyword argument in the `sort()` method call:

```
 >>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```

Above, `str.lower` causes the `sort()` function to treat all items in the list as if they were lowercase without acually changing the values in the list.

### Reversing Values in a List: `reverse()` Method

Quickly reversing the order of the items in a list, you can call the `reverse()` list method.

```
>>> spam = ['cat', 'dog', 'moose']
>>> spam.reverse()
>>> spam
['moose', 'dog', 'cat']
```

`reverse()` also does not return a value.

### Exceptions to Indentation Rules for Lists

Python knows that a list is not finished until it sees the ending square bracket.

```
spam = ['apples',
    'oranges',
                    'bananas',
'cats']
print(spam)
```

A single instruction accross multiple lies can be done using the \ line continuation character

```
print('Four score and seven ' + \
      'years ago...')
```

### Example Program: Magic 8 Ball with a List

```
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

```
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

```
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```

Lists can be either changed or overwritten since lists are mutable.
List Example where an entirely new and different list value is overwriting the old list value:

```
>>> eggs = [1, 2, 3]
>>> eggs = [4, 5, 6]
>>> eggs
[4, 5, 6]
```

To modify the original list, would have to do:

```
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

```
>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>
```

Tuples are used to convey in code that you don't intend for that sequence of values to change.
**Tuple Benefits** include Python's implementation of optimizations that make code using tuples slightly faster than code using lists.

### Converting Types with the `list()` and `tuple()` Functions

Just like str(42) will return the string representation of the integer 42, the functions list() and tuple() will reurn the list and tuple versions of the values passed to them.

```
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

```
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

```
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

```
>>> id('Howdy') # The returned number will be different on your machine.
44491136
```

Python picks address based on which memory bytes happen to be free on your computer at the time, so it'll be different each time you run code.

Immutable strings `id()`

```
>>> bacon = 'Hello'
>>> id(bacon)
44491136
>>> bacon += ' world!' # A new string is made from 'Hello' and ' world!'. 
>>> id(bacon) # bacon now refers to a completely different string.
44609712
```

Mutable lists `id()`

```
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

```
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

```
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

```
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
```

Of course, this is only an estimate, but 10,000 is a decent sample size. Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

```
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

```
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

A *dictionary* is a mutable collection of many values. Unlike indexees for lists, indexes for dictionaries can use many different data types, not just integers.
**Dictionary Index** = **Keys** and a key with its associated value is called a *key-value pair*.
Dictionaries use braces, `{}`
`>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}`
You access the values through their keys:

```
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```

### Dictionaries vs Lists

**Order**
Dictionaries are unordered
List order mattered in comparisons, but dictionaries do not.

```
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

```
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

```
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
...     print(v)

red
42
```

`for` loop iterated over each value in the `spam` dictionary. A `for` loop can also iterate over the keys or both keys and values (`dict_items` value returned by the `items()` method are tuples of the key and value):

```
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

```
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

`list(spam.keys())` lines takes the `dict_keys` value returned from `keys()` and passes it to `list()`, which then returns a list value of `['color','age']`.

**for Key, Value in Dictionary**

```
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
...     print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42
Key: color Value: red
```

### Check Key Value Existance in Dictionary

`in` and `not in` can check whether a value exists in a dictionary just like in lists.
Returns Boolean.

```
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

```
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
```

`get()` will subvert error messages such as:

```
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

```
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
```

The 1st argument passed to the method is the key to check for, and the secuond argument is the value to set at that key if the key does not exist.

```
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

```
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

```
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

```
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```

Those 2 lines are equivalent.

### Nested Dictionaries and Lists

```
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

```
 Number of things being brought:
 - Apples 7
 - Cups 3
 - Cakes 0
 - Ham Sandwiches 3
 - Apple Pies 1
```

## CH6 Manipulating Strings

Working with Strings lets you write, print, and access strings in your code.

### String Literals

Use single quote `' '`
Using a quote within a string requires double and single quotes.

```
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

```
>>> print(r'The is \n Carol\'s cat.')
```

will output:

```
That is \n Carol\'s cat.
```

Windows file paths or regular expressions are useful to use *raw strings*
`r'C:\Users\Josh\Desktop'`

### Multiline Strings with Triple Quotes

`\n` puts newline into a string, but using multipline strings `''' string '''` (can also use 3 double quotes) allow any quotes, tabs, or newlines in between the "triple quotes" to be part of the string.
Python's indentation rules for blocks do not apply to lines inside a multiline string.

```
 print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Ouput:

```
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

```
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

```
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

```
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

```
>>> name = 'Al'
>>> age = 4000
>>> 'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'
'Hello, my name is Al. I am 4000 years old.'
```

Use ***String Interpolation*** where `%s` operator inside strings is a marker replaced by values following the string.

```
>>> name = 'Al'
>>> age = 4000
>>> 'My name is %s. I am %s years old.' % (name, age)
'My name is Al. I am 4000 years old.'
```

`str()` does not have to be called to convert values to strings.
Python 3.6 introduced ***f-string***, similar to interpolation except braces `{}` are used instead of `%s`.

```
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

```
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

```
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

```
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

```
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

`split()` method is called on a string and returns a list of strings.
Default split character is whitespace (space, tab, or newline characters)

```
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

Delimiter strings can be passed to `split()`

```
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

**`partition()`**
`partition()` string method can split a string into the text before and after a separator string. Returns a tuple of 3 substrings.
Will only find the 1st occurance:

```
>>> 'Hello, world!'.partition('o')
('Hell', 'o', ', world!')
```

If not found, 1st full string returned, other 2 strings empty:

```
>>> 'Hello, world!'.partition('XYZ')
('Hello, world!', '', '')
```

Multiple assignment can ssign 3 returned strings to 3 variables:

```
>>> before, sep, after = 'Hello, world!'.partition(' ')
>>> before
'Hello,'
>>> after
'world!'
```

**`rjust()`, `ljust()`, and `center()`**

```
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

```
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

*Printing Tables Example*

```
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

```
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

```
>>> spam = '    Hello, World    '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'    Hello, World'
```

String argument can be passed into `strip()`

```
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

```
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

```
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

```
>>> import pyperclip
>>> pyperclip.copy('Hello, world!')
>>> pyperclip.paste()
'Hello, world!'
```

### Running python Scripts Outside of MU (or other editors)

More info in ToC Appendix B of Automate the boringstuff
MacOS -> create a shell script to run Python scripts by creating a text file with the *.command* file extension. Createa  new file in a text editor and add the following contrnet:

```
#!/usr/bin/env bash
python3 /path/to/your/pythonScript.py
```

Save file with the *.command* file extension in home folder. In terminal window, make the shell script executable by running `chmod u+x yourScript.command`. Now you'll be able to click the Spotlight icon (command-SPACE) and enter *yourScript.command* to run the shell script, which with run the Python script.

Windows -> Create a *batch script* with *.bat* file extension like the shell script in macOS and Linux. To make a batch file:

```
@py.exe C:\path\to\your\pythonScript.py %*
@pause
```

@ sign at the start of each command prevents it from beign displayed in the terminal window.
%* forwards any command line arguments entered after the batch filename to the Python script. The python script in turn reads the command line arguments in the `sys.argv` list. @pause will add `"Press any key to continue..."` after the end of the Python script to prevent the program's window from disappearing too quickly.
Recommend to place all batch and .py files in a single folder that already exists in the `PATH` environment variable, such as C:\Users\<USERNAME>.

### Project: Multi-Clipboard Automatic Messages

Automate responding to large number of emails with similar phrasing. Process is made easier with a program that stores multiple phrases.
**Step 1: Program Design and Data Structures**
Run program with a command line argument that is a short key phrase - for instance, *agree*, or *busy*.

The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email.
