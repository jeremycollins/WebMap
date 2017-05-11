import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map=folium.Map(location=[45.372,-121.697], zoom_start=4, tiles="Stamen Terrain")

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
    map.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(icon_color="red")))

map.save(outfile="map.html")

