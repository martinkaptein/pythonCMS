import os, shutil
import sys

print('Welcome to pythonCMS, the simplest CMS in the universe!')
slug = input('Enter url slug (e.g. "my-awesome-post"): ')
title = input('Enter title of your post: ')
description = input('Enter description of post: ')
blogFilename = input('Enter filename of blog (e.g.: draft.html): ')

#build file paths
blogFileLocation = os.path.join("drafts/drafts/", blogFilename)
targetDir = os.path.join("posts/", slug)
targetPath = os.path.join(targetDir, blogFilename)
correctTarget = os.path.join(targetDir, "index.html")

#check if user input was valid
if not os.path.isfile(blogFileLocation):
    sys.exit("Error: Blog file does not exist.")

#make new dir for post


os.mkdir(targetDir)

#copy blog file from drafts/drafts to targetDir
shutil.copy2(blogFileLocation, targetDir)

#rename to index.html
os.rename(targetPath, correctTarget)

#concatenate HTML element
contentToInsert = '\n<h4><a href="' + targetDir + '">' + title + '</a></h4><p>' + description + '</p><br><br>'


#modify menu page to include the new post
lookup = '$InsertLatestPostBelow'

with open("index.html") as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            lineInsert = num + 1
            f = open("index.html", "r")
            contents = f.readlines()
            f.close()

            contents.insert(lineInsert, contentToInsert)

            f = open("index.html", "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
            
            
            
            
print('Success!')
print('Open the root index.html file to see your new post.')
    
    
    


