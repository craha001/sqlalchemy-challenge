# sqlalchemy-challenge
For this week's challenge, we will be utilizing SQLAlchemy for us to code in pandas directly from the query. In the SurfsUp resources file, there are two datasets and a SQL file which are essential to completing the task at hand. First dataset known as measurement,  
has a list of dates, stations, precipitation values and temperatures. Second dataset known as stations contains station, name, latitude, longitude, and elevation. Once the jupyter notebook analysis is done which can be found in the climate_starter file, the second part  
is creating an app reflecting the data we found where users can explore the answers obtained which is in file app.py.

## Part 1: Analyze and Explore the Climate Data
Open up the climate_starter.ipynb in Jupyter Notebook. With the two databases loaded into our code as station and measurement two different analysis will be performed. In order to perform our analysis the following is a list of imports required to achieve the desired   output:

%matplotlib inline  
from matplotlib import style  (Used for style)  
style.use('fivethirtyeight')  
import matplotlib.pyplot as plt (Matplotlib import for visualization)  
import numpy as np  (Numpy is imported for calculations)  
import pandas as pd  
import datetime as dt (Imported to convert dates into integers for calculation)  
 
(Python SQL toolkit and Object Relational Mapper)
import sqlalchemy  
from sqlalchemy.ext.automap import automap_base (used to create variables for the datasets from SQL)  
from sqlalchemy.orm import Session  (Imported to create a session where we can query into sql alchemy)  
from sqlalchemy import create_engine, func, inspect (Import used for engine creation, func is imported to perform calculations on the datasets, and inspect is imported to show what columns are found in each dataset)  

### Precipitation Analysis
To perform our precipitation analysis we will look into our data from the most recent date and trace it back a whole year. By performing a session.query command on the measurement.date column to find the most recent date in the dataset we can begin performing the analysis. The graph that will be plotted is date in the x-axis and precipitation in inches for the y-axis. Once the most recent date is acquired, then we can transform this date into an integer using datetime imported as dt, so the code looks like dt.datetime(yyyy,mm,day). With our recent date converted to an integer, we can simply subtract 366 days to cover the entire year we want to visualize and store it in it's own variable as one_year. Finally a query was performed to obtain the dates and precipitation over the last year using our one_year variable as a parameter. Then convert this query into a dataframe using pandas, sort it based on dates in descending order and plot the scatter plot using matplotlib plt.plot. After our visualization, a statistical summary was performed to find the counts, min, max, mean, standard deviation, 25% quantile, 50% quantile, and 75% quantile. 

### Station Analysis
In the station analysis we will be using Pandas and SQL alchemy to find the most active station and create a histogram for temperature values and their frequency meaning how often said values were calculated. Step one is using a query to output a list of our stations to see how many are in the dataset. Next, using similar code we can find the most active station by query their names and ordering them by counts in descending order putting the most active station at the top of our list. The most active station is determined by how many times it occurs within the dataset. Then we will reuse the code from our precipitation analysis to calculate the most recent date and subtract by 366 days to cover data for the last year. With this information we can filter the qeury by the most active station and the date for the whole year and create a list for temperatures and their frequencies. With matplotlib we can now create a histogram to compare temperature values to how often they occurred for the specified station.


## Part 2: Design Our Climate App
In order to accomplish our task, we created a Flask API based on the queries developed from our climate_start.ipynb file. The code for this can be found in the app.py file. 

### Step 1: Import Dependencies

import numpy as np  
import sqlalchemy  
from sqlalchemy.ext.automap import automap_base  
from sqlalchemy.orm import Session  
from sqlalchemy import create_engine, func  
from flask import Flask, jsonify  
import datetime as dt  

### Step 2: Database Set Up
We created our engine using the same code found in climate_starter. Once this was completed we have variables for our station and measurement databases. Once the session was created, next step is to begin our app setup.

### Step 3: Flask Routes
The following is a list of routes and their desired outcomes:

@app.route("/") - Our homepage where all the api routes will be listed for the user of the code.

@app.route("/api/v1.0/precipitation") - Here the results from our precipitation analysis can be found. Our goal for this route is to create a jsonifyed list for the dates and their precipitation values in inches. We used the one year calculated from most recent date.

@app.route("/api/v1.0/station") - This route simply outputs the list of stations in our datasets.

@app.route("/api/v1.0/tobs") - Here the results of our station analysis can be found where the values for the most active station's temperatures for the one year of data calculated. 

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>") - For these two routes, the user of the app can find a list of minimum temperature, average temperature, and maximum temperature for a specified start or start-end range. 
To use this api route an example would be: /api/v1.0/2016-08-23 or /api/v1.0/2016-08-23/2017-08-23.



