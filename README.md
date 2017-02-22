# Final Project:
Chicago Bike and Crime

### Research Question:
What is the crime count and type around any bike station in Chicago?

### Datasouces:
Divvy data:

https://data.cityofchicago.org/Transportation/Divvy-Trips-Dashboard/u94x-unre

Crime data (all, but filter for post-2013):

https://data.cityofchicago.org/Public-Safety/Crimes-2016/kf95-mnd6

### How the data was cleaned and reduced:

For the divvy data, I selected the latest data from Ferb 1st to July 1st to count the stations. 

From it, I picked three columns "FROM STATION ID","FROM LONGITUDE","FROM LATITUDE", kept every new station while dropped the duplicate stations. 

The result shows that there are 524 stations been used recently. 

Then we transferred this station data into a geo data-frame.

For the crime data, we picked Primary Type, Longitude and Latitude column to make a list of tuple as location points and transferred them into a geo data-frame as we did with divvy data. 

Then we set divvy points radian and join with crime data points, save the intermediate join data as join_data.csv, and used by the website for plot.
 
### For the cleaning scripts, please see project folder:
get_station.py:  get unique station id, name , Longitude and Latitude of the station

get_station_model.py: helper script to generate 524 stations as model input

folium_map.py:  generate join_data.csv file, and map data


### Fully Processed Data, please see project folder:
divvy_station.csv

/mysite/static/myapp/join_data.csv
          

### Django Site, please see project folder-mysite:
Runserver and you can navigate to see instructions, map (crime count), and plot (crime type). Enjoy!!!

