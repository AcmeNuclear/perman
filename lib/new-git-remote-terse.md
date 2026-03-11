# new-git-repo

*>>> perman Reference Page - Terse*

# Git: set new up-stream remote-tracking repo for local repo

**Empty repository with same name resident on remote to begin sequence.**

Local repository already exists. 

```
  > git switch <main>
  > git branch -avv
  > git branch -M main   # if needed

  > git commit ...       # if needed

  > git remote add origin https://someorg.com/user/repostory.git
  > git push [ --set-upstream | -u ] origin main 
```

-------