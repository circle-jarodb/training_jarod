# TASK-4: Pandas, Numpy, and Math

![image](https://user-images.githubusercontent.com/91676235/140940262-3bb84140-a458-495b-86cb-62a14b752308.png)
![image](https://user-images.githubusercontent.com/91676235/140940530-b802ad80-303c-4da6-85a7-bd434ecf3739.png)

## Question 1
Using the iris dataset that is already imported via the sample code. Create a pandas df that groups all flower measurements by the species and reports the median values. Save that to csv.

## Question 2
1. Import bid_data.csv
2. Remove all rows with nothing in them in the BID_STATUS column
3. Remove rows that are duplicates in the AUCTION_ID column
4. Handle missing data in all columns. Provide reasoning. I will give you descriptions of the columns, but if you need background, ask me.
5. Export clean data to bid_data_yourname.csv

| Table Name           | Description                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| A_ACCOUNT            | The account/shippers name                                                                                                   |
| AUCTION_ID           | Unique identifier for the load provided by shipper                                                                          |
| A_MODE_TYPE          | Ignore                                                                                                                      |
| A_AUCTION_TYPE       | Ignore                                                                                                                      |
| AUCTION_STATUS       | Says if the Auction is still running or closed                                                                              |
| BIDDER               | This is the account I am using to scrape the data                                                                           |
| DATE_BID             | The is the date the bid was placed                                                                                          |
| BEST_BID             | Autozone doesn’t use this, but it is the best bid they have                                                                 |
| NEXT_BID             | Again not used but if it is, it is the max bid allowed by the shipper. So   you have to beat the best bid so far or not bid |
| BID_STATUS           | Our actual bid                                                                                                              |
| TIME_LEFT            | Time left in the auction                                                                                                    |
| A_OPEN_DT            | When the Auction Started                                                                                                    |
| A_HAZMAT             | Does the Load have hazmat cargo                                                                                             |
| A_TANKER_ENDORSEMENT | Do they need a tanker endorsement (for carrying liquids and such)                                                           |
| A_ORIGIN_LOC_NAME    | Location of where you are shipping from. This is like the first line in   an address                                        |
| A_ORIGIN             | Origin city and state                                                                                                       |
| A_PICKUP_DT          | Pickup Date                                                                                                                 |
| A_DEST_LOC_NAME      | Location of where you are shipping to. This is like the first line in an   address                                          |
| A_DEST               | Destination city and state                                                                                                  |
| A_DELIVERY_DT        | Date it needs to be delivered by (sometimes you can get there earlier)                                                      |
| A_STOPS              | How many intermediary stops there are                                                                                       |
| loc_0                | The following 10 columns are the location and time of where the stops   need to be.                                         |
| appt_0               | We limit it to 5 stops, so if there are more then they aren't counted                                                       |
| loc_1                | I am not 100% sure, but I highly doubt we would see more than 3 ever                                                        |
| appt_1               |                                                                                                                             |
| loc_2                |                                                                                                                             |
| appt_2               |                                                                                                                             |
| loc_3                |                                                                                                                             |
| appt_3               |                                                                                                                             |
| loc_4                |                                                                                                                             |
| appt_4               |                                                                                                                             |
| A_EQ_TYPE            | Type of truck needed                                                                                                        |
| A_DISTANCE           | Distance of the trip calculated by the shipper, who knows how                                                               |
| A_WEIGHT             | Weight of cargo                                                                                                             | 

## Question 3: Part 1
Load in the dataset, codys_cat_data.csv. This is some data recorded about each of my four cats. I need you to do some analysis for me.  
I would like some summary statistics of these four cats measurements. Knowing that, you might want to manipulate the data, but you do not have to.  

Please find:  
-Mean and Variance of Each Cat's tail length and weight

Variance equation:  
![image](https://user-images.githubusercontent.com/91676235/140966196-05b46c09-3e58-44b3-80ca-b5b89b007cef.png)

## Question 3: Part 2
1. Load in the dataset from part 3. Create a program that finds the regression line for each of the four sets. We are assuming that weight is dependent on tail length and want to make a model to predict it. Use least squares regression to find a and b where y = ax + b and:    
![image](https://user-images.githubusercontent.com/91676235/140944645-f9cc5f38-f646-409f-8240-6d4c0ab7725f.png)  
You may use functions that do sum and means for you, but no functions that do the least squares for you. 

2. Find the correlation of each cats measurments (i.e. r^2) where:  
![image](https://user-images.githubusercontent.com/91676235/141536971-68882459-f3ba-4589-8df2-ffb0638378ec.png)
Again do not use any functions to do this for you other than mean or sum

## Question 3: Part 3
1. Using the linear equation you found for each cat, create a function that given the cat and tail length, would output a prediction for weight.
2. Use the previous function to create a prediction for a tail length of 1 to 20 at intervals of 0.1
3. Use seaborn to plot a scatter plot of the values, and then your regression line for all 4 cats. DO NOT USE seaborn regplot
4. Okay, now use seaborn regplot :) and compare

![image](https://user-images.githubusercontent.com/91676235/140948302-343dd84b-f96b-4cab-b658-ad52064dfbd7.png)

