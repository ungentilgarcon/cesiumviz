# -- coding: utf-8 --
# GENERATEUR DE FEATURE COLLECTION
# DE POLYGONES DEPUIS UN POINT GEO
# carré:
# "({1}-{3},{2}+{3})({1}{3},{2}{3})({1}{3},{2}{3})({1}{3},{2}{3})({1}{3},{2}{3})"
# soit:
# ({1}{4}{3},{2}{5}{3})n+1 fois(signe1,signe2)
# n étant le nombre d'arêtes
# et avec {4},{5} ou signe1,signe2 décrivant:
# __
# 01
# 00
# 10
# 11
# 01
# __
# 
# 3 aretes et plus:
#au besoin:*
#({1}+{3}*cos{6},{2}+{3}*sin{6})n+1 fois
# n étant le nombre d'arêtes
# 7 etant égal à cos ou sin
# et avec {4}{5}{6} décrivant:
# {3} = float(row['count'])/width
# {6}=angle
# u = unit
# v = 360
# pas= 360 / n
# {6}= angle = 0
# for i = 0 to n
# {6}=i*pas
# i++ 
# on peut aussi faire la moitie du travail et reintegrer {4}et {5} et se passer alors des nombres premiers...
# 
import json
import os
from geojson import Feature, Point, FeatureCollection, Polygon

'''//ouvrir fichier points de viz, utiliser geojson pour en faire un geojson
import json'''

dataout_file = open('exportbands_all_venues.geojson','a+');
f = open('exportbands_all_venues-1000.json');

data = json.loads(f.read())

f.close()

width = 4	
z = len(data)
print z
y = 0
for row in data:
	
	print row
	print row['count']
	print z
	if row['count'] > 5:
		# TODO: pass if null
		# pour l'instant
		my_poly = Polygon([[(
			row['longitude']-float(row['count'])/width,
		 row['latitude']+float(row['count'])/width),(row['longitude']-float(row['count'])/width,
		  row['latitude']-float(row['count'])/width),(row['longitude']+float(row['count'])/width,
		   row['latitude']-float(row['count'])/width),(row['longitude']+float(row['count'])/width,
		    row['latitude']+float(row['count'])/width),(row['longitude']-float(row['count'])/width,
		     row['latitude']+float(row['count'])/width)]])


		geojs = Feature(geometry=my_poly,properties={"type": "Salle"})		
		# print my_poly
		# print geojs
		if z == 1:
			json.dump(geojs,dataout_file)	
			terminator = "]}"
			dataout_file.write(terminator)
			z -= 1		
		elif y == 0: 
		 	# geocoll = "{'type': 'FeatureCollection', 'features': ["
			dataout_file.write("{\"type\": \"FeatureCollection\", \"features\": [")
		 	json.dump(geojs,dataout_file)
		 	y += 1
		 	z -= 1
		 	print y
		else :
			dataout_file.write(',')
			json.dump(geojs,dataout_file)
			z -= 1
			# json.dump (geojsvirgule,dataout_file)
	else: 
			if z == 1:	
			
				terminator = "]}"
				dataout_file.write(terminator)
				z -= 1		
			else :
				z -= 1
			# json.dump (geojsvirgule,dataout_file)
