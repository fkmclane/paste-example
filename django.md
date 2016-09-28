# Django + Web Technologies

By: Foster McLane

Note:
The the audience to please ask questions during the presentation since it has a lot of information, much of which may be foreign.



# Introduction to MVC

Note:
MVC is short for Model-View-Controller. It is a paradigm for creating applications that focuses on clean separation of code and well defined behavior of components.


## Model

* how the data is stored
* contains some inherent interactivity with the data
* usually part of the "backend" of an application


## View

* how the data is viewed
* usually the "frontend" of an application


## Controller

* how the data is interacted with
* usually part of the "backend" of an application


## Django Is A Bit Different

In Django, what we call the "view" is called a "template", what we call the "controller" is called a "view". Django generally regards itself as an "MTV" framework, or model, template, view, to accomodate this.



# Introduction to Django


## Websites

* Django is built around projects or websites that contain webapps
* we will only have one webapp in our case

Note:
Go ahead and start a website with a witty name from the audience.


## Applications

* a website can have multiple webapps under particular URL namespaces
* a webapp can also be shared between websites

Note:
Create the webapp "pastebin".


## Model

* the model automatically stores data and converts to and from Python types
* the backend can be chosen between several flavors of SQL and Oracle DB
* Django handles storage and selection with a rather intuitive Python interface

Note:
Ask the audience what information they would like in the pastebin. Give a few obvious answers such as "name" and "code". Be sure to activate the model and register on the admin site. Show off the model API ('all', 'filter', 'get') in the shell.


## Admin

* allows an administrator to modify website data
* gives direct access to the database in a friendly format

Note:
Go ahead and add a paste here to be used for creating the first view.


## Views

* mediate HTTP interactions with the data
* use templates to generate HTML output

Note:
Ask the audience what views we need, giving them a few obvious answers such as "index" and "paste". Be sure to add urls to project. Start with "paste" view.


## Templates

* take context information and turn it into HTML

Note:
Ask audience what context we'll need for the "paste" view.



# Brief Introduction to HTML


## Tag Oriented Markup

* most tags are found in nested pairs with a begin and end tag
* some tags are singular and only have one tag
* between the tags are a combination of more tags and possibly text

```html
<p>Some <span>HTML</span> with an <img src="img.png" alt="image"/></p>
```


## Common Tags

* html - document root
* head - heading information about document
* body - displayed content of document


## Head Tags

* title - title of the document
* style - style information about document


## Body Tags

* div - divider and general content holder
* p - paragraph
* input - user input
* img - image
* form - submittable form


## Semantics vs. Styling

* HTML provides structure and semantics
* CSS provides styling

```html
<style>
p {
	color: red;
}
</style>

<p>The 'p' tag indicates that this is a paragraph and
the above CSS indicates that all paragraphs should be red.</p>
```

Note:
We will use styling, but it will be fairly minimal so do not get too caught up in what is available in CSS.


## Scripting

* standard language is Javascript
* HTML is available and mutable via the Document Object Model, or DOM
* other features, such as prompting the user for information, are available in addition to the DOM

Note:
We won't do any scripting (except for the dropdowns) so we will not worry too much about this part.



# Creating the Pastebin


## Model

We have already created the model, but is it complete?

Note:
Make sure to add remaining information to the model and run migrations.


## Templates

What templates will we need?

(hint: What views will we have?)

What context will we need?

Note:
Create very basic HTML versions of the templates.


## Views

What will we need to do with what requests?

Note:
Create GET views then show how to get POST data from an HTML form.



# Pygments for Syntax Highlighting


## Simple Construction

```python
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

lexer = get_lexer_by_name(paste.language, stripall=True)
formatter = HtmlFormatter(linenos=True)

highlighted = highlight(paste.code, lexer, formatter)
```

Note:
Do not forget to 'mark\_safe' in the context to allow HTML output



# Make This Look Good With Semantic UI


## Requirements

```html
<script src="//cdn.jsdelivr.net/jquery/3.1.1/jquery.min.js"></script>

<link rel="stylesheet" href="//cdn.jsdelivr.net/semantic-ui/2.2.4/semantic.min.css"/>
<script src="//cdn.jsdelivr.net/semantic-ui/2.2.4/semantic.min.js"></script>
```


## Global Header

* need a nav bar
* need to create the "logo" button
* need to link to all relevant pages

Note:
Ask what the relevant pages are (basically whether they want admin or not there).


## Main Container

* need centering
* needs to be move a bit down from the top


## Paste Page

* needs metadata
* needs highlighted code


## Latest Page

* needs a list
* needs metadata


## Index Page

* needs a greeting
* needs a form



# What About Deleting Expired Entries?


## A Solution

There is no good way (yet) in Django to run periodic functions, but we can create a "view" that runs periodic functions and can be CURLed from a crontab.

Note:
Curl is a program to interact with the web.



# Questions?
