## Assignment 1

*50 points*

# Setup

1. Learn Python by complete the online Python training course at <http://www.codecademy.com/tracks/python>.

2. Learn git by completing the online training course at <http://try.github.io>.

3. Install the Python/SciPy stack on your computer (if you haven't already) by follwing the instructions here: <http://continuum.io/downloads>. We'll be using Python 2.7, **not** Python 3. I recommend using Linux/Mac for this class, but Windows should work as well. 

4. Install Pip <http://pip.readthedocs.org/en/latest/installing.html>. Pip allows you to install additional Python libraries.

5. Install Git
  - Windows:
    - Download the installer from <http://msysgit.github.io/> and run it
    - Download and install the [GitHub app](https://github-windows.s3.amazonaws.com/GitHubSetup.exe)
  - Mac/Linux: Check if git is already installed by running `which git`
    - To install on Linux: `sudo apt-get install git` (Ubuntu) or `yum install git-core` (Fedora)
    - To install on Mac: <http://sourceforge.net/projects/git-osx-installer/>

6. Setup Git: <https://help.github.com/articles/set-up-git>
  - Mac/Linux only: Generate SSH keys <https://help.github.com/articles/generating-ssh-keys>

7. Clone your private class repository **[I'm still waiting on the accounts to be created, so this may not work yet (8/24/14)]**
   ```
   git clone https://github.com/iit-cs579/[iit-username].git
   ```
  E.g., for me this would be:
  ```
   git clone https://github.com/iit-cs579/aculotta.git
  ```
  - You should have read/write (pull/push) access to your private repository.
  - This is where you will submit assignments.

8. Update your private repository with `git pull`

9. Modify the README.md file in your repository to list your name.
  - Checkin this change with:

  ```
  git add README.md 
  git commit -m 'my first commit'
  git push
  ```
  
  # Data Collection
  
  **[in progress]**
