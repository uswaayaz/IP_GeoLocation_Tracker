# IP_GeoLocation_Tracker

To create a script in Python that fetches a user's geolocation using their IP address and displays it on a map, you'll need to use a few libraries:

requests - To make HTTP requests to an API that provides geolocation data based on the IP address.
geopy or ipinfo - For fetching geolocation data.
folium - To display the geolocation on a map.

How It Works:
Get IP Address: The script uses the requests library to fetch the user's public IP address.
Get Geolocation Data: It uses the IP address to fetch geolocation data, which includes latitude, longitude, city, region, and country.
Display Map: The script uses folium to create a map centered on the fetched latitude and longitude, with a marker indicating the user's location.
Output: The map is saved as an HTML file (user_location_map.html), which can be opened in a web browser.
Running the Script
Run the script using Python. The map will be saved as an HTML file, which you can open in your web browser to see the user's location.

 
