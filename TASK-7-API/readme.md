# TASK-7: Fun with APIs

![image](https://user-images.githubusercontent.com/91676235/141155308-e2ffea5f-f4a1-49b1-8dd1-e8b41fcc1162.png)

## For all questions using randomness, make sure that you do not reuse the same item

### Question 1
Using the USA population data, pull the populations for the latest avaliable year. Choose 5 states at random, and then graph the populations.

### Question 2
Using the endpoint example below, create a program that creates 10 random IPs, gets the city and region. Then dumps the IP, city, region, and country to a csv file. If the IP is a "bogon" then do not include that and try another. https://ipinfo.io/161.185.160.93/geo

### Question 3
Using the example endpoint below, store all the information it returns in the 'place' key in a csv file for 10 zips randomly chosen from the text file "zips.txt". You will need to handle when the api returns an empty response. Do not count that as one of your 10.
HINT: zips with leading zeros need their lead zeros kept. This is a problem with dealing with zips almost everytime. Numpy makes this really easy. 
https://api.zippopotam.us/us/33162

### Question 4
Get the ratecast data from each of the lanes in lanes.csv. (See demo for starter code)
Store the following in a csv file:  
-Origin  
-Destination  
-Per mile forecast, high, and low  
-Use distance form the API response to get a total cost of the trip  

### Question 5
Find a free api that interests you and come up with something to do with it. What you do with it doesn't have to make a ton of sense, it is just more practice working with API requests and JSON
