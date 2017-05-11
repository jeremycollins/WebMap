import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[45.372,-121.697], zoom_start=4, tiles="Stamen Terrain")

def color(elev):
    if elev in range(0,1000):
        col = "green"
    elif elev in range(1000,3000):
        col = "orange"
    else:
        col = "red"
    return col

for lat, lon, name, elev in zip(df["LAT"],df["LON"],df["NAME"],df["ELEV"]):
    map.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(icon_color=color(elev))))

map.save(outfile="map.html")

