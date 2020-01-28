Title: File Based Blog
Date: 2020-01-15 20:00

> This work is licensed under the Creative Commons
> Attribution-ShareAlike 4.0 International License. To view a copy of
> this license, visit
> [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).

Our project for today is to create a blog!

It will be a collection of files which represents posts with the ability
to retrieve an index of all posts.

For now we will just interact with it on the command line, but
eventually we will put it on the internet with a library called Flask
but more on that later.

## Files

One critical ability most programming environments provide is the power
to manipulate files on your local disk.

With Python you can create files, edit files and even delete files! You
can use this power to automate all sorts of things.

For now our goal to make our blog work is to open and output the
contents of text files.

> We will be writing a very simplified version of the `cat` command for Mac OS/Linux.
> After you are done this project think about how
> you could extend it to implement more of the features of `cat`.

## Your first program

Before we get to opening files, let's start with everyone first program,
"Hello, World!". Writing and running this simple program will make sure
everything is working for us before we forge ahead.

Using your editor, create a file called `blog.py` and carefully type out
the following code:

```python
if __name__ == "__main__":
    print("Hello, World!")
```

> Why is it called `blog.py` and not something like `hello.py`? We are
> just using this simple program to verify that things are working as we
> expect. This is a technique every programmer often use to help test
> assumptions, we will make it more like a blogging engine soon enough :)

Make sure you save `blog.py` and then switch to your command line window
and try running it.

```
$ python blog.py
```

If everything went well you should see "Hello, World!" on your command
line screen. If there is some kind of error see if you can figure out
what went wrong, ask a friend or a tutor. This is where the real learning
happens.

Awesome, we now have a flow where you can edit your code in your editor
and run it on the command line. Let's create!

> If what == what? For now don't worry too much about `if __name__ ==
> "__main__":`. We admit it is weird and unexpected. It is there to
> solve a problem you don't know you have yet, so go with it. We will explain
> it later in the day.

## Opening Files

Like `print` Python has a built in function which make it easier to open
file. It is called `open` and it takes the name or path to the file and
a hint about what you want to do with it, read or write or both.

```python
blog_post = open("somefile.html", "r")
```

In this example "somefile.html" is the name of the file we expect to
find on the file system right beside `blog.py` and "r" indicates to the
`open` function that we want to read the file.

> You could also try to open "myfolder/somefile.html" and the `open`
> function will look for the folder "myfolder" beside our code file,
> `blog.py` and then for "somefile.html" in that folder.

Let use open in `blog.py` and replace the `print` line. When you are
done typing you want to look like this:

```python
if __name__ == "__main__":
    blog_post = open("somefile.html", "r")
```

Try running that:

```
$ python blog.py
```

Oh no and error!

```
Traceback (most recent call last):
  File "blog.py", line 2, in <module>
    blog_post = open("somefile.html", "r")
IOError: [Errno 2] No such file or directory: 'somefile.html'
```

It is ok though, Python is just trying tell us that we can't open a file
which doesn't exist so it gives up and ends the program for us while
printing out the exception (another word for error).

This shouldn't be too surprising, we haven't create a file called
"somefile.html".

### First Post

Use your editor to open up another file call it "first-post.html" and
type out the following:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Blog</title>
</head>
<body>
  <h1>First Post</h1>
  <p>Hello, Internet!</p>
</body>
</html>
```

Now we have a file we want to open let's make `blog.py` a bit more
interesting.

First we are going to open our file in a slightly different way. We will
combine the `open` function with the `with` keyword. We will also read
the file and output the lines using `print`.

When you are done it should look like this:

```python
if __name__ == "__main__":
    with open("first-post.html", "r") as blog_post:
      for line in blog_post.readlines():
        print(line, end="")
```

Run the program and see if it works.

Lets go line by line.

`with open("first-post.html", "r") as blog_post` is basically the same
as `blog_post = open("first-post.html", "r")` except when we leave the
indentation under the `with` statement the file will be closed for us.
If you don't do this you have to remember to write `blog_post.close()`
after you done with a file you have opened. It is easier to just let the
block do it for you.

Next we have a loop over the text lines in the file.

Inside the loop we use `print` to output the line. We include `end=""`
because `readlines` returns the line with the line endings already
there.

Using `readlines` to go through each line in the file can be a handy way to
manipulate the text in a file. For our blog we always want to output
everything, so instead we can use `read` on the file
which just grabs all the lines. Make the following changes:

