# Creating new repository from the local copy

## From Terminal(Mac)
1. Navigate to the local working directory
> cd /path_to_local_working_directory
1. Initiate the local working directory as a git repository
> git init .
1. Add all the local files to the repository
> git add .
1. Check the status of the files added/modified from your working directory
> git status

  _NOTE: Since this is the first initialization all the files present in your local working directory will be marked as new file_
1. Commit the changes with a sensible comment/message (-m)
> git commit -m "\<ID/Name>: Creating an inital repo"
1. Now login to your github.com and create the repository with local directory name.
1. Once created it should display instructions on how to create a new repository or push an existing repository from command line. Copy those somewhere safe.
2. If this is your first time working with local directory and remote repository then check the following steps else skip the first time setup

  #### **First time setup:**
  You have to generate ssh keys first and add that to the ssh agent. Refer [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

  If you already have a key or have genereted from the above url then its time to add it to your GitHub account. Refer [Adding a new SSH key to your GitHub account](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

  Once added now go back to your Terminal and try running
  > ssh -T git@github.com

  It should display your username and say **You've successfully authenticated**

1. Add remote GIT url
> git remote add origin git@github.com:\<userName>/\<repositoryName>.git

  If you make a typo or need to update the URL then you can still update it
  > git remote set-url origin git@github.com:\<userName>/\<repositoryName>.git
1.  Once added you can verify it
> git remote -v
1. Create a new branch
> git branch -M main
1. Push the changes to a remote repository
> git push -u origin main

  _NOTE: Make sure all the changes are commited before the push. You can check that using <git status> if in doubt_
