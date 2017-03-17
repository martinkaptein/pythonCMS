# pythonCMS

PythonCMS

PythonCMS is a truly simple, yet very flexible static site generator, written in Python 3.

Why PythonCMS?

-It's truly simple to use (only basic HTML knowledge required; no Markdown or other config files)
-It fully portable (just upload the full folder to the server)
-You are truly in control of what happens
-No local webserver required
-Incredibly easy theming (more on that later)
-Easy Search Engine Optimization (SEO)
-AMP (Accelerated Mobile Pages by Google) support build in

Instructions:
-Download (or clone) the repo and unzip into the directory of your future blog

-Only thing you will need is python 3.x (free download from https://www.python.org/)

-Edit root index.html to your liking, it will become the main menu for the blog (there are explanatory comments)

-Your working directory is drafts/drafts
-Write your first blog entry in drafts/drafts/post.html; again change it however you want (meta tags)

-feel free to get rid of example-post in posts/ and root index.html (menu)

-For media (e.g. images) put them into media folder and link 2 levels up from the index.html (like so: src="../../assets/img/yourimage.jpg")

-preview your post by opening the .html file you just edited (no local webserver neccessary for preview).

-Run pythonCMS.py (cd to dir & run 'python3 pythonCMS.py' or double - click on windows) and follow the instructions on screen (it will generate the neccessary folders and add your post to the root index.html)

-upload the whole directory to your server

Done!


Notes:

-Default theme has been gracefully copied from http://blacktie.co/  >> props to them for their amazing work



Theming:
-you can change everything except:
--for $InsertLatestPostBelow (in the root index.html); it's required for PythonCMS to work
--For styling and javascript, make sure draft_filename.html links 2 levels up (like so: src="../../assets")
Done!


AMP:
See https://ampbyexample.com/ for theming, then apply standart theming procedure for this static site generator.



//this file is for the github .md
