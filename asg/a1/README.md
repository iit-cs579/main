## Assignment 1

**50 points**  

# Setup

1. Learn Python by complete the online Python training course at <http://www.codecademy.com/tracks/python>.
  - At a minimum, you must complete the [Advanced Topics in Python](https://www.codecademy.com/courses/python-beginner-en-KAgt5/0/1) module. If you're new to Python, you'll likely have to complete many of the earlier modules as well.
  - In your repository, upload a screenshot showing that you have completed the module. **Name the file python.pdf**
  - This screen shot should be of your badges, which shows your username and the Advanced Topics in Python badge (e.g. https://www.codecademy.com/users/YOUR_USER_NAME/achievements)

2. Learn git by completing the online training course at <http://try.github.io>.

3. Create a GitHub account and email me your github name (along with your IIT email address and full name).

3. Install the Python/SciPy stack on your computer (if you haven't already) by follwing the instructions here: <http://continuum.io/downloads>. We'll be using Python 2.7, **not** Python 3. I recommend using Linux/Mac for this class, but Windows should work as well. 

3. Install Pip <http://pip.readthedocs.org/en/latest/installing.html>. Pip allows you to install additional Python libraries.

3. Install ipython: `pip install ipython` [**nb**: If you did step 4, this should already be installed]

5. Install Git
  - Windows:
    - Download the installer from <http://msysgit.github.io/> and run it
    - Download and install the [GitHub app](https://github-windows.s3.amazonaws.com/GitHubSetup.exe)
  - Mac/Linux: Check if git is already installed by running `which git`
    - To install on Linux: `sudo apt-get install git` (Ubuntu) or `yum install git-core` (Fedora)
    - To install on Mac: <http://sourceforge.net/projects/git-osx-installer/>

6. Setup Git: <https://help.github.com/articles/set-up-git>
  - Mac/Linux only: Generate SSH keys <https://help.github.com/articles/generating-ssh-keys>

7. Clone your private class repository [Note, you won't be able to do this until we create this repo for you, likely a week after class starts.]
   ```
   git clone https://github.com/iit-cs579/[YOUR_GITHUB_ID-asg].git
   ```
  E.g., for me this would be:
  ```
   git clone https://github.com/iit-cs579/aronwc-asg.git
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
  
1. Complete the data collection assignment, following [a1.ipynb](http://nbviewer.ipython.org/github/iit-cs579/main/blob/master/asg/a1/a1.ipynb). 
2. Push your all your code and supporting files (.cfg, .txt, .json) to your **private** GitHub repo under `asg/a1`
