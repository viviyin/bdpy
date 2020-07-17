import pandas as pd
import folium

sample_data = pd.read_csv('data/demo101_utf8.csv', sep=',')
print(sample_data.shape)
print(sample_data.columns)

sample_data.columns = ['section', 'road', 'road_detail', 'lon', 'lat', 'extra']
print(sample_data.columns)
# mkdir map

center_point = [25.086496, 121.520864]
zoom = 15
map_osm = folium.Map(location=center_point, zoom_start=zoom)

for i in range(len(sample_data)):
    coord = [sample_data.iloc[i, 4], sample_data.iloc[i, 3]]
    print(f"[{i}]{coord}")
    message = "(%d)[%s]%s" % (i, sample_data.iloc[i, 1], sample_data.iloc[i, 2])
    icon1 = folium.Icon(color='red', icon='info-sign')
    folium.Marker(coord, icon=icon1, popup=message).add_to(map_osm)

ucom = [25.052026, 121.543911]
folium.CircleMarker(ucom, radius=200, popup='ucom taipei',
                    fill_color='#C0FFEE').add_to(map_osm)

giant = [25.042763, 121.559932]
folium.Circle(giant, radius=200, popup='giant egg',
              fill_color='#FFC0EE').add_to(map_osm)
map_osm.save('map\\demo101.html')
