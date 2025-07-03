 eval "$(ssh-agent -s)" && ssh-add ~/.ssh/hyper && ssh -T git@github.com 
