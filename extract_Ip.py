import pyshark

def extract_ip_addresses(pcap_file):
    ip_addresses = []

    # Open the pcap file
    capture = pyshark.FileCapture(pcap_file)

    # Extract IP addresses
    for packet in capture:
        if "IP" in packet:
            ip_src = packet.ip.src
            ip_dst = packet.ip.dst
            ip_addresses.append((ip_src, ip_dst))

    return ip_addresses