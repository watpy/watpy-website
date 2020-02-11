Title: Installing Python
Date: 2020-01-15 20:00

> This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/4.0/][1].
> Parts of this section are based on excellent Django Girls Tutorial.

There is some software we would like for you to install on your laptop before you arrive.

1. Python
1. An editor

Python is the coding environment we will be using. Having a text editor designed for writing code will make your experience a lot better.

# Python

## Windows

In general we are assuming Windows 7, but these instructions should basically work for Windows 8. Contribution to further specialize these instructions are welcome.

> Python 3 versus Python 2 Through out these materials we will be focusing on Python 3.5. The latest release of Python 2 is 2.7, please don't install this version.

Use one of the following links to download Python:

* For 32 bit Windows: https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe
* For 64 bit Windows https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64.exe
* Or go to https://www.python.org/


> **Put Python on the PATH**
>
> If you are given the option during the installation, please check the box to put python on the path for you. If not a tutor can help set it up for you on the day of.

Choose "run" if you have the option to. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.

If everything worked correctly you should be able to run Python from the command line. To check this, open your command line by searching for cmd.exe and running it. You will be presented with a mostly black window with a **prompt** which should look something like `C:\>`. Here type `python` and press the `enter` key. You should see output like:

```
Python 3.5.0 (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Exit the Python prompt by typing

```
exit()
```

> If you see Python 2.7.x instead of 3.5.0 this means you previously installed Python 2.7 which is fine. We can help you at the event to make both Python 2.7 and Python 3.5 available to you.

## Put Python on the PATH

In case you weren't able to put Python on your PATH above we have included the manual instruction here so you can go through it yourself or with a tutor at the event.

### Get to System Properties

1. Open up "My Computer" by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to "Computer".
1. Right-click on the empty space in the window, and choose Properties.

A window labeled "View basic information about your computer" will appear.

1. In this window, click "Advanced system settings"

A window with the title "System Properties" will appear.

### Edit the Path

1. Within System Properties, make sure you are in the tab labeled "Advanced".
1. Click the button labeled "Environment Variables".
1. A window labeled "Environment Variables" will appear.
1. In this window, the screen is split between "User variables" and "System variables". Within "System variables", scroll down and find the one labeled Path. Click the "Edit..." button.
1. A window with the "Variable name" and the "Variable value" should appear. The "Variable value" will already have some text in it; click in the box to unhighlight it (we don't want to accidentally delete that text).
1. In the "Variable value" box, scroll to the end. Add the following text, and hit OK. Make sure to include the semicolon at the start!

```
;c:\Users\<Your Username>\Appdata\Local\Programs\Python\Python35;c:\Users\<Your Username>\Appdata\Local\Programs\Python\Python35\Scripts
```

or

```
;c:\Users\<Your Username>\Appdata\Local\Programs\Python\Python35-32;c:\Users\<Your Username>\Appdata\Local\Programs\Python\Python35-32\Scripts
```

If you installed the 32bit version of Python 3.5

1. Hit "OK" to close out the system properties window.

Test your change:

Open up a new command prompt by searching for `cmd.exe` This needs to be a new command prompt because the changes you just made didn't take affect in prompts that were already open.

Type `python` into the command prompt to start Python

Notice that you now get a Python interpreter, indicated by the change to a `>>>` prompt.

Exit the Python prompt by typing

```
exit()
```

and hitting enter. Now you're back at the Windows command prompt `C:\`.

## Mac OS X

We are assuming you are using Mac OS X 10.6 or later, if you have an older version please come early and consult a tutor.

Mac OS X comes with Python 2.7 pre-installed, but we will be working with Python 3.5. Generally you can have both installed and you can access Python 3 with `python3` instead of `python` on the command line.

- Click this link: https://www.python.org/ftp/python/3.5.0/python-3.5.0-macosx10.6.pkg and save the dmg. Open the dmg file and click on the package installer. Follow the installer to completion.

If everything worked correctly you should be able to run Python from the command line. To check this, open your command line by searching for Terminal in spotlight and running it. You will be presented with a mostly black window with a **prompt** which should look something like `Computername:~ username$`. Here type `python` and press the `enter` key. You should see out put like:

```
Python 3.5.0 (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Exit the Python prompt by typing

```
exit()
```

> If you see Python 2.7.x instead of 3.5.0 this means you previously installed Python 2.7 which is fine. Try typing in `python3` instead of just `python` to see if that work better.

## Linux

You should be able install Python with your package manager, for example `apt-get install python3`.

# Editor

There are a lot of different editors and it largely boils down to personal preference. Most Python programmers use complex but extremely powerful IDEs (Integrated Development Environments), such as PyCharm. As a beginner, however, that's probably less suitable; our recommendations are equally powerful, but a lot simpler.

## Atom

We recommend Atom since it is free, open-source an available for Window, Mac OS X, and Linux.

[Download it here](https://atom.io/)

## Sublime Text 2

Sublime Text is a very popular editor with a free evaluation period. It's easy to install and use, and it's available for all operating systems.

[Download it here](http://www.sublimetext.com/2)

## Why are we installing a code editor?

You might be wondering why we are installing this special code editor software, rather than using something like Word or Notepad.

The first is that code needs to be plain text, and the problem with programs like Word and Textedit is that they don't actually produce plain text, they produce rich text (with fonts and formatting), using custom formats like RTF (Rich Text Format).

The second reason is that code editors are specialised for editing code, so they can provide helpful features like highlighting code with colour according to its meaning, or automatically closing quotes for you.

We'll see all this in action later. Soon, you'll come to think of your trusty old code editor as one of your favourite tools :)

# Bonus Round

## Heroku Sign Up

If you have time please sign up for Heroku here: https://signup.heroku.com/dc. By signing up before the event you will prevent any issues we might run into if we all sign up from the same location.

[1]: http://creativecommons.org/licenses/by-sa/4.0/
