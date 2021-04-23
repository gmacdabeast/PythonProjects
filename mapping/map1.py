import folium
import pandas
import io

df = pandas.read_csv('/Users/gmacdabeast/Python/mapping/Volcanoes.txt')
##print(df)

#for loop get the coordinates

lat = list(df['LAT'])
lon = list(df['LON'])
elevation = list(df['ELEV'])

def colorproducer(el):
    if elev >0 and elev <= 2000:
        return 'green'
    elif elev>2000 and elev<=3000:
        return 'orange'
    else:
        return 'red'

#def populationcolors():


#print(lat,lon)
map = folium.Map([38,-99],zoom_start=6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name='Volcanoes')
fg_2 = folium.FeatureGroup(name='Population')

for lt, ln, elev in zip(lat,lon, elevation):
        fg.add_child(folium.CircleMarker(radius = 10, location = [lt,ln], popup = elev,fill = True, fill_opacity=.7, color=colorproducer(elev))) #icon= folium.Icon(colorproducer(elev))))

fg_2.add_child(folium.GeoJson(data=open('/Users/gmacdabeast/Python/mapping/world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'red' if 10000000 <= x['properties']['POP2005'] <20000000 else 'blue'}))
map.add_child(fg)
map.add_child(fg_2)
map.add_child(folium.LayerControl(position='topleft'))


map.save('/Users/gmacdabeast/Python/mapping/Map1.html')