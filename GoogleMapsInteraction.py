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


if(__name__ == "__main__"):

	obj = GoogleMaps();
	height = obj.GetElevation(39.7391536, -104.9847034)
	print (height)