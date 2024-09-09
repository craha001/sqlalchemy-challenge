# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"  # tmin, tmax, tavg for specified start date
    )


# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data)  to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(bind=engine)

    # Most recent date
    first_measurement = dt.datetime(2017, 8, 23)

    # Calculate the date one year from the last date in data set.
    one_year = first_measurement - dt.timedelta(days=366)

    measurement_data = session.query(
        measurement.date, measurement.prcp
    ).filter(measurement.date >= one_year).all()

    # Precipitation dictionary
    precipitation_dict = {date: prcp for date, prcp in measurement_data}

    session.close()

    return jsonify(precipitation_dict)


@app.route("/api/v1.0/station")
def station():
    session = Session(bind=engine)
    #Return a JSON list of stations from the dataset.
    stations_list_names = session.query(
        measurement.station
    ).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()

    # Extracting the station names from the query result
    station_names = [station[0] for station in stations_list_names]

    session.close()
    return jsonify(station_names)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(bind=engine)
    #Query the dates and temperature observations of the most-active station for the previous year of data.
    #Return a JSON list of temperature observations for the previous year.

    most_active_station = session.query(
        measurement.station,
        func.min(measurement.tobs),
        func.max(measurement.tobs),
        func.avg(measurement.tobs)
    ).group_by(measurement.station).order_by(func.count(measurement.station).desc()).first()

    if most_active_station:
        most_active_station_id = most_active_station[0]  # Extract the station ID

        # Calculate the date 12 months ago from most recent
        # Most recent date
        first_measurement = dt.datetime(2017, 8, 23)

        # Calculate the date one year from the last date in data set.
        one_year_ago = first_measurement - dt.timedelta(days=366)

        temperature_data = session.query(
            measurement.date, measurement.tobs
        ).filter(
            measurement.station == most_active_station_id,
            measurement.date >= one_year_ago
        ).all()

        # Extract the temperature values for plotting
        temperatures = [temp.tobs for temp in temperature_data]

        session.close()
        return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_range(start, end=None):
    # Create our session (link) from Python to the DB
    session = Session(bind=engine)

    if end:
        # If both start and end dates are provided, example:  /api/v1.0/2016-08-23/2016-10-23
        results = session.query(
            func.min(measurement.tobs),
            func.avg(measurement.tobs),
            func.max(measurement.tobs)
        ).filter(measurement.date >= start).filter(measurement.date <= end).all()
    else:
        # If only the start date is provided example:  /api/v1.0/2016-08-23/
        results = session.query(
            func.min(measurement.tobs),
            func.avg(measurement.tobs),
            func.max(measurement.tobs)
        ).filter(measurement.date >= start).all()

    # Close the session
    session.close()

    # Extract the result and structure the response
    temp_data = {
        "TMIN": results[0][0], #lowest temperate from specific day
        "TAVG": results[0][1], #average temperature from specific day
        "TMAX": results[0][2]  #highest temperature from specific day
    }

    return jsonify(temp_data)

if __name__ == '__main__':
    app.run(debug=True)






