# Xpression

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

## Installation
<img src="static\Images\light.png"/>

Locally, clone this repository on your computer.
Run app.py using python3
Once the flask wsgi server is live, access the url displayed by flask from your browser. It's ````http://127.0.0.1:5000/```

To interact with our application visit this url

## Usage
Here is Youtube demo on using the web app.
[![How to use expression](static\Images\Youtube_screenshot.png)](https://www.youtube.com/watch?v=MgIZWGZnXgE)

##### How to search on Xpression
<img src="static\Images\Xpression -search_demo_Trimmed.gif" alt="search demo">

#### Contributing
- ###### Fraol Tolera
[Github](https://github.com/Fraol123)
[LinkedIn]
- ###### Claudette Mokeira
[Github]](https://github.com/keira-claudette)
[LinkedIn](https://www.linkedin.com/in/claudette-mokeira/)


#### Related Projects
Our web application is similar to:
- Giphy
- Tenor

#### Licensing
MIT License

#### Blog post about our developing this web app
[Here's a summary of our development journey]()
###### [Xpression landing page on github pages](https://keira-claudette.github.io/xpression.github.io/)
