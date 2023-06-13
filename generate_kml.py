import pygeoip

def generateKml(ipaddress,dataPath,blackListedIp):
    geo = pygeoip.GeoIP(dataPath)
    location_dict = {}
    if ipaddress in blackListedIp:
        try:
            address = geo.record_by_addr(ipaddress)
            plong = address['longitude']
            plat = address['latitude']

            location_dict[str(ipaddress)] = str(plong) + "," + str(plat)
        except:
            print("Unregistered IP address")
    else:
        pass

    return location_dict