```python
if __name__ == "__main__":
    with open("first-post.html", "r") as blog_post:
      print(blog_post.read(), end="")
```

Run the program and make sure it outputs the same text.

# Your Second Post

Let's step it up a notch with our second post. With your editor create
a file called `coding-is-pretty-cool.html` and type out the following:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Blog</title>
</head>
<body>
  <h1>Coding is Pretty Cool</h1>
  <p>I wrote my own blog and soon enough it will be on internet</p>
</body>
</html>
```

You could change `blog.py` to open `coding-is-pretty-cool.html`
manually, but we want to be able to show as many posts as we have
created. We can use a function and a argument to make our program
dynamic.

Let's start with writing a function which take the filename, without
the ".html" and returns the content or None if it can't find it. We will
call the filename with out the extension the "slug".

Type out the following code **above** the `if __name__ == "__main__"`
line in your `blog.py` file:

```python
import os
import sys


def get_post(slug):
    filename = slug + ".html"

    if not os.path.isfile(filename):
        return None  # There is no post with the slug provided

    with open(filename, "r") as blog_post:
        content = blog_post.read()

    return content
```

We have added some error checking here, if the `filename` based on the
`slug` isn't found on the disk we catch on the line `if not
os.path.isfile(filename):`. `isfile` is a function defined in the Python
standard library which returns `True` if the path provided is a file and
`False` if not.

Instead of just printing out the contents of the file we return it.

Next update the second line under the `if __name__ == "__main__":` to
make use of our new function:

```python
if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print("Please provide a slug!")
        sys.exit(0)

    slug = sys.argv[1]

    blog_post = get_post(slug)

    if blog_post is None:
        print("Unable to find post with slug {}".format(slug))

    print(blog_post, end="")
```

We have used the `sys` module from Python to allow us to access values
passed in from the command line when we run our program. This includes
some input checking.

The current file should look like:

```python
import os
import sys


def get_post(slug):
    filename = slug + ".html"

    if not os.path.isfile(filename):
        return None  # There is no post with the slug provided

    with open(filename, "r") as blog_post:
        content = blog_post.read()

    return content

if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print("Please provide a slug!")
        sys.exit(0)

    slug = sys.argv[1]

    blog_post = get_post(slug)

    if blog_post is None:
        print("Unable to find post with slug {}".format(slug))

    print(blog_post, end="")
```

Now we should be able look at both blog posts:

```
$ python blog.py first-post
$ python blog.py coding-is-pretty-cool
```

# Index Page

Awesome job, we have code that ouputs the contents of files which is kind of like `cat`. We can save
files to the disk and output them with our program. Our final task is to
list all the blog posts we know about when the user doesn't ask for a
particular post.

We will be using more of the `os` library which help see what files are on our
disk. The best way to do this is to define another function to do the
work for us.

You can put it below the `get_post` function.

```python
def index():
    slugs = []
    for filename in os.listdir('.'):
        if not filename.endswith('.html'):
            continue
        slugs.append(filename.replace('.html', ''))
    return slugs
```

Lets update the "__main__" section to output the index if you don't
provide a slug.

```python
if __name__ == "__main__":
    if len(sys.argv) < 2 :
        slugs = index()
        for slug in slugs:
            print(slug)
        sys.exit(0)

    # ...
```

The final results should look like this:

```python
import os
import sys


def get_post(slug):
    filename = slug + ".html"

    if not os.path.isfile(filename):
        return None  # There is no post with the slug provided

    with open(filename, "r") as blog_post:
        content = blog_post.read()

    return content


def index():
    slugs = []
    for filename in os.listdir('../../learn-to-code-with-python'):
        if not filename.endswith('.html'):
            continue
        slugs.append(filename.replace('.html', ''))
    return slugs


if __name__ == "__main__":
    if len(sys.argv) < 2 :
        slugs = index()
        for slug in slugs:
            print(slug)
        sys.exit(0)

    slug = sys.argv[1]

    blog_post = get_post(slug)

    if blog_post is None:
        print("Unable to find post with slug {}".format(slug))

    print(blog_post, end="")
```

Let's run out program:

```
$ python blog.py
$ python blog.py first-post
$ python blog.py coding-is-pretty-cool
```

We have a really simple blog that we can build on in the next section.
Huzzah!

> **Security** Most blogging engines take advantage of different storage
> technologies than the disk for a variety of reasons. One key reason is
> security. Someone might be access files you don't want them to using
> the system we have put together here. It is fine for learning and
> experimenting but don't try to take over the web with this code :)
