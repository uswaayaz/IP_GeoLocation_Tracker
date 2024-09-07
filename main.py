import folium
import requests
from geopy.geocoders import Nominatim

 
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()['ip']

 
def get_geolocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/geo')
    data = response.json()
    location = data['loc'].split(',')
    latitude = float(location[0])
    longitude = float(location[1])
    return latitude, longitude, data['city'], data['region'], data['country'] 
 
def display_map(latitude, longitude):
    map_ = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup="User Location").add_to(map_)
    return map_

if __name__ == "__main__":
    ip = get_ip()
    latitude, longitude, city, region, country = get_geolocation(ip)
    
    print(f"IP Address: {ip}")
     
    print(f"Location: {city}, {region}, {country}")
    print(f"Coordinates: Latitude {latitude}, Longitude {longitude}")
    
 
    map_ = display_map(latitude, longitude)
    
    
    map_.save("user_location_map.html")
    
    print("Map has been saved as user_location_map.html")
