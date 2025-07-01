 eval "$(ssh-agent -s)" && ssh-add ~/.ssh/work_comp && ssh -T git@github.com 
