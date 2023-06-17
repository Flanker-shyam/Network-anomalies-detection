import geoip2.database
from geoip2.errors import AddressNotFoundError
import ipaddress

def is_public_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return not ip.is_private
    except ValueError:
        return False


def get_geolocation(dst_ip_address, blackListed):
    reader = geoip2.database.Reader('GeoLite2-City_20230616/GeoLite2-City.mmdb')
    ip_type = ""
    city = ""
    region_code = ""
    country = ""
    latitude = ""
    longitude = ""
    type=""

    is_public = is_public_ip(dst_ip_address)

    if not is_public:
        ip_type = "Private"
    else:
        ip_type = "Public"
    try:
        response = reader.city(dst_ip_address)
        city = response.city.name
        region_code = response.subdivisions.most_specific.iso_code
        country = response.country.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        if dst_ip_address in blackListed:
            type = "Yes"
        else:
            type = "No"
    except AddressNotFoundError:
        city = ""
        region_code = ""
        country = ""
        latitude = ""
        longitude = ""
        type=""
    
    return ip_type,type,city, region_code, country, latitude, longitude