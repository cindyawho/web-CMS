# web-CMS
Using Python, I will create a rudimentary web content management system.

## Build Your Own Content Management System

To run, download the repo, then in terminal:  
<code>python .\createSiteFiles\main.py</code>

From CIS 112D Advanced Python:
### Introduction:
Content management systems (CMS) are crucial for modern web development, offering a robust framework for creating, managing, and optimizing digital content with ease and efficiency. They enable users, regardless of their technical proficiency, to design and update websites through user-friendly interfaces and pre-built templates, thus democratizing web publishing. CMS platforms like Wordpress now comprise the majority of websites available on the web.

A content management system (CMS) is a full stack application that includes both front-end and back-end components. On the front end, it provides templates, themes, and user interfaces that allow users to create and manage content easily. On the back end, it includes a database to store content, server-side scripts to process user requests, and administrative tools for managing the site. This combination allows users easily to build, edit, and publish content within a single platform.

For your final project you will create a rudimentary web content management system. This will comprise virtually all modules covered in this course. 

### Components:
1. <b>Content Editing UI</b>: 
Your app will include a GUI application that can read in and modify the text of a webpage you will want to to publish

2. <b>Static Data Storage</b>: 
You will create a module to retrieve and edit a static file (exp: a JSON file). This will serve as static storage for your app. Anytime your user edits the content via the GUI the update should be stored in the JSON file.

3. <b>Webpage Creation</b>: 
Whenever your user edits content, the app should also publish a static webpage file with the revised content, overwriting previous drafts of the site. Make a module that does this and have the GUI import it as part of the operations of the app. 

4. <b>Server File Hosting</b>: 
You should independently run a webserver that will send the webpage file to any client that requests it. Users should be able to navigate to the host location via a browser and load the webpage on demand.

5. <b>Class and Module Construction</b>: 
You will employ classes and modules to construct the various elements of your application.

## Concept

### Ideas:
- Blogging
- Personal Book Journal/Tracker
- Project Portfolio
- Library-related site
- Fictional Character database like fandom wikis

### Personal Book Journal

- Home page: users will edit their name, journal title and their latest book entry
- Latest Book entry: date read, title, author, rating, thoughts on the book, cover image
- Going beyond req's: users can create multiple pages for each of their book entries
- CSS style:
  - background color
  - font color
  - title font
  - all other font

#### Figma Design

Tkinter Inputs needed:
https://www.figma.com/design/1LKiPaDYrf1I9lPZohOQoc/Tkinter-Content-Management-System?node-id=0-1&t=54Q2t0oJrWdt1UAA-1
