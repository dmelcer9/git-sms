# git mess

Allows you to send and recieve SMS messages, with git.

## Installation and running

 - Make sure you have git and python3 installed (along with pip)
 - Create a bare git repository on your server
 - Run install.sh
 - Set the environment variables that install.sh tells you to set
 - Run run.sh. It will automatically drop in the push hook based on the set environment variables
 - All phone numbers are in the format 15558675309
 
 ## Using
 
 - Create a file whose name is a phone number. Add a few lines of text, commit, and push. 
 - To send an attachment, add a line in the format exactly like `Attachment: https://my.image.com/path`
 - Check for new messages or replies with `git pull`
 - If you want to clear message history, delete first, then commit and push, then you can add new messages.
