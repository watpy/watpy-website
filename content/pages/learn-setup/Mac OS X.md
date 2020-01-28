Title: Mac OS X
Date: 2020-01-15 20:00

# Installing Python on Mac OS X

We are assuming you are using Mac OS X 10.6 or later, if you have an older version please consult a tutor.

Mac OS X comes with Python 2.7 pre-installed, but we will be working with Python 3.4. Generally you can have both installed and you can access Python 3 with `python3` instead of `python` on the command line.

1. Click this link: [https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg](https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg) and save the dmg. Open the dmg file and click on the package installer. Follow the installer to completion.
1. Search spotlight for `IDLE` you should find an application.
1. SUCCESS!

# Running IDLE on Mac OS X

IDLE is an application that lets you edit and run Python programs.

1. Open IDLE either by doing a spot light search for IDLE or via finder goto Applications > Python 3.4 > IDLE.app
1. IDLE will open up with a Python shell. Type the following into the Python prompt (">>>") in the Python shell

    `print("Hello, World!")`
    
    and press Enter. Python should answer back with Hello, World!
    
1. Next click on File > New Window. Type the following on the first line of the new window:

    `print("Hello, World!")`
    
1. Click Run > Run Module. When it asks to save the file choose OK. Save the file on your Desktop with the file name `hello.py`. If you need help please ask a tutor.
1. IDLE will bring the Python shell to the front and run the program. In Python shell you should see

        >>>
	    Hello, World!
        >>>
        
    The same thing that happened when you typed print("Hello, World!") into the Python prompt (">>>") directly

###Success!

You have used the Python prompt in IDLE and created and saved your first Python program!

# The Command Prompt on Mac OS X

1. Search spot light for `terminal` or use the Finder to goto Applications > Utilities > Terminal.app.
1. It will open a window with a command prompt. At the prompt `$` type `python`
1. You should see something like 

        Python 3.4.3 (...)
        [..] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
        
1. There is that Python prompt again `>>>`. You can type `print("Hello, World!")` 
    followed by pressing Enter again to make sure it works the same way.
1. Type `exit()` and press Enter. This will take you back to the Mac OS X command prompt `$`

###Success!

You have opened the Windows command prompt. From there you open a Python command prompt and used exit() to close it.

# Navigating with the Command Prompt on Mac OS X

The filesystem on your computer is like a tree made up of folders (also called "directories") and files. The filesystem has a root directory called /, and everything on your computer lives in subdirectories of this root directory.

We often navigate the filesystem graphically by clicking on graphical folders. We can do the exact same navigation from the command line.

There are two commands that we'll be using at a command prompt to navigate the filesystem on your computer:

* `ls`
* `cd`

`ls` lists the contents of a directory.
`cd` moves you into a new directory (it stands for "change directory").

Let's practice using these commands.

## Open a command prompt:

* Search spot light for `terminal` or use the Finder to goto Applications > Utilities > Terminal.app.

## Practice using `ls` and `cd`

Type each of these commands and hit enter:

```
ls
```

This lists all the files in your home directory.

```
cd /
```

This will change you into the `/` directory.

```
ls
```

This lists the contents of the `/` directory.

```
cd Users
```

This will change you into the `Users` subdirectory of the `/` directory.

```
ls
```

You should see the names of all the files and directories in `/Users`.

```
cd ..
```

`..` means "parent directory", so this command moved you up to the parent directory. You were in `/Users`, so now you are in `/`, the root directory.

```
ls
```

This lists the contents of the root directory, confirming where you are.

## Tips

* You can use Tab to auto-complete directory and file names. So from inside the root directory, if you type `cd Use` and hit Tab, the command prompt will auto-complete the directory name, and you can then hit enter to change into the `/Users` directory.
* The command prompt maintains a command history. You can use the up arrow to cycle through old commands.
* Note that the text that makes up the command prompt changes as you move around directories. The command prompt will always give the full directory path to your current directory.

## Check your understanding

Answer these questions. Experiment at the command line if you need to! If you aren't sure about an answer, ask a helper.

1. What directory are you in after starting a new command line prompt?
1. After starting a new command line prompt, how would you get to the root directory?
1. How do you check what files and directories are in your current working directory?
1. If you are in directory /Users, and you want to get to /Users/jesstess/projects, how would you do that?
1. What are 2 ways to avoid typing out a full navigation command? (hint: one requires that you've run the command before)
1. What is the difference between a command prompt and a Python prompt?

### Success!

You've practiced using `ls` and `cd` to navigate your computer's filesystem from the command prompt.

# Running a Python Program from the Command Line on Mac OS X

## Run hello.py

1. In a previous goal we created a file called hello.py which had `print("Hello, World!")` in it and we saved it to your Desktop.
1. Navigate to your Desktop directory from a command prompt, using the `ls` and `cd` commands. See the [terminal navigation on Windows](http://legacy.watpy.ca/learn/mac/navigation/) instructions for a refresher on using these commands. Don't hesitate to get help from a staff member on this step if you need it -- it's a new way of navigating your computer, so it may be unintuitive at first!
1. Once you are in your Desktop directory, you'll see `hello.py` in the output of `ls`.
    
    Type
    
    ```
    python hello.py
    ```
    
    and press Enter.
    
1. Doing this will cause Python to execute the contents of that script -- it should print "Hello World!" to the screen. What you've done here is run the Python application with an argument -- the name of a file, in this case "hello.py". Python knows that when you give it a file name as an argument, it should execute the contents of the provided file.

### Success!

You have configured Python to run easily from anywhere with the Command Prompt and you have run your first Python program form a file!
