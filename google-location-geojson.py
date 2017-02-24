#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from time import localtime, strftime
from geojson import Feature, Point, FeatureCollection

# your location data file from Google here
jsonFile = 'LocationHistory.json'

with open(jsonFile, 'r') as f:
  data = json.load(f)

features = []

for obj in data:
  for item in enumerate(data[obj]):
    timestamp = strftime("%Y%-m-%dT%H:%M:%S", localtime(float(item[1]['timestampMs']) / 1000))
    latitude = item[1]['latitudeE7'] / 1E7
    longitude = item[1]['longitudeE7'] / 1E7
    coordinates = Point((longitude, latitude))
    feature = Feature(geometry=coordinates, properties={"accuracy": item[1]['accuracy'], "timestamp": timestamp})
    features.append(feature)

geojson_object = FeatureCollection(features)

outfile = "google_points.geojson"
with open(outfile, 'w') as outfile:
  json.dump(geojson_object, outfile)


