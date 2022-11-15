# TASK-8: Automation Training With Selenium

![image](https://user-images.githubusercontent.com/91676235/141536446-950f0dc8-d0ae-49df-98dc-2e9007c2c8aa.png)

I have given you a small framework to work within. Everytime there is an error, it will put a screenshot in the error_screenshots folder. This should help a bit with debugging.

Link to site we are automating:
https://phptravels.com/demo

## Project 1: Navigating Pages
1. This project uses the navigator.py and navigator_runner.py
2. Using the site above, and the starter code, make a bot that navigates to the pricing page
3. Click every check mark shown in the image below
![image](https://user-images.githubusercontent.com/91676235/140827173-4a461cdb-cbbf-4ee5-a844-af79229bb91b.png)
3. Click buy now
4. Type in the following details   
First Name: John  
Last Name: Doe  
Business Name: Widgets Inc.  
Email: john.doe@widgets.com  
Mobile: 555-555-5555  
5. Then click "I'm not a robot". HINT: It might say the checkbox can't be found. I promise its there, you just need to figure out how to get to it.

![image](https://user-images.githubusercontent.com/91676235/140827012-0447c470-9d8f-4c31-89a9-a47cac048fa6.png)

## Project 2: Scrape Some Data
1. This project uses the scraper.py and scraper_runner.py files
2. Use the site above and the starter code, to make a bot that goes to the suppliers page under the product menu item (you need to have the bot navigate this, don't just travel strait to the suppliers list, that would be cheating :) 
3. Extract every supplier name on the page and then the category they belong to. In this case it is attraction
![image](https://user-images.githubusercontent.com/91676235/140826838-64d7db64-08db-4d40-9785-ffd99b3e311a.png)
3. Save this in a pandas dataframe
4. Export to csv
