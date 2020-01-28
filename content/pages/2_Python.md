Title: Python
Date: 2020-01-15 20:00

> This work is licensed under the Creative Commons
> Attribution-ShareAlike 4.0 International License. To view a copy of
> this license, visit
> [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).
>
> Parts of this section are based on excellent [Django Girls Tutorial](http://tutorial.djangogirls.org/).

## Python

We will be using Python 3.4. Python 2.7 is similar but changes made in Python 3 make installing and working with Python much easiser!

## Python Prompt

To get started with Python open your command line on your computer.

Once  you are ready, type in `python` on Windows or `python3` on Mac OS
or Linux and hit `enter` to open the Python console.

```
$ python3
Python 3.4.3 (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The output on each computer will be slighlty different but you you want to see `Python 3.4.x` and the **Python prompt** `>>>`. When you see the `>>>` prompt it means Python is running and the prompt will only accept Python commands.

If you want to exit the Python console at any point you can just type
`exit()` or use the chortcut `Ctrl + Z` on Windows and `Ctrl + D` on
Mac OS/Linux. Then you won't see the `>>>` any longer.

For now, we don't want to exit the console. We want to learn more about
Python. Let's look a basic example.

Throughout this document you will see code blocks like this:

```python
print('Hello World!')
```

Please type the code into the ">>>" prompt. You could copy and paste but
we are here to learn and practice so typing out the code will help you
learn and think about what you are typing.

After you have typed out `print('Hello World!')` you can run it by pressing `enter`. In this case Python will respond with the text "Hello, World!". Once you have the result we expect try pressing the `up arrow` and change the line of code to see what else is possible.

That is all there is to it. Read, type, and change. When things don't
work or you want to understand more how something works raise your hand
and a tutor will come help you. Talk with your neighbours as well and
share what you have learned!

#Part 1

## Basic Math

Python knows math! Run the block of code below to make sure the answer is right!

```python
1 + 1
```

Hopefully Python outputs `2` :)

Now lets say you won the lottery. You are about to collect your millions, but first you have to answer this skill testing question:

> `8+6*2*3-(15-13)`

Fortuntely Python can help. The order of operations you learned in school applies, i.e. BEDMAS (brackets, exponents, division, multiplication, addition, subtraction)

```python
8 + 6*2*3 - (15 - 13)
```

Numbers are valid Python code as are the common operators, `+`, `/`, `*`, `-` and `()`. You can write different types of numbers including **integers** aka whole numbers, real numbers (**floating point**) and negative integers.

```python
42 + 3.149 + -1
```

Since `42` is literally 42, we call these numbers **literals**. You are literally writing a number in your Python code.

## Check Please

You just had big meal will all your friends to celebrate your winnings, and now you need to calculate the tip.

```python
meal_cost = 200.00
# as a decimal, 10% would be 0.1
tip_percent = 0.10
meal_cost * tip_percent
```

Type in each line and hit `enter`. You don't have to type out the line which starts with the hash
mark `#` because it is a comment. Comment are useful in code to
communicate why something is writen a certain way, but they aren't
excuted by Python. They are there for humans not Python.

If you want to make it more user friendly you could do the following.

```python
meal_cost = 200.00
# as integer, 10% would be 10
tip_percent = 10
meal_cost * tip_percent / 100
```

Because of BEDMAS we don't need brackets, but `meal * (tip_percent / 100)` would work too.

## Variables

`meal` and `tip_percent` aren't literal numbers, they are **variables**.
In Python variables are like buckets (dump trucks?). You can put anything you want in them. Just give them a name and you can use them in place of the literal value.

Above `meal` was `200.00` but we could also set meal to the text 'Hello, World'

```python
meal = 200.00
print(meal)
meal = "Hello, World!"
print(meal)
```

The value of a variable only depends on what was last assigned to it using the `=`.

It is kind of like a spreadsheet except you choose the names for the cells yourself.

## Errors

Python only understands certain code. When you write something Python doesn't understand it throws an **exception** or error and tries to explain what went wrong, but it can only speak in a broken Pythonesque english. Let's see some examples by running these code blocks

```python
gibberish
```

```python
*adsflf_
```

```python
print('Hello'
```

```python
1v34
```

```python
2000 / 0
```

Type each line into your prompt and read the error it produces. Python tries to tell you where it stopped understanding, but in the above examples, each program is only 1 line long.
It also tries to show you where on the line the problem happened with caret `^`.

Python tells you the type of thing that went wrong such as NameError, SyntaxError, or ZeroDivisionError. It will also provide a bit more information like "name 'gibberish' is not defined" or "unexpected EOF while parsing".

Unfortunately you might not find "unexpected EOF while parsing" too helpful. EOF stands for End of File, but what file? What is parsing?

Python does its best, but it does take a bit of time to develop a knack for understanding what these messages mean. If you run into an error you don't understand please ask a tutor.

First type out the following blocks and then see if you can spot the error in these two block and try to fix them so that they run successfully

```python
print('Hello, World!)
```

```python
aswer = 3 * 8
print(answer)
```

# Part 2

## The Written Word

Numbers are handy, but most of our day to day computer interactions involve text, from emails to tweets to documents.

We have already seen a **text literal** in Python, "Hello, World!"

```python
"Hello, World!"
```

Text literals are surrounded by quotes. Without the quotes Hello by itself would be viewed as a variable name.

You can use either double quotes `"` or single quotes `'` for text literals.

Since variable can store anything they can also store text, just use the
`=` to assign them.

## What's a String?

Programmers call text literals **strings** because we are weird like that. It can be a bit hard to get used to so from now on we will only refer to text as strings to help you practice. Strings are pieces of text inside our code.

Let's use strings with variables!

```python
your_name = "Albert O'Connor"
print("Hello, ")
print(your_name)
```

Strings can be strung together with the `+`.

```python
"Hello, " + "Albert"
```

Though `+` doesn't insert a space for you, you have to tack it on.

You can multiply string with a number.

```python
"Meow" * 3
```

There are more to strings though than these operations. Strings have their own **functions** we can call on them to change them. We can use the built in `dir` function to get an idea of what they are.

```python
dir("Hello, World!")
```

That is a really long list. For now you can ignore the ones which start and end with double underscores `__`, but that still leaves a lot! Let's start with `upper()` and `lower()`.

Let's say you are really happy to see the world, and you want to make sure everyone knows it, you can use `upper()`. "upper" is short for uppercase and you will see what it does by running the code block below.

```python
string = "Hello, World"
string.upper()
```

Maybe you are feeling a bit sad and you want to be quiet, you can then use lower.

```python
string = "Hello, World"
string.lower()
```

We use the dot `.` to call these function on the string. A function is a sequence of instructions that Python knows to perform on a given object (`"Hello, World"`) once you call it. The functions lower and upper operate on the object that comes before the dot. That object needs to be a string variable or string literal.

```python
"Hello, World".upper()
```

## Formating

Sometimes you want to create a string out of a few other strings. Above we printed

> Hello,
> Your Name

by using two `print` functions, but it would be nice to output "Hello, Your Name!" instead. (Where Your Name is actually your name... oh variables)

We can do this with the string function called `format`. `format` is different from `lower` and `upper` because it can take other arguments. An argument is the name for the value passed to a function, it doesn't mean we are fighting :)

```python
your_name = "Albert O'Connor"
string = "Hello, {0}!"
string.format(your_name)
```

We can also use literal strings:

```python
"Hello, {0}!".format("Albert O'Connor")
```

`{0}` is a placeholder. `{0}` is where the first (0th?) argument, "Albert O'Connor", to format() is placed in the resulting string. `{1}` would mean use the second value if there was one.

## Indexed by Zero

For better or worse, (and practically it is better most of the time) everything in Python is index by 0. We will see this over and over again but for now if you call format like this:

```python
"{0} likes {1}".format("Albert O'Connor", 'Python')
```

We would call "Albert O'Connor" the 0th string passed into format and 'Python' the 1st. It is kind of weird, but roll with it. It will eventually make things eaiser.

## Line Endings

Let's say we wanted to represent the string in one string variable?

```
200 University Ave.
Waterloo, ON
```

A line ending is one example of something which is part of text on the screen that we need to somehow represent in a string. The key is the backslash `\` character. `\n` and `\r\n` represents two kind of line endings. Try adding `\n` in the right place in the string below to make it appear like the text at the beginning of this section.

```python
# Add a \n to this string to make output on multiple lines
print("200 University Ave. Waterloo, ON")
```

# Part 3

## Lists

So far we have played with numbers and strings, but there are other handy data types built into Python which are combinations of other data. They can be thought of as containers. The first one is the `list`!

A **list** in Python is just like a shopping list or a list of numbers. They have a defined order and you can add to it or remove from it.

Let's take a look at some simple lists.

```python
[]
```

This is the empty list, like a blank sheet of paper.

```python
["Milk", "Eggs", "Bacon"]
```

```python
[1,2,3]
```

List literals are all about square brackets `[]` and commas `,`. You can create a list of literals by wrapping them in square brackets and separating them with commas.
You can even mix different types of literals into the same list, numbers
and strings.

```python
[1, 2, "Awesome"]
```
We can put variables into a list and set a variable to a list.

```python
your_name = "Albert O'Connor"
awesome_people = ["Eric Idle", your_name]
print(awesome_people)
```

Like strings, lists have function

dir([])

"append" is an interesting one. "append" lets you add an item to the end of a list.

```python
your_name = "Albert O'Connor"
awesome_people = ["Eric Idle", your_name]
awesome_people.append("John Cleese")
print(awesome_people)
```

We can use square brackets `[]` again to access individual elements from the list variable.

```python
awesome_people[0]
```

There is that 0 indexing again. The first element of the list is given index value 0.

```python
print("These people are awesome: {0}, {1}, {2}".format(awesome_people[0], awesome_people[1], awesome_people[2]))
```

You can get the length of a list using the built in `len()` function.
Try calling it on our `awesome_people` list.

```python
len(awesome_people)
```

You can also use `len()` on string to found out how long they are.

```python
len(awesome_people[0])
```

`awesome_people[0]` is the first value in the list which should be "Eric
Idle" unless you have changed the list and the result of the last
statement should be the number of characters include spaces in the
string "Eric Idle" or 9.

If you ask for the item at an index beyond the end of the list Python
with raise an exception. Give it a try

```python
awesome_people[5]
```

## Dictionaries

**Dictionaries** are another container like lists, but instead of being index by a number like 0 or 1 it is indexed by a key which can be almost anything. The name comes from being able to use it to represent a dictionary which maps words to definitions.

We saw list literals use square brackets `[]` but dictionaries use braces `{}`. Use `shift + [` to type `{`.

> {"Python": "An awesome programming language",
>  "Monty Python": "A british comedy troupe"}

In a dictionary the key comes first followed by a colon `:` than the value then a comma `,` then another key and so on.

Let's see what running the literal dictionary looks like.

```python
{"Python": "An awesome programming language", "Monty Python": "A british comedy troupe"}
```

We can assign a dictionary to a variable; we can index with square brackets `[]` using keys to get the values (definitions) out.

```python
our_dictionary = {"Python": "An awesome programming language", "Monty Python": "A british comedy troupe" }
our_dictionary["Python"]
```

If you ask for a value at a key that isn't in the dictionary Python will
raise a `KeyError`.

```python
our_dictionary['invalid']
```

# Part 4

## If, Else and Conditions

Has an computer ever ask you a question? Maybe it asks you if you really want to quit because unsaved changes might be lost, or if you want to leave a webpage. If you answer OK one thing happens, like your application closing, but if you answer No or Cancel something else happens. In all those cases, no matter the language, there is a special piece of code that is being run somewhere, it is an if condition.

Python allows us to conditionally run code. To have an if condition we need the idea of something being true and something being false. Remember, we call numbers "integers" and "floating point", and text "strings". We call true or false **boolean** values. True would represent OK where as false would represent No or Cancel in the example above.

The literal values in Python for true and false are `True` and `False`

```python
False is False
```

```python
True is True
```

```python
True is False
```

```python
true is False
```

We can write conditions with operations and function too.

```python
1 > 2
```

```python
"Cool".startswith("C")
```

```python
"Cool".endswith("C")
```

```python
"oo" in "Cool"
```

```python
42 == 1 # note the double equals sign for equality
```

Here we have looked at some new operators and functions. The comparison
operators include `>`, `<`, `<=`, `>=`, `==`, `is`, `!=`, `not`, `in`.
Some of the function on string are comparison which return boolean
values like `startswith()` and `endswith()`.

## Python Code in Files

So far we have been using the Python interpreter, which is handy
specially when you want to figure out how something works. Normally programs
are saved in files and executed by Python so we don't have to type it out
everything we want to use it.

To switch into this mode of writing code we will need to:

* Exit the Python interpreter
* Open up your code editor of choice
* Type out and save some code into a new python file
* Run it!

To exit from the Python interpreter we've been using, type `exit()`:

```python
exit()
```

Now you should be back at your computers command prompt, `>` on Windows
or `$` on Mac OS/Linux.

Open up your code editor of choice in a separate window. In a new file
write one line of Python code. We are doing this just to make sure
everything is working as a we expect!

```python
print('Hello, Python!')
```

Now we need to save the file and give it a descriptive name. Let's call
the file `python_intro.py` and save it to your Desktop. We can name the
file anything we want, but the important part here is to make sure the
file ends in `.py`. The `.py` extension tells our operating system that
this is a python executable file and Python can run it.

Now you can switch back to your command line window to run the file.
First you have to change directory `cd` into your Desktop if you aren't
already there.

On Mac OS this will look something like:

```
$ cd /Users/<your_name>/Desktop
```

On Linux, it will be like this (the word "Desktop" might be translated):

```
$ cd /home/<your_name>/Desktop
```

And on Windows, it will be like this:

```
> cd C:\Users\<your_name>\Desktop
```

Ask for help if you get stuck.

Now use Python to execute the code in the file like this:

```
python python_intro.py
```

> Depending on your setup you might need to type `python3` instead of `python`.

You should see "Hello, Python!" appear on the command line!

Congrats you just ran your first Python program that was saved in a
file!

## If and Else

In order to write an "if" statement we need code that spans multiple lines

> if condition:
>     print("Condition is True")
> else:
>     print("Condition is False")

Some things to notice. The if condition ends in a colon `:`. In Python blocks of code are indicated with a colon `:` and are grouped by indenting lines of code. Notice the else also ends with a colon `:`, "else:".

Type out the following 5 lines of code in your `python_intro.py` file
replacing the `print` which is already there:

```python
condition = 1 > 2
if condition:
    print("Condition is True")
else:
    print("Condition is False")
```

Note the spaces before the `print` lines. For now practice hitting space
4 times before you write these lines. Eventually your editor will be
able to do this for you.

We need to do indent with spaces so Python knows what code to run if the result is true or flase. You can do one space, but nearly all Python programmers do 4 to make things look neat.

Save the file and run your new program in the command line window.

```
$ python3 python_intro.py
```

The output should be "Condition is False" since 1 is not greater than 2.
Try changing the condition line using different operator to see what is
true and false. Save your file each time and re-run it.

You can type `up arrow` on your keyboard in the command line interface to re type the last command you entered for you!

## Functions

Remember functions like `print()`, `dir()` or `len()`. You can write your
own functions to do whatever you want.

A function is a sequence of instructions that you want Python to
execute. Each function in Python starts with the keyword `def`, is given
a name, and has some **parameters**, which we can pass arguments into.

Let's start by replacing the code in `python_intro.py` with the
following:

```python
def say_hi():
    print('Hi there!')
    print('How are you?')

say_hi()
```

We start with the definition of our function and then we call it at the
end in the last line `say_hi()`. Python reads the files and executes it
from top to bottom, so in order to use our function, we have to call it
at the bottom.

Run it and see what happens:

```
$ python3 python_intro.py
```

Assuming we have a lot of people to `say_hi` to, having a function is
useful since we only need to type a short line to use it instead of two
longer lines. Functions can be much longer and save us a lot more
typing as well as organizing our program in to different units.

Let's make it even more useful by adding a parameter, say we want to
personalize our greetings.

```python
def say_hi(name):
    print('Hi {0}!'.format(name))

say_hi()
```

Now `say_hi` takes a parameter, name, and we personalize the message.

Try running it now.

We likely got an error!

```
TypeError: say_hi() missing 1 required positional argument: 'name'
```

We added the parameter to the `say_hi` function but forgot to add the
argument, the value we are passing in, when we called it.

```python
say_hi("Caroline")
```

Try running again and it should work. Try it with your own name.

## Loops

We have come a long way learning so many useful parts of Python. We have
one more in this section. *Loops* like the if blocks which came before
them are one of the most fundimental tools we can use.

You could say hi to lots of people by calling the `say_hi` function we
wrote many times, but we can use loops and lists to make it easier to
write and ready.

They look like this:
> for item in list:
>    print(item) # Do any action per item in the list

`for` and `in` are required. `list` can be any variable or literal which is like a list. `item` is the name you want to give each item in the list in the indented block as you loop through. We call each step where item has a new value an **iteration**.

Let's see it in action with our `say_hi` function in our python_intro.py
file.

```python
def say_hi(name):
    print('Hi {0}!'.format(name))


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for girl in girls:
    say_hi(girl)
    print("Looping")
```

Here we define the variable `girls` which is the list we will loop through; `name` will take on each value in the list. Note `:` after the `girls` which indicates the start of block of code similar to the if statements and the function definition. We indent `say_hi(name)` and `print("looping")` because we want to run both instructions every time we loop!

You can use the built in `range` function if you want to loop through a
list of numbers with out writing it out.

```python
for i in range(1, 6):
    print(i)
```

This should print

```python
1
2
3
4
5
```

`range` is a function that creates a list of numbers following one after the other (these numbers are provided by you as parameters).

Note that the second of these two numbers is not included in the list that is output by Python (meaning range(1, 6) counts from 1 to 5, but does not include the number 6). That is because "range" is half-open, and with that we mean it includes the first value, but not the last.

# Conclusion

Awesome job! This was a tricky chapter so you should feel proud of
yourself. These are the key thing all coders need to learn and now we
can move to the next step and create something more.

Before we get there take a break, stretch and walk around, rest your
eyes and your brain for a few minutes!
