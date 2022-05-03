import osmnx as ox #Osmnx takes snippet from google maps, lays out a shortest distance in realworld roads
import networkx as nx #to be able to use the functions for the graph
import warnings #to be able to work with warnings

ox.config(log_console=True, use_cache=True)
from geopy.geocoders import Nominatim
locator = Nominatim(user_agent = "MajorProject")

place     = 'Rhode Island' #location
mode      = 'drive' #transportation mode
optimizer = 'length' #optimization for time

graph = ox.graph_from_place(place, network_type = mode, retain_all=False, truncate_by_edge=True, simplify=False) #graph of layout of Europe

T = input("Enter number of Trucks: ")
totallength = 0

for i in range(int(T)):

  start_location = input("Enter start location: ")
  end_location = input("Enter end location: ")

  start_latlng = locator.geocode(start_location).point
  end_latlng = locator.geocode(end_location).point

  # find the nearest node to the start location
  orig_node = ox.get_nearest_node(graph, start_latlng)

  # find the nearest node to the end location
  dest_node = ox.get_nearest_node(graph, end_latlng)

  Gs = ox.utils_graph.get_largest_component(graph, strongly=True) #choose "strong" main roads

  warnings.filterwarnings("ignore") #ignore warning given (the warning is just a diff way of using"ox.get_nearest_node")

  shortest_route = nx.shortest_path(Gs, orig_node, dest_node, weight=optimizer) #calculate the shortest route from original and final nodes, optimize by time

  shortest_route_map = ox.plot_route_folium(Gs, shortest_route, tiles='Stamen Terrain') #form map from graph, use shortest route, and type map is stamen

  length = nx.shortest_path_length(Gs, orig_node, dest_node, weight='length') #define length in meters

  totallength = totallength + length

print("Total minimum distance traveled: "+str(length*22.1)+" Meters") #length in m

print("Total gas used: "+str((length*0.000621371)/5.49)+" Gallons") #gallons of gas used

shortest_route_map #print graph
