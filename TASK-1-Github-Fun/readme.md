# TASK 1: Github-Fun

![image](https://user-images.githubusercontent.com/91676235/141353916-cf49d199-ade8-4ced-97d0-e93015fac5d3.png)

## TASK 1.1: Very Important Tasks
1. Star this repo
2. Find and add a picture to your profile. Let's have fun with github profiles, no picture of yourself. Only a picture of an animal. It could be your pet, your spirit animal or anything. Real picture or animated. If any one wonders why you are googling animal pictures, I have your back :) 

## TASK 1.2: Create repo from github.com and clone
1. Click your profile picture in the top right of github.com and select "Your Repositories"
2. Then click the green "New" button
3. Set the name of the repository to something random (Github even gives you an idea), we are deleting this anyways
4. Set it to Private (we are not doing any open source work here)
5. It is usually good to also add a readme and a gitignore so do that. In the gitignore choose python from the dropdown No need for a license, it's not open source after all
6. Then click create repository
7. Open a command prompt
8. Type the following command:
```
git clone <the url to your repo you just made>
```
9. There might be some authentication, just follow the directions.

## TASK 1.3: Pushing/Pulling changes
1. Find the folder of the repo you just cloned in your file explorer
2. Right click and add text file
3. Name the textfile what you want and open it
4. Type in anything save and close it
5. Back in the command prompt enter the following commands
```
git add <new file you created>
git commit -m "some message you want to say about the commit"
git push
```
6. Go back to your repo on github.com and refresh if needed to see your file
7. Open your file on your computer and open and change the file you created and your readme file
8. Run the following commands, you can update multiple files by listing them, or if you want to update the whole repo just use "."
```
git add .
git commit -m "some message you want to say about the commit"
git push
```
9. From the main repo page, click one of the files you updated
10. Then click the History button
11. Then click one of the changes
12. Github tracks your changes
13. Now from github.com edit one of the files, commit it. Now the online repo is a change ahead of your computer
14. In the command line run the following command:
```
git pull
```
15. Check to see that your local file is updated.
16. Delete the folder on your computer
17. Click the repo settings button
18. Scroll to the bottom and delete the repository  

## TASK 1.4: Issues
I am not sure if/how we will use this feature, but just for your personal enrichment it is good to understand how helpful issues can be, especially on open source projects.
1. Find an issue within this repo. They are numerous. Mostly based on formatting, but I am sure there are spellign 3rrorrs someWere. Or maybe the steps are incomplete.
2. Go to the issues tab and create a new issue. 
3. Be descriptive of the issue, include a link to the file. then explain what changes you would like to see. You can link to the exact section of readmes as seen below.
![image](https://user-images.githubusercontent.com/91676235/141494448-5ae0168f-17a4-4dd7-b8a9-8413859b3bd1.png)
4. You can include the links and also just copy and paste screenshots. Look at the closed issues if you want to see an example. You can get to them from the issues tab.
5. Submit the issue (just do one, we need to keep errors for the next part).
6. We will go over how things work from my side.


## TASK 1.5: Fork 

1. Go to the main page of this repo and click fork 
2. Follow the prompts, you should now have a copy of the repo on your own account and not in the organization
3. You will now be able to edit on this version of the code
4. I should have given you a task, if not come ask me
5. Once you think you have accomplished said task and made the changes go back to the main repo page
6. Click pull requests and then new pull request
7. Click compare across forks
8. On the right drop down select your fork
9. Click create pull request
10. Give some notes on what you did
11. Click create pull request
12. I should get an email, but tell me that you have done so
13. We will go over how things work from my side.

