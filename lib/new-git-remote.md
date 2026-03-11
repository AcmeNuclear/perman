# new-git-repo

*>>> perman Reference Page*

# Git: set new up-stream remote-tracking repo for local repo

**Repository with same name assumed to be resident on remote
prior to starting this command sequence.** This repository should
be created with no content (README.md, LICENSE.md, .gitignore) so
local content can be directly pushed to new remote repo. 

Local repository should already exist and Git is initialized for it. 

```
# Ensure primary branch is named "main" (branch being used)
  > git branch -avv
  > git branch -M main

# Ensure all local changes are committed
# Add the new remote as name origin per convention
  > git remote add origin https://someorg.com/user/repostory.git

# Set up-stream to origin and push local contents to remote
  > git push --set-upstream origin main 
  OR
  > git push -u origin main

# Validate
  > git branch -avv
```

-------