CREATE TABLE weather (
    city            varchar(80),
    date            date,
    temp_lo         int,           -- low temperature
    temp_hi         int,           -- high temperature
    temp            int,           -- Current Temperature
    prcp            real,          -- precipitation
    pressure        varchar(80),
    wind            varchar(80),
    snow            varchar(80),
    rain            varchar(80),
    sunrise_time    varchar(20),
    sunset_time     varchar(20),
    status          varchar(100),
    weather_cd      int,
    visibility_distance float,
    dewpoint            float,
    humidity            int

);