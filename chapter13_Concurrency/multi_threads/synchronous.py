import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()

PLACES = (
    'shanghai', 'beijing', 'yuncheng'
)

def fetch_place(place):
    location = geolocator.geocode(place)
    print(location.address)
    print((location.latitude, location.longitude))

def main():
    for place in PLACES:
        fetch_place(place)

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print(elapsed)
