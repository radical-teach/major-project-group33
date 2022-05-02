# major-project-group33

This program takes a total number of trucks/routes that the user wants to find the total distance traveled and the total gallons of gas used. 
The general area has to be set at first in the actual code, weahter it is a state, a country, or a terrirtory for the routes.

Packages needed to download to run the code on a linux machine (Syntax using pip):
**make sure the location of the code file is the same place where terminal is being operated in.
Using pip you will need to download the latest version of python, osmnx, geopy, sickit-learn, and folium. 
We used nano as our compiler of choice to write and read the code files. 

**The code might take a long time to run depending on the ram of the memory

python3 -m pip install osmnx 

python3 -m pip install geopy

python3 -m pip install scikit-learn

python3 -m pip install folium

To write: nano example.py

copy code from sprint1.py (or sprint2.py)

save and exit (cntrl+o, enter, cntrl+x)

To read: python3 example.py

**Example would be sprint1 or sprint2


The program will run and load up a map of the area, in this case it is New Jersey, then it will ask the user for the number of 
trucks/routes that are needed. After that it will ask the user to enter a starting location and an ending location for each route,
they must be cities with in the area written, and in this case it is NJ. 

The program will output the total distance of all of the routes in meters and the total amount of gallons of gas used.
