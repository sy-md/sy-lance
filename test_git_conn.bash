 eval "$(ssh-agent -s)" && ssh-add ~/.ssh/android  && ssh -T git@github.com 
