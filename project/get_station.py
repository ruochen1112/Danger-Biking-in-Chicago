import pandas as pd

divvy_data = pd.read_csv('Divvy_Trips.csv')
divvy_data.dropna(inplace = True)
stations = divvy_data[["FROM STATION ID", "FROM STATION NAME", "FROM LONGITUDE","FROM LATITUDE"]].drop_duplicates(keep='first')
stations.to_csv('divvy_station.csv')
