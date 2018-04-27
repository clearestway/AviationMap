import csv, json
from geojson import Feature, FeatureCollection, Point
import pandas as pd

test = pd.read_csv('templates/metar_data.csv',sep=',',header=5)
test = test[['station_id','latitude','longitude','raw_text']]
test.to_csv('new_metar_data.csv')

features = []
with open('new_metar_data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i in reader:

        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'Station Id': station_id,
                    'text': raw_text
                }
            )
        )

collection = FeatureCollection(features)
with open("METAR.json", "w") as f:
    f.write('%s' % collection)