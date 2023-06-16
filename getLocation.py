import geoip2.database
from geoip2.errors import AddressNotFoundError

def get_geolocation(src_ip_address,dst_ip_address, blackListed):
    reader = geoip2.database.Reader('GeoLite2-City_20230616/GeoLite2-City.mmdb')
    try:
        response = reader.city(src_ip_address)
        city = response.city.name
        region_code = response.subdivisions.most_specific.iso_code
        country = response.country.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        type =""

        if src_ip_address in blackListed:
            type = "source"
        elif dst_ip_address in blackListed:
            type = "destination"
    except AddressNotFoundError:
        city = ""
        region_code = ""
        country = ""
        latitude = ""
        longitude = ""
        type=""
    
    return city, region_code, country, latitude, longitude,type