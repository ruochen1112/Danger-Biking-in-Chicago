import folium
from folium.element import IFrame
import geopandas as gpd
import pandas as pd
import fiona
from shapely.geometry import Point
from geopy.geocoders import Nominatim

divvy_data = pd.read_csv('divvy_station.csv')

station_locations = [Point(xy) for xy in zip(divvy_data["FROM LONGITUDE"], divvy_data["FROM LATITUDE"])]
geo_stations = gpd.GeoDataFrame(divvy_data, geometry = station_locations)

geo_stations.crs = fiona.crs.from_epsg(3528)
geo_stations.set_geometry(geo_stations.buffer(0.002), inplace = True)

crimes = pd.read_csv("chicago_crimes.csv", usecols = [5, 19, 20])
crimes.dropna(inplace = True)
crime_locations = [Point(xy) for xy in zip(crimes["Longitude"], crimes["Latitude"])]
geo_crimes = gpd.GeoDataFrame(crimes, geometry = crime_locations)
geo_crimes.crs = fiona.crs.from_epsg(3528)

result = gpd.sjoin(geo_crimes, geo_stations)
result['Counts'] = result.groupby("index_right")["FROM STATION ID"].transform('count')
result = result[["Primary Type","FROM STATION ID", "FROM STATION NAME", "FROM LONGITUDE","FROM LATITUDE", "Counts"]]
result.to_csv('join_data.csv')
result = result[["FROM STATION ID", "FROM STATION NAME", "FROM LONGITUDE","FROM LATITUDE", "Counts"]].drop_duplicates(keep='first')
# create empty map zoomed in on Chicago
Chi_COORDINATES = (41.88, -87.63)
chi_map = folium.Map(location=Chi_COORDINATES, zoom_start=12)
#when zoom out, cluster and sum the number
my_marker_cluster = folium.MarkerCluster().add_to(chi_map)

# add a marker for every station, use a clustered view.
for ix, row in result.iterrows():
	text = "Station Name: " + row['FROM STATION NAME'] + "<br>" + "Station Id: " + str(row['FROM STATION ID']) + "<br>" \
			+ "Crime Count: " + str(row['Counts'])
	popup = folium.Popup(IFrame(text, width=300, height=100))
	folium.Marker(location = [row['FROM LATITUDE'],row['FROM LONGITUDE']], popup=popup).add_to(my_marker_cluster)

chi_map.save('divvy_crime_map.html')