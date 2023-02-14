## Instructions for git (from DataCamp class)

`git status` - display a list of the files that have been modified

`git diff` - display the differences between two sets of files / commits / branches  
`git diff branch1..branch2`  
`git diff commit1..commit2`

`git diff filename` - display changes to filename

`git diff directory` - changes to the files in directory

`git add filename` - add one or more files to the staging area

    `HEAD` is a shortcut meaning "the most recent commit"

`git diff -r HEAD` - compare the state of your files with those in the staging area

`git commit -m "message"` - save the changes in the staging area

`git commit --amend -m "new message"` - change commit message

`git log` - view the log of the project's history

`git log path` - inspect only the changes to particular files or directories

`git commit` - launche a text editor with a template to write a message

`git show commit-hash` - view the details of a specific commit with cimmit-hash (the first few characters of the commit's hash)

    `HEAD` - the most recent commit  
    `HEAD~1` - the commit before it  
    `HEAD~2` - the commit before that, and so on

`git annotate filename` - show who made the last change to each line of a file and when

`git clean -n` - show a list of files that are in the repository, but not currently tracking  
`git clean -f` - delete those files

`git config --list` - see what the settings are, with one of three additional options:

    `--system`: settings for every user on this computer  
    `--global`: settings for every one of your projects  
    `--local`: settings for one specific project  

`git config --global setting value` - specify the setting you want to change and the value you want to set

`git reset HEAD` - unstage the additions

`git checkout -- filename` - discard the changes that have not yet been staged

`git checkout commit_hash filename` - replace the current version of filename with the version that was committed with commit_hash

`git branch` - list all of the branches in a repository

`git diff branch1..branch2` - show the difference between two branches

`git checkout branch-name` - switch to branch-name.

`git rm filename` - remove the file then stage the removal of that file with git add, all in one step

`git checkout -b branch-name` - create a branch then switch to it in one step

`git merge source-branch destination-branch` - merge two branches

`git init project-name` - create a repository for a new project in the current working directory

`git init` - convert existing project into repository (run in the project's root directory)

`git init /path/to/project` - convert existing project into repository (run from anywhere else on your computer)

`git clone URL` - clone a repository from URL

`git remote` - list the names of repository's remotes

`git pull remote-name branch-name` - get changes from branch-name (ex. master) in the repository associated with the remote-name (ex. origin) and merge them into your branch

`git push remote-name branch-name` - push the contents of branch-name in the remote-name

`git branch -d branch_name` - delete local branch that is merged

`git branch -D branch_name` - force delete of a local branch

`git fetch -p` - update branch list and delete non-existing references

`git switch branch_name` - If branch_name exists on the remote repository, but not on your local branch (automatically set up remote branch tracking)
