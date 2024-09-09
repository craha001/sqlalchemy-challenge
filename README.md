# sqlalchemy-challenge
For this week's challenge, we will be utilizing SQLAlchemy for us to code in pandas directly from the query. In the SurfsUp resources file, there are two datasets and a SQL file which are essential to completing the task at hand. First dataset known as measurement,  
has a list of dates, stations, precipitation values and temperatures. Second dataset known as stations contains station, name, latitude, longitude, and elevation. Once the jupyter notebook analysis is done which can be found in the climate_starter file, the second part  
is creating an app reflecting the data we found where users can explore the answers obtained which is in file app.py.

##Part 1: Analyze and Explore the Climate Data
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

###Precipitation Analysis
First will be precipitation analysis where we will cover data from the most recent date and trace it back a whole year. By performing a session.query command on the measurement.date column to find the most recent date in the dataset  
we can begin performing the analysis. The graph that will be plotted is date in the x-axis and precipitation in inches for the y-axis. Once the most recent date is acquired, then we can transform this date into an integer using  
datetime imported as dt, so the code looks like dt.datetime(yyyy,mm,day). With our recent date converted to an integer, we can simply subtract 366 days to cover the entire year we want to visualize and store it in it's own variable  
as one_year. Finally a query was performed to obtain the dates and precipitation over the last year using our one_year variable as a parameter. Then convert this query into a dataframe using pandas, sort it based on dates in descending  
order and plot the scatter plot using matplotlib plt.plot. After our visualization, a statistical summary was performed to find the counts, min, max, mean, standard deviation, 25% quantile, 50% quantile, and 75% quantile. 




###Station Analysis
Second will be a station analysis where using Pandas and SQL alchemy we will find the most active station and create a histogram for temperature values and their frequency meaning how often said values were calculated. 
