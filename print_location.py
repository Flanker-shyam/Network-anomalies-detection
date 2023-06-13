import pygeoip

def printLocation(ipaddress,dataPath):
        gic = pygeoip.GeoIP(dataPath)
        try:
            address=gic.record_by_addr(ipaddress)
            pcity=address['city']
            pregion=address['region_code']
            pcountry=address['country_name']
            plong=address['latitude']
            plat=address['longitude']

            print(f"[*] Target {ipaddress} is located at>")
            print(f"[+] Longitude: {plong} + Latitude: {plat}")
            print(f"[+] City: {pcity} + Region Code: {pregion} + Country: {pcountry}")

        except:
              pass
