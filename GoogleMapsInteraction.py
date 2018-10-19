import requests
import json

API_KEY = "AIzaSyA7YNuS2vMOKSr5mY94GpWk25aZqw3Fmbs";
elevation_url = "https://maps.googleapis.com/maps/api/elevation/json?locations=";

class GoogleMaps():

	def __init__(self):
		print("class Google maps called");

	def GetElevation(self, latitude, longitude):
		request_url = elevation_url + str(latitude) + "," + str(longitude) + "&key=" + API_KEY;
		response = requests.get(request_url);
		# print(response.json())
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


if(__name__ == "__main__"):
	obj = GoogleMaps();
	height = obj.GetElevation(39.7391536, -104.9847034)
	print (height)
