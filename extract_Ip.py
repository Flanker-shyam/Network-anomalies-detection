import pyshark

def extract_ip_addresses(pcap_file):
    # Open the pcap file
    cap = pyshark.FileCapture(pcap_file)

    # Initialize a list to store the IP addresses
    ip_addresses = []

    # Iterate over the packets
    for packet in cap:
        # Check if the packet has an IP layer
        if 'IP' in packet:
            # Check if the source and destination attributes are present
            if hasattr(packet['IP'], 'src') and hasattr(packet['IP'], 'dst'):
                # Extract the source and destination IP addresses
                src_ip = packet['IP'].src
                dst_ip = packet['IP'].dst

                # Add the IP addresses to the list
                ip_addresses.append((src_ip, dst_ip))

    # Close the pcap file
    cap.close()

    return ip_addresses
