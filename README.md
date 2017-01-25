# google-location-geojson.py
Python script converts your Google location data to GeoJSON format.  Great fun if you have or had an Android phone with GPS enabled! 

This script requires the geojson library to function.  Running "pip install geojson" should take care of the dependency.

Usage: Download your personal location history from https://takeout.google.com/settings/takeout and extract the JSON file into the same folder as this script.  Change the filename in your file system or the path in the script if necessary.
Execute by running  "python google-location-geojson.py" and look for the output file google_points.geojson when it is done.

The script takes care of converting the latitude and longitude to the correct format as well as putting timestamps into human-readable form.  Once your location data is in GeoJSON you can use it a lot more easily for things like plotting on a map.  Desktop tools like QGIS, and for the web, the Leaflet mapping library play well with GeoJSON.  For an example of the latter check out https://github.com/rtbigdata/my-google-locations
