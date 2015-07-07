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
		my_poly = Polygon([[(
			row['longitude']-float(row['count'])/1000,
		 row['latitude']+float(row['count'])/1000),(row['longitude']-float(row['count'])/1000,
		  row['latitude']-float(row['count'])/1000),(row['longitude']+float(row['count'])/1000,
		   row['latitude']-float(row['count'])/1000),(row['longitude']+float(row['count'])/1000,
		    row['latitude']+float(row['count'])/1000),(row['longitude']-float(row['count'])/1000,
		     row['latitude']+float(row['count'])/1000)]])

# GENENRATEUR DE POLYGONES DEPUIS UN POINT GEO
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
# 3,5, et plus:
#au besoin:
#({1}+{3}*cos{6},{2}+{3}*sin{6})n+1 fois
# n étant le nombre d'arêtes
# 7 etant égal à cos ou sin
# et avec {4}{5}{6} décrivant:
# {3} = float(row['count'])/1000
# {6}=angle
# u = unit
# v = 360
# pas= 360 / n
# {6}= angle = 0
# for i = 0 to n
# {6}=i*pas
# i++ 
# on peut aussifaire la moitie du travail et reintegrer {4}et {5} et se passer alors des nombres premiers
# 

		geojs = Feature(geometry=my_poly,properties={"type": "Salle"})		
		print my_poly
		print geojs
		geocoll = FeatureCollection([geojs])

		json.dump (geocoll,dataout_file)



liste_de_polygones = dict()
