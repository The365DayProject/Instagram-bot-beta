# Instagram-bot-beta
A python automated instagram bot to comment on giveaways.

This is my first attempt at building a web scrapping python app that automates commenting on instagram giveaways.

The app saves information in a .txt form locally, such as your comments, your credentials and the last giveaway link you used

The ui offers the following options to the user:
1) Credentials for logging in instagram.
2) Paste instagram giveaway link.
3) Choose number of tags @ required.
4) Enter the list of comments.
5) Choose the commenting frequency.

How to run:
1) Open cmd and go to the folder of the project
2) Run the main.py file (python main.py or py main.py or py -m main.py)

How to comment:
1) Place your comment in the corresponding box in the form (@jlo @cristiano @leomessi) where of course in your case you can @[add name of user].
2) Click the 'Add comment' button.
3) To add another comment, delete the previous text and repeat the above.

The script picks only the comments that meet the giveaways' requirements, meaning that it matches the number of tags to the number of required tags the user have entered.
(e.g. If the user enters 5 different comments, 2 of which have 3 people tagged and the rest having 2 people tagged, if the giveaway requires to tag 3 people it will pick the 2 comments that have the 3 tags)
From the comments that meet the requirements the script will pick one at random each time it posts a comment.

Requirements:
1) python 3
2) latest version of chromedriver

Python modules needed:
1) tkinter
2) time
3) selenium
4) random
5) os

As I mention in the beggining, this is my very first attempt at such an application and hence it is more than certain that it will have mistakes. Please if you have the time and knoweledge required, I would greatly appreciate all comments and/or suggestions.

Useful links:
https://chromedriver.chromium.org/
https://www.python.org/downloads/
https://docs.python.org/3/installing/index.html
