# TASK-0: Get Your Environment Set-up

![image](https://user-images.githubusercontent.com/91676235/140823339-945f1115-0f09-40ff-8b8a-f3d37fbdc208.png)

## TASK-0.0.0: Email me
1. Email me with your circle account. That way I can invite/make you various accounts.

My email: cody.harris@circledelivers.com

## TASK-0.0: Install Python
1. Your computer probably doesnt have Python, but check if it does. Open the command line or powershell and type the following
```
python --version
```
If you get an error or the version isn't 3.8 install 3.8 which is what we will use for the meantime. I really wanted to use 3.9 to get the walrus operator because it's awesome but iirc AWS EC2 doesn't have 3.9 and I had to refactor code in the past.

2. Go here: https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe
3. Scroll to the bottom and download and install the file that says "Windows x86-64 executable installer"
4. During the install you will see a screen like this, make sure the box is checked to add Python to your PATH directory. We will run a lot of command line programs and you need anything the command line needs file wise, to be in the PATH variable.
![image](https://user-images.githubusercontent.com/91676235/140785447-8ab9aae6-94ce-4d42-ba75-108e09f7a33c.png)  
***I know this says 3.7, I pulled it off the internet***
5. After install is complete run the code above and verify you have Python Version 3.8

## TASK-0.1: Install Git and Github CLI
1. Go to the command line, type in "git". If you get an error, and not something like the image below you need to install git.
![image](https://user-images.githubusercontent.com/91676235/140785811-72120c00-94f3-4acc-978b-914264ecd430.png)
2. Go here and follow instructions for Windows: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
3. Run the following command and follow prompts to install Github CLI
```
winget install --id GitHub.cli
```
4. Restart your command prompt
5. Run the following command
```
gh auth login
```
6. Follow prompts, we use Github.com, HTTPS opertions, auth however you want. Google it if you get stuck :)

## TASK-0.2: Install and Configure VS Code
1. Go here https://code.visualstudio.com/download
2. Download and install VS Code
3. Open VS Code
4. Go here https://marketplace.visualstudio.com/items?itemName=ms-python.python
5. Install the Python extension, it will open VS Code, this might take a few seconds

NOTE: If you want to use notebooks, you have two options. One is within VS Code which you can Google how to, or preferably Google Colab. Colab would be great because if you have issues you can send it to me and I can look at the code. Like its name suggests, its more colaboratory. I know Jupyter is great but usually you install that with Anaconda, and it's a whole thing. I strongly suggest not installing Anaconda on your work computer unless we deem it necessary. I just have found it kind of hard to deal with when it comes to package management....Okay fun story, for a project I was working on some deep learning frameworks, I spent 8-10 hours debugging why it wouldn't run and it came down to some environment things with Anaconda. I could have used venv but at that point I was so frustrated I wiped out my entire python environment and started from scratch. So that is why I am anti Anaconda, but pro notebooks. 

## TASK-0.3: Projects Folder
1. It is up to you but I suggest having a projects folder somewhere easy to get to. Like C:\projects. Don't put it deep into a folder structure (Ask or tell me why I would suggest this)
2. For each project you have one folder with everything in it. 

## TASK-0.4: Download this Repo and Make Your Own
1. Go to the main page of the repo
2. Click the code button and choose download zip
3. Unzip that and put it in your projects folder
4. Now we want to create a repo so you each have one. (If you are familiar with github there is a reason we are doing this instead of a fork)
5. On github.com create a new repo (click your profile, go to repos, click new)
6. Name it training_***yourname***, no gitignore, no readme no license
7. Once created run the following command
```
git clone urltoyourrepo
```
8. Copy the contects of the folder we unziped into the new folder created by cloneing the repo. The folders DEMO-0,DEMO-1,etc should be directly in your training_***yourname** folder
9. Navigate to this folder in your command prompt
10. Run the following commands
```
git add .
git commit -m "initial commit"
git push
```
11. Now your repo should look just like this one. You will modify code in your own repo, i.e. coding assigments. 
12. As you progress with updating code, you will want to make sure you keep github updated with your code. To do this, make sure you are in your project directory in the command line and runn the following three commands one after another. At some points you might have to login again. You can update one or more files at a time. I am doing two in this example. Or like above can "git add ." to update all files
```
git add <file1> <file2>
git commit -m "some message about what you are doing"
git push
```
  
## TASK-0.5: Installing Main Python Packages
1. On the command line navigate to the TASK-0 folder.
2. Run the "dir" command, you should see a file named "requirements.txt"
3. Install the packages listed in the requirements.txt file
```
pip install -r requirements.txt
```
4. In the future if you run python code and it says you are missing a package, just open the command line and type "pip install ***package name***"

## TASK-0.6: Download and Install Putty
1. Download and install here: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
  
## TASK-0.7: Jira - IGNORE
1. Jira is going to be something we try to use with project management. I say try because I want to see how it goes. I used it for 3 years at my last job and like it, but they've changed the look on me. 
2. If you haven't gotten an email to setup a Jira account, remind me.
3. Follow the email instructions, you can login here: https://circle-logistics.atlassian.net/
  
## TASK-0.8: Install Chromedriver
1. Goto this link: [https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.35/](https://chromedriver.storage.googleapis.com/index.html?path=102.0.5005.61/)
2. Download the windows version
3. Unzip and run the application


## TASK-0.9: Install MySQL
https://dev.mysql.com/downloads/workbench/

## TASK-0.10: Verify Credentials and setup MFA for AWS
1. Go to: https://circle-logistics.signin.aws.amazon.com/console
2. Login using the credentials I gave you
3. You will need to change your password to something secure
4. In the search bar search for "IAM"
5. Click "My security credentials"
6. You might have to scroll down, but then click "Manage MFA Device"
7. Then follow the prompts to adding a MFA device (your smartphone)
8. You should choose a virtual device. I use Google Authenticator. You can use any supported software, but if you aren't already using one of them, I would use Google Auth
9. Once setup, log out and then back in to verify the MFA works.
10. Whenever you can, I suggest using MFA, either through the google app or texting. I like the apps because I can put the same accounts multiple devices. It is unlikely that you would lose access to your cell number though.

## TASK-0.11: Install 8x8
1. Google how to download 8x8
2. Install 8x8 and verify your credentials work
