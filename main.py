import webbrowser
import pyshark
from printData import printPacketData
import os
from view_google import view_on_google

def main():
    # Code to be executed when the script is run directly

    print("[+] Enter mode: ")
    print("[+] Type 1 for cli (to print location on commandline)")
    print("[+] Type 2 for kml(to print location on google map)")
    choice = int(input())

    print("[+] Enter path of GeoLiteIp.dat file")
    dataPath = input()

    if (not os.path.exists(dataPath)):
        print("[-] File doesn't exist")
        return

    blackListIp = ['2.1.1.2','2.1.1.1','103.229.206.240','192.168.43.108','2a03:2880:f22f:c5:face:b00c:0:167', '2409:4055:496:ab1e:ef70:9540:fee8:9832', '212.242.33.35' ,'147.137.21.94','157.39.74.255','2409:4055:496:ab1e:ef70:9540:fee8:9832']

    # capture = pyshark.LiveCapture(interface='wlo1')
    # capture.sniff(timeout=50)

    capture = pyshark.FileCapture('ipv4frags.pcap')
    # for packet in capture.sniff_continuously(packet_count=5):
    for packet in capture:
        print('Just arrived:', packet)

        if(choice == 1):
            print("printing on console")
            printPacketData(packet,blackListIp,dataPath)
        elif(choice == 2):
            print("""
            <?xml version="1.0" encoding="UTF-8"?>
            <kml xmlns="http://www.opengis.net/kml/2.2">
            <Document>
                <name>sourceip.kml</name>
                <open>1</open>
                <Style id="exampleStyleDocument">
                <LabelStyle>
                    <color>ff0000cc</color>
                </LabelStyle>
                </Style>\n""")
            view_on_google(packet, dataPath, blackListIp)
            print( """\n
            </Document>
            </kml>
            """)
            new=1
            url="https://www.google.com/maps/d/splash?app=mp"
            webbrowser.open(url,new=new)
                                                                                                
# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()