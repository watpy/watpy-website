Title: Deploy to Heroku
Date: 2020-01-15 20:00

> This work is licensed under the Creative Commons
> Attribution-ShareAlike 4.0 International License. To view a copy of
> this license, visit
> [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).
>
> Parts of this section are based on excellent [Django Girls Tutorial](http://tutorial.djangogirls.org/).

Until now your website was only available on your computer, now you will learn how to deploy it! Deploying is the process of publishing your application on the Internet so people can finally go and see your app :).

As you learned, a website has to be located on a server. There are a lot of providers, but we will use the one with the simplest deployment process: [Heroku](http://heroku.com/). Heroku is free for small applications that don't have too many visitors, which is great to testing ideas or learning like we are doing today.

We will be somewhat following this tutorial: [https://devcenter.heroku.com/articles/getting-started-with-python-o](https://devcenter.heroku.com/articles/getting-started-with-python-o), though we have changed it to make it simpler and we will be deploying the web app you have already created.

## `runtime.txt`

First we need to tell Heroku which Python version we want to use. This is done by creating a runtime.txt in your `learncode` folder beside your `interface.py` file using your editors "New File" command. Put the following text (and nothing else!) inside:

```
python-3.4.3
```

## `requirements.txt`

Next we a `requirements.txt` file to tell Heroku what Python packages need to be installed on our server.

We need to install one more package to make our app work on Heroku:

```
$ pip install --user gunicorn
```

After the install is finished from your `learncode` folder run

```
$ pip freeze > requirements.txt
```

This will create a file called `requirements.txt` with a list of your installed packages (i.e. Python libraries that you are using, for example Flask :)).

> Note: `pip freeze` outputs a list of all the Python libraries installed locally or in a virtualenv, and the `>` takes the output of `pip freeze` and puts it into a file. Try running `pip freeze` without the `> requirements.txt` to see what happens!

## `Procfile`

Another thing we need to create is a `Procfile`. This will let Heroku know which commands to run in order to start our website. Open up your code editor, create a file called `Procfile` in you `learncode` folder and add this line:

> **Note** The case of the file name `Profile` matters. `procfile` won't work.

```
web: gunicorn interface:app --log-file=-
```

This line means that we're going to be deploying a web application, and we'll do that by running the command `gunicorn hello:app --log-file=-` (gunicorn is a program that's like a more powerful version of flask default server).

Then save it. Done!

## Heroku Account

You need to install your Heroku toolbelt which you can find here: [https://toolbelt.heroku.com/](https://toolbelt.heroku.com/
)

> When running the Heroku toolbelt installation program on Windows make sure to choose "Custom Installation" when being asked which components to install. In the list of components that shows up after that please additionally check the checkbox in front of "Git and SSH".
>
>On Windows you also must run the following command to add Git and SSH to your command prompts PATH: `setx PATH "%PATH%;C:\Program Files\Git\bin"`. Restart the command prompt program afterwards to enable the change.
>
> After restarting your command prompt, don't forget to go to your flask folder again!

If you haven't already, please create a free Heroku account here: [https://signup.heroku.com/dc](https://signup.heroku.com/dc)

Then authenticate your Heroku account on your computer by running this command:

```
$ heroku login
```

In case you don't have an SSH key this command will automatically create one. SSH keys are required to push code to the Heroku.

## Git

Git is a version control system used by a lot of programmers - software which keeps track of changes to a file or set of files over time so that you can recall specific versions later. Heroku uses a git repository to manage your project files, so we need to use it too.

Create a file named `.gitignore` in your `learncode` folder with the following content:

```
__pycache__
db.sqlite3
*.py[co]
```

and save it. The dot on the beginning of the file name is important!

Next, we’ll create a new git repository and save our changes.

> Note: Check out your current working directory with a `pwd` command before initializing the repository. You should be in the 'learncode' folder.

Go to your console and run these commands:

```
$ git init
Initialized empty Git repository in ~/Desktop/learncode/.git/
$ git config user.name "Your Name"
$ git config user.email you@example.com
```

Initializing the git repository is something we only need to do once per project.

It's a good idea to use a git status command before git add or whenever you find yourself unsure of what will be done, to prevent any surprises from happening (e.g. wrong files will be added or commited). The git status command returns information about any untracked/modifed/staged files, branch status and much more. The output should be similar to:

```
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Procfile
    blog.py
    first-post.html
	interface.py
	requirements.txt
	runtime.txt
    templates/base.html
    templates/home.html
    templates/post.html
    ...
```

nothing added to commit but untracked files present (use "git add" to track)

And finally we save our changes. Go to your console and run these commands:

```
$ git add -A .
$ git commit -m "My Flask app"
[master (root-commit) 9db7fd0] My Flask app
 4 files changed, 16 insertions(+)
 create mode 100644 Procfile
 create mode 100644 blog.py
 create mode 100644 interface.py
 create mode 100644 requirements.txt
 create mode 100644 runtime.txt
 ...
```

## Pick an application name

We'll be making your app available on the Web at [app name].herokuapp.com, so we need to choose a name that nobody else has taken. 

The easist way to do this is let Heroku choose the name for us.

```
$ heroku create
```

This will make a name with the format "verb-noun-number" such as "agile-citadel-4903"

You can also give it your own name, but it has to be something no one
else has picked and Heroku is quite strict as to what characters you can use: you're only allowed to use simple lowercase letters (no capital letters or accents), numbers, and dashes (-).

```
$ heroku create myawesomename
```

> Note: You have to specify something other than myawesomename, since
> myawesomename is probably already taken. If not it will be soon :)

If you ever feel like changing the name of your Heroku application, you can do so at any time with this command (replace the-new-name with the new name you want to use):

```
$ heroku apps:rename the-new-name
```

Note: Remember that after you change your application's name, you'll need to visit [the-new-name].herokuapp.com to see your site.

## Deploy to Heroku!

That was a lot of configuration and installing, right? But you only need to do that once! Now you can deploy!

By the way when we said this was the easist deployment setup we meant
it. Putting code on the web can get complicated!

When you ran heroku create, it automatically added the Heroku remote for our app to our Git repository. Now we can do a `git push` to deploy our application:

```
$ git push heroku master
```

Note: This will probably produce a lot of output the first time you run it. You'll know it's succeeded if you see something like https://yourapplicationname.herokuapp.com/ deployed to Heroku near the end of the output.


## Web Scale

You’ve deployed your code to Heroku, and specified the process types in a Procfile (we chose a web process type earlier). We can now tell Heroku to start this web process.

To do that, run the following command:

```
$ heroku ps:scale web=1
```

This tells Heroku to run just one instance of our web process. Since our blog application is quite simple, we don't need too much power and so it's fine to run just one process. It's possible to ask Heroku to run more processes (by the way, Heroku calls these processes "Dynos" so don't be surprised if you see this term) but it will no longer be free.

## Visit your application

We can now visit the app in our browser with heroku open.

```
$ heroku open
```

This will open a url like https://yourapplicationname.herokuapp.com/ in your browser.

You should now be able to see your website in a browser! Not only that,
your friend could visit the same url and see your work! Congrats :)!
