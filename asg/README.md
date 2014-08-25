All assignments should be submitted to your private GitHub repository. To submit an assignment:

1. Update your private repository to get the assignment files:
  ```
  cd [my_repo_name]
  git pull
  ```

2. Do the homework, adding and modifying files in the proper assignment directory (e.g., `asg/a1`). **Commit often!**

3. Before the deadline, push all of your changes to GitHub. E.g.:
  ```
  cd asg1/a1
  git add *
  git commit -m 'homework completed'
  git push
  ```

4. Double-check that you don't have any outstanding changes to commit:
  ```
  git status
  # On branch master
  nothing to commit, working directory clean
  ```

5. Double-check that everything works, by cloning your repository into a new directory and executing all tests.
  ```
  cd 
  mkdir tmp
  cd tmp
  git clone https://github.com/iit-cs579/[your_iit_id]
  cd [your_iit_id]/asg/a1
  [...run any relevant scripts/tests]
  ```
6. Question about the assignment? You can [create an issue](https://github.com/iit-cs579/main/issues), which we will use like a message board. Either myself or a fellow student can answer.
