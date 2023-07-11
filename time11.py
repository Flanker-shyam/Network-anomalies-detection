import pyshark

# Open the pcap file for reading
cap = pyshark.FileCapture('pcap_files/demo.pcap')

# Iterate over each packet
for packet in cap:
    # Access the timestamp of the packet
    timestamp = packet.sniff_time

    # Print the timestamp
    print(timestamp)

# Close the capture file
cap.close()
