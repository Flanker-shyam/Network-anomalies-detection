from print_location import printLocation 

def printPacketData(packet,blackListIp,dataPath):
    try:
        sourceIp = packet['ip'].src
        destinationIp = packet['ip'].dst

        if sourceIp in blackListIp:
            print(f"[+] source ip: {sourceIp}---------> destination ip: {destinationIp}")
            print("[+] printing sourceIp location")
            printLocation(str(sourceIp),dataPath)

        elif destinationIp in blackListIp:
            print(f"[+] destination ip: {destinationIp}")
            print("[+] printing destinationIp location")
            printLocation(str(destinationIp),dataPath)

        else:
            pass
    except:
        pass
    

