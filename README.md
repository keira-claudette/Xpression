# Xpression

<blockquote class="imgur-embed-pub" lang="en" data-id="a/1rdJiQh" data-context="false" ><a href="//imgur.com/a/1rdJiQh"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
<br>

###### Sometimes words aren't enough!
<br>

## Introduction

Xpression is a web application that displays gifs to users.You do not have to be logged in to explore the appliation but if you do, then you will be able to save your favorites.<br>
Xpression also allows users to search for gifs that fit a certain theme. You could for instance search dancing gifs or happy birthday. <br>
The main aim of this project is to get to work with APIs and to explore the whole Software Development Life Cycle.

## Technologies
###### Front-end
- HTML (static content)
- CSS (static content)
- JavaScript, jQuery (dynamic content)
###### Back-end
- Python (WSGI server)
- Sqlite3 (Database)

## Files
### /Static
- ##### /Images
Contains the logo in different formats and icons only.
- ##### /scripts
Contains main.js file that uses jquery to dynamically fetch and display content on the homepage.<br>
Currently, the homepage displays trending gifs which change everyday or even every few hours.
- ##### /styles
This folder contains the css files for the different templates of the web application.
- ##### /templates
This contains html templates to be rendered using flask render_template in order to serve dynamic content and to enable user sign up and log in.

### app.py
This is our WSGI server. 

### database.db
This is our database that saves user details after they sign up and track user's favorites.

## Launch 
To interact with our application ...

###### [Xpression landing page on github pages](https://keira-claudette.github.io/xpression.github.io/)
