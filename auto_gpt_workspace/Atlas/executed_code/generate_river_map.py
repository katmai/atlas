#!/usr/bin/env python3

import sys

# Add the correct path to the 'arcgis' module to the system path
sys.path.append('/usr/local/lib/python3.9/site-packages')

from arcgis.gis import GIS
from arcgis.mapping import WebMap

# Connect to ArcGIS Online
gis = GIS("https://www.arcgis.com", "username", "password")

# Create a new web map
web_map = WebMap()

# Add a feature layer to the map
web_map.add_layer({"type": "FeatureLayer", "url": "https://services.arcgis.com/V6ZHFr6zdgNZuVG0/arcgis/rest/services/USA_Rivers_and_Streams/FeatureServer/0"})

# Save the web map
web_map.save(item_properties={"title": "River Map", "snippet": "A map of rivers in the USA"})