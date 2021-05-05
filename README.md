# Instagram-bot-beta
A python automated instagram bot to comment on giveaways.

This is my first attempt at building a web scrapping python app that automates commenting on instagram giveaways.

The app saves information in a .txt form locally, such as your comments, your credentials and the last giveaway link you used

The ui offers the following options to the user:
-Credentials for logging in instagram.
-Paste instagram giveaway link.
-Choose number of tags @ required.
-Enter the list of comments.
-Choose the commenting frequency.

How to comment:
-Place your comment in the corresponding box in the form (@jlo @cristiano @leomessi) where of course in your case you can @[add name of user].
-Click the 'Add comment' button.
-To add another comment, delete the previous text and repeat the above.

The script picks only the comments that meet the giveaways' requirements, meaning that it matches the number of tags to the number of required tags the user have entered.
(e.g. If the user enters 5 different comments, 2 of which have 3 people tagged and the rest having 2 people tagged, if the giveaway requires to tag 3 people it will pick the 2 comments that have the 3 tags)
From the comments that meet the requirements the script will pick one at random each time it posts a comment.

Requirements:
-python 3
-latest version of chromedriver

Python modules needed:
-tkinter
-time
-selenium
-random
-os

As I mention in the beggining, this is my very first attempt at such an application and hence it is more than certain that it will have mistakes. Please if you have the time and knoweledge required, I would greatly appreciate all comments and/or suggestions.
