# Geolocation rendering using google api 
## Description
   This application generates the heat map based on the json files from data processing of the strava health data. The main json file is filtered into sectors for ease of rendering . The sectors are dynamically added to the seletion menu for loading the heat map of that sector . 

   * The google map api uses following features
      1.  Bicycle routes
      1. Zooming with selection
      1. Heat map toggle and color coding
      
## How to set on a server 
    * start the httop server using :
         python -m SimpleHTTPServer 8000
    * view the rendering using firefox or other browser supporting jquery at 8000 port as follow
    *   use the web address: localhost:8000 or server_public_IP:8000

