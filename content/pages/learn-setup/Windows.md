Title: Windows
Date: 2020-01-15 20:00

# Setting up Python on Windows

In general we are assuming Windows 7, but these instructions should basically work for Windows 8. Contribution to further specialize these instructions are welcome.

> Python 3 versus Python 2
>
> Through out these materials we will be focusing on Python 3.4. Python 3.5 was just release and will probably work just as well.
> The latest release of Python 2 is 2.7, please don't installed this version.

You can use the `command line` to check if you already have Python installed.


    C:\> python
    Python 3.4.x (...)
    Type "help", "copyright", "credits" or "license" for more information.
	>>>
    
If you have Python 2 already installed you can install Python 3 and access it with `python3` rather than `python`
	
## Install Python

1. Use one of the following links to download Python:
    * For 32 bit Windows: [https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi](https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi) 
    * For 64 bit Windows [https://www.python.org/ftp/python/3.4.3/python-3.4.3.amd64.msi](https://www.python.org/ftp/python/3.4.3/python-3.4.3.amd64.msi)
    * Or go to [https://www.python.org/](https://www.python.org/)
1. Choose "run" if you have the option to. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.
1. Verify that there is a Python folder in your start bar with Python Command Prompt and IDLE programs.

### Success!

You have successfully installed Python 3.4.3.

## Practice Running IDLE

IDLE is a simple built in application for editing and running Python programs and it one of a few way to interact with the Python prompt `>>>`.

1. Open IDLE either by the `Start Menu > Programs > Python > IDLE` or type `IDLE` into the search field.
1. IDLE will open up a window called Python shell. Type the following into the Python prompt `>>>` in the Python shell window
        
        print("Hello, World!")
   and press Enter. Python should answer back with Hello, World!
1. Next click on `File > New Window`. Type the following on the first line of the new window
        
        print("Hello, World!")
1. Click `Run > Run Module`. When it asks to save the file choose OK. Save the file on your `Desktop` with the filename `hello.py`. 
1. IDLE will bring the Python shell to the front and run the program. In Python shell you should see
        
        >>>
        Hello, World!
        >>>
   The same thing that happened when you typed `print("Hello, World!")` into the Python prompt `>>>` directly.
   
### Success!

You have used the Python prompt in IDLE and created and saved your first Python program!

## Practice with the Windows Command Prompt

IDLE is a way to interact with your Python programs. The built in command prompt provides another way which can be very flexible.

> Building Command Prompt Skills
>
> If you want more than a crash course, try out the Introductory Windows Command Prompt under skills.

1. Click on the Start Menu, type `cmd` into the Search field directly above the Start Menu button, and click on `cmd.exe` in the search results above the Search field. This will open a window with white text and a black background with something like `C:\>`.
1. Click on the window and type `C:\Python34\python.exe` after the Windows command prompt `C:\>`. You should see something like this

        Python 3.4.3 (...) on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
1. There is that Python prompt again `>>>`. You can type `print("Hello, World!")` followed by pressing Enter again to make sure it works the same way.
1. Type `exit()` into the Python prompt `>>>` and press Enter. This will take you back to the Windows command prompt `C:\>`

### Success!

You have opened the Windows command prompt. From there you open a Python command prompt and used exit() to close it.

>Tail of two prompts
>
>First we ran an application called `cmd.exe` which openned a Windows command prompt. It is a program design to take your commands and run other programs. One of the program you can run is Python. When Python runs it takes over the Windows command prompt and provides its own Python promtp `>>>`. Until you use `exit()` to quit Python, you can also run Python code.
>
>You can think of it likea prompt with in a prompt, kind of like insception.

## Running Your Own Python Program from the Command Prompt

### Put Python on the PATH

You might have noticed that you typed a "full path" to the Python application above when launching Python (`python.exe` is the application, but we typed `C:\Python34\python.exe`). In this step, you will configure your computer so that you can run Python without typing the "Python34" folder name.

#### Get to System Properties

1. Open up "My Computer" by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to "Computer".
1. Right-click on the empty space in the window, and choose Properties.
1. A window labeled "View basic information about your computer" will appear.
1. In this window, click "Advanced system settings"
1. A window with the title "System Properties" will appear.

#### Edit the Path

1. Within System Properties, make sure you are in the tab labeled "Advanced".
1. Click the button labeled "Environment Variables".
1. A window labeled "Environment Variables" will appear.
1. In this window, the screen is split between "User variables" and "System variables". Within "System variables", scroll down and find the one labeled Path. Click the "Edit..." button.
1. A window with the "Variable name" and the "Variable value" should appear. The "Variable value" will already have some text in it; click in the box to unhighlight it (we don't want to accidentally delete that text).
1. In the "Variable value" box, scroll to the end. Add the following text, and hit OK. Make sure to include the semicolon at the start!

        ;c:\python34\;c:\python34\scripts
1. Hit "OK" to close out the system properties window.
1. Test your change:
        1. Open up a new command prompt: you do this the same way you did above when installing python. This needs to be a new command prompt because the changes you just made didn't take affect in prompts that were already open.
        1. Type python into the command prompt to start Python
        1. Notice that you now get a Python interpreter, indicated by the change to a `>>>` prompt.
        1. Exit the Python prompt by typing `exit()` and hitting enter. Now you're back at the Windows command prompt (C:\).

#### Mini Success!

That was likely a lot clicking and a fair amount of effort, but this is an example of something you only have to do once. Once it is setup it will keep working for as long as you have your computer.

### Run hello.py

1. In a previous step we created a file called `hello.py` which had `print("Hello, World!")` in it and we saved it to your `Desktop`.
1. Navigate to your Desktop directory from your newly opened Windows command prompt, using the `dir` and `cd` commands.
1. Once you are in your Desktop directory, you'll see hello.py in the output of dir. Type

        python hello.py
   and press Enter.
1. Doing this will cause Python to execute the contents of that script &mdash; it should print "Hello World!" to the command prompt window. What you've done here is run the Python application with an argument &mdash; the name of a file, in this case "hello.py". Python knows that when you give it a file name as an argument, it should execute the contents of the provided file.

Success!

You have configured Python to run easily from anywhere with the Windows command prompt and you have run your first Python program form a file!

