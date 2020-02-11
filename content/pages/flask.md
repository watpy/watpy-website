Title: Flask
Date: 2020-01-15 20:00

> This work is licensed under the Creative Commons
> Attribution-ShareAlike 4.0 International License. To view a copy of
> this license, visit
> [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/).

We have a blog that we can kind of use through the command line, but
really blogs are on the web and used through a browser.

[Flask](http://flask.pocoo.org/) is the simplest web framework for Python. With just a few lines we
can take what we have and run it locally as if it was on the internet.

Since Flask is a 3rd party library we need to install it before we can
use it.

```
pip install --user flask
```

> If you are using Mac OS X/Linux you will need to type `pip3` instead of `pip`


## Your First Flask App

Use your editor to create `interface.py` and type in the following basic
`flask` application:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Internet!"

if __name__ == "__main__":
    app.run(debug=True)
```

There is that `__name__` again. We are close to explaining it.

`app` is an instance of a class provided by the Flask framework and
`app.run()` runs the development web server which allows us to test out
how this Flask thing works.

You can run it the same way you ran the `blog.py` program.

```
$ python interface.py
```

This program doesn't return to the command prompt, it outputs:

```
 * Running on http://127.0.0.1:5000/
```
and a blank line.

The server will keep running until you type Control (or CTRL) and the
letter "c".

While the server is running you can type `http://127.0.0.1:5000/` into
your browser URL bar and test out your program!

## Reusing your `blog.py` code with Flask

We have a blogging engine in `blog.py` and an web interface, now lets
combine by implementing the index part of our online blog.

To do that we will have to import the code from `blog.py`. We have
imported code from the Python standard library and Flask but this out
first time doing it from our own file.

In `interface.py` alter the top section:

```python
from flask import Flask
from blog import index, get_post

app = Flask(__name__)
```

The import line makes the `index` and `get_post` available to us in the
`interface.py` file.

> `if __name__ == __main__:` comes in right here. When you import a file
> like `blog.py` it runs the code in the file, but we don't want to run
> the code which provided our command line interface. When you run a
> program directly `python file.py`, then `__name__` is set to "__main__"
> by Python. This condition allows us to define code in a file which
> only get run when we run the file directly.

We can use the `index` function we defined earlier to create a view (a
function which returns HTML) in flask to start our blog app.

Replace the `hello` function with:

```python
@app.route("/")
def home():
    slugs = index()
    return "<br>".join(slugs)
```

The `interface.py` file should look like this now:

```python
from flask import Flask
from blog import index, get_post

app = Flask(__name__)

@app.route("/")
def home():
    slugs = index()
    return "<br>".join(slugs)

if __name__ == "__main__":
    app.run(debug=True)
```
## Blog Post Page

We need another view to look at individual blog posts. Just like with the
command line interface we need to be able to tell the view which blog
post we want to view using the slug like we did last time.

Flask lets us do this through the `route` function/decorator.

> Decorators are a more advanced concept, but using them very straight
> forward. For the curious a decorator take a function as its argument
> and returns another function.

Let's define a `post` view below the `home` view:

```python
@app.route("/<slug>")
def post(slug):
    content = get_post(slug)
    return content
```

When you go to `http://127.0.0.1:5000/` see your index page and you can manually to each post with `http://127.0.0.1:5000/first-post` and any other slug you have defined.

Cool.

The next step is to hook up it up using templates and links so you can go from the index page to each post.

## Templates

Most web frameworks have a built in templating system. Templates enable
you to write some of the more repeative aspects of HTML once and
reuse them. Think of the header, footer or navigation on your favorite
website. They apper on on every page, but we want want to duplicate it.
If we did then a change in the footer would have to be made across all
the pages in a web application!

Flask uses a template language called [Jinja2](http://jinja.pocoo.org/)
and we will cover some of it today, but there is more when you are ready
to learn about it.

> If you are interested in Django, a more powerful web framework written
> in Python, its template language is similar to Jinja2, and the latest
> release of Django works with Jinja2 directly.

Flask looks for your template files in folder called `templates` right
beside `interface.py`. Create the folder called `templates` either with
the commandline or your file explorer.

Use your editor to create a file called `base.html` in `templates` and type in the
following:

```
<!DOCTYPE html>
<html>
<head>
  <title>My Blog</title>
</head>
<body>
  {% block content %}
  {% endblock content %}
</body>
</html>
```

This is basically the start and end of the two blog posts you wrote in
the last section, but instead of the main part, the header and text, we
have put in a placeholder `{% block content %}`. Jinja2 will pass
through the HTML we write in our templates but it will process two kinds
of special markup. The first is block which we just saw. The second is
inserting data which uses a syntax like `{{ foo }}`. We will see an
example shortly.

Next create a file called `post.html` in `templates` and type in the
following:

```
{% extends "base.html" %}
{% block content %}
{{ post|safe }}
{% endblock content %}
```

This template has no HTML in it at all, but it is still valid. `{% extends "base.html" %}` tells Jinja2 to use that template first and then apply this template. What that means is inside `post.html` we can override `blocks` in `base.html`.

The only block in `base.html` was `{% block content %}`. In `base.html` it contained nothing, but here we are placing `{{ post|safe }}` inside of it.

`{{ post }}` get the value post out of the context (which we will see below) and inserts into the HTML. The `|safe` says to pass the content in `post` through the `safe` filter. There are filters for date and time formatting among other things. They are like functions you can use in the template.

> The `safe` filter tells Jinja2 that if the value, in this case `post` contains HTML let it through. Normally Jinja2 would escape it to prevent malicious HTML from untrusted soruces, but we trust ourselves since we are writing the blog posts.

Instead of `{{ post|safe }}` we could have written

```
<h1>First Post</h1>
<p>Hello, Internet!</p>
```

But we want to write only one template for all blog posts instead of a
template for each one.

The next step is to use the template in your `post` function. Type out
the new import and the changes in the `post` function:

```python
from flask import Flask, render_template  # Change this line
from blog import index, get_post

app = Flask(__name__)

@app.route("/")
def home():
    slugs = index()
    return "<br>".join(slugs)

@app.route("/<slug>")
def post(slug):
    content = get_post(slug)
    return render_template('post.html', post=content)  # Change this line

if __name__ == "__main__":
    app.run(debug=True)
```

`post=content` is where we define the context of which varibles are available in our template.

This should work, except the content inside each of your blog post file
includes `<html>` and `<head>` element which aren't needed any more.

Edit your "first-post.html" to remove everything in the `base.html`:

```
<h1>First Post</h1>
<p>Hello, Internet!</p>
```

Do the same for any other blog posts you have written.

Now you can run the server again, and you should see you first post
again at `http://127.0.0.1:5000/first-post/`. When you call `post`, the
file is read and put into the `content` variable. Then in the
`render_template` line we pass `content` in as `post` and the `{{ post
}}` part in the template takes the value in `post`, what was in
`content` and inserts it into the resulting HTML.

## Better Home Page

We have come a long way and you have done a great job! The last step is
to make the index of the blog link to each post with a template.

Use your editor to create `templates/home.html` and type in the
following:

```
{% extends "base.html" %}
{% block content %}
<h1>My Blog</h1>
<ul>
{% for slug in slugs %}
<li><a href="{{ url_for('post', slug=slug) }}">{{ slug }}</a></li>
{% endfor %}
</ul>
{% endblock content %}
```

This template has two new things, first is a `for` loop. It works the
same as the `for` loop you are familar with in Python, though it is
specific to Jinja2.

The second is the `url_for` which is a helper function provided by flask
to construct the correct url given the name of a function view and the
data passed into it.

Update the `home` function in `interface.py`:

```python
@app.route("/")
def home():
    slugs = index()
    return render_template("home.html", slugs=slugs)  # Change this line
```

Re-run your application and you should have a blog you can surf around.

After well deserved break we are going to put it on the Internet!
