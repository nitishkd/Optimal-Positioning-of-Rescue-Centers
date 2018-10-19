import requests
import json
import math
import numpy as np

API_KEY = "AIzaSyA7YNuS2vMOKSr5mY94GpWk25aZqw3Fmbs";
elevation_url = "https://maps.googleapis.com/maps/api/elevation/json?locations=";

class GoogleMaps():

	def __init__(self):
		print("class Google maps called");

	def GetElevation(self, latitude, longitude):
		request_url = elevation_url + str(latitude) + "," + str(longitude) + "&key=" + API_KEY;
		response = requests.get(request_url);
		result = response.json()
		if(result["status"] == 'OK'):
			return	float(result['results'][0]['elevation'])
	
	def getLatLngFromText(self, query): # it accepts a place name and gets lat,lng and height from it
		api_key = 'AIzaSyDM8Ns40uQHDt6M51vYHIx11ncTSj84VNo'
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
		r = requests.get(url + 'input=' + query + '&inputtype=textquery'+
		                        '&key=' + api_key) 
		x = r.json()
		y = x['results'] 
		for i in range(len(y)): 
		    print(y[i]['geometry']['location']['lat'] , " " , y[i]['geometry']['location']['lng'])

		if(len(y) != 0):
			lat=y[0]['geometry']['location']['lat']
			lng=y[0]['geometry']['location']['lng']
			print lat , lng
			height = self.GetElevation(lat, lng)
		else:
			print "nothing"
		return height


	def makeGrid(self, latitude, longitude, radius):					##make Grid to plot
		dx = radius;
		dy = radius;
		r_earth = 6387; 												##distances are in KM
		partitions = 5;
		a = latitude - (dy / r_earth ) * (180 / math.pi);
		b = longitude - (dx / r_earth ) * (180 / math.pi ) / math.cos(latitude * math.pi / 180);
		c = latitude + (dy / r_earth ) * (180 / math.pi);
		d = longitude + (dx / r_earth ) * (180 / math.pi ) / math.cos(latitude * math.pi / 180);
		
		minLong = max(b,d);
		maxLong = min(b,d);
		minLat = min(a,c);
		maxLat = max(a,c);

		corners = [[minLat, maxLong], [maxLat, maxLong], [maxLat, minLong], [minLat, minLong]];
		rows , cols = partitions, partitions 
		self.GRID = [[0 for x in range(cols)] for y in range(rows)] 
		i, j = 0,0;
		LAT = np.arange(minLat, maxLat, (maxLat-minLat)/rows);
		LON = np.arange(minLong, maxLong, (maxLong-minLong)/cols);

		for latd in LAT:
			j = 0;
			for longd in LON:
				height = self.GetElevation(latd, longd)
				self.GRID[i][j] = height;
				j += 1;
			i += 1;

		print (self.GRID);

if(__name__ == "__main__"):
	obj = GoogleMaps();
	# height = obj.GetElevation(39.7391536, -104.9847034)
	# print (height)

	obj.makeGrid(39.7391536, -104.9847034, 10);