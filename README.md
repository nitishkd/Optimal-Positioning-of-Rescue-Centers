# Optimal-Positioning-of-Rescue-And-Resource-Centers

## Optimal Positioning of Rescue Centers in a Natural Disaster occurred.

We are trying to build a solution for Positioning of Rescue Centers in a Natural Disaster event and guiding the refugees to the Rescue Centers.

Observing the previous few trends of Natural Disaster and their effect on human lives. One thing is that the number of Natural Disaster has not reduced but the casualty in those unfortunate accidents has been significantly reduced. We think this huge difference is because of the improvement in the Rescue services. 

However, there is a lot of scope for improvement. The recent flood in Kerala led us to believe that this can be improved significantly. If we can set up rescue camp such that its position is both optimal and feasible. For that, we want to analyze the live data consisting of the position of peoples will be received via text. We will then use this data instead of the census data.

Thus we can select much better positions for the rescue centers. Analyzing this with the geographical data we will provide the list of feasible points where we can set up our camp. Such that the resource used can be minimized. This will significantly reduce the setup time for the rescue camps. On the other side provide full communication to the user like guiding them to the rescue center and letting them know whether they have to reach the Rescue center themselves or the help will reach them.


## How does it work?

Data of users will be collected from the users who are stuck somewhere in some natural disaster or need any supplies or shelter for survival.

Problem is to identify the candidate locations of establishing rescue and shelter homes such that people are able to safely travel to those places and get the shelter while natural disaster occurred. Such shelter homes could be home to many civilians during the crisis of natural or man-made disasters(like a radio-active disaster).

Refugees could interact with the project in two ways.

1) Users, who have the application can share their location with the application server via a text message which will contain their geo-location. This will not require any type of internet connection which is generally not available during such events.

2) Users who do not have phones with GPS could share a near landmark where they can reach, thus giving their approximate location.

This location will be used to plot the cluster of people who are together and their count. This will help to make a refugee camp nearby to them such that their safety in transit is maximized and cost of refugees reaching there and cost of establishing those refugee camps is minimized.

## How users can get started with the project?

Users can access the application on their smartphone device. The important features provided by the application works in offline mode, So there is no requirement of internet connectivity which won’t be available during a disaster. 

The user sends his/her location in the language of his/her choice in the form of text message. This text will be processed by the server to update the user about nearest rescue camp. This information will also be shared with the person registered as “the person to be contacted in case of emergency”. This will ensure that the family of the person is updated about the camp where they can look for the victim. 

There will be a section in the application where the user can get information about the steps to be followed in case of occurrence of some general natural disasters.

## Used Datasets

1) Live data is generated in form of geo-location and location address.
2) Google Maps for identifying the terrain.


## Technologies Using

1) Python
2) Kotlin/Java
