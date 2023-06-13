from generate_kml import generateKml


def kml_format_for_map(ipadrress, dataPath, blackListedIp):
    location = generateKml(ipadrress, dataPath, blackListedIp)
    for i in location.keys():
        print(""" 
        <placemark>
            <name>IP Address: %s</name>
            <styleurl>#exampleStyleDocument</styleurl>
            <Point>
            <coordinates>%s</coordinates>
            </Point>
        </placemark>
        """ % (i, location[i]))


def view_on_google(packet, dataPath, blackListedIp):
    try:
        sourceIp = packet['ip'].src
        destinationIp = packet['ip'].dst

        kml_format_for_map(sourceIp, dataPath, blackListedIp)
        kml_format_for_map(destinationIp, dataPath, blackListedIp)

    except:
        pass
