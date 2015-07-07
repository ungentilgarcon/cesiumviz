# -- coding: utf-8 --
import json
import os
from geojson import Feature, Point, FeatureCollection, Polygon

'''//ouvrir fichier points de viz, utiliser geojson pour en faire un geojson
import json'''

with open('exportbands_all_venues-1000.geojson','a+') as dataout_file:
	f = open('exportbands_all_venues-1000.json');

	data = json.loads(f.read())

	f.close()

	for row in data:
		my_poly = Polygon([[(row['longitude']-float(row['count'])/1000,
		 row['latitude']+float(row['count'])/1000),(row['longitude']-float(row['count'])/1000,
		  row['latitude']-float(row['count'])/1000),(row['longitude']+float(row['count'])/1000,
		   row['latitude']-float(row['count'])/1000),(row['longitude']+float(row['count'])/1000,
		    row['latitude']+float(row['count'])/1000),(row['longitude']-float(row['count'])/1000,
		     row['latitude']+float(row['count'])/1000)]])
		geojs = Feature(geometry=my_poly,properties={"type": "Salle"})		
		print my_poly
		print geojs
		geocoll = FeatureCollection([geojs])

		json.dump (geocoll,dataout_file)