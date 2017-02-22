import pandas as pd

divvy_data = pd.read_csv('divvy_station.csv')
for ix, row in divvy_data.iterrows():
	text = "(\'" + str(row['FROM STATION ID']) + "\', \'" + row['FROM STATION NAME'] + "\'),"
	print(text)
