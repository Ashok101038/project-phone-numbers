import phonenumbers
import folium

from mynumber import number
from phonenumbers import geocoder
key= '3527436c438b47d8b1e7df886986183d'
samnumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(samnumber, "en")
print(yourlocation)

# get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder= OpenCageGeocode(key)

query = str(yourlocation)

results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)

folium.Marker([lat,lng],popup =yourlocation).add_to((myMap))

# save map in html file
myMap.save("mylocation.html")