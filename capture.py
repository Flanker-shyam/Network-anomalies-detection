import pyshark

def capture_packets():
    capture = pyshark.LiveCapture(interface='eth0')
    capture.sniff(timeout=50)

    for packet in capture.sniff_continuously(packet_count=5):
        print('Just arrived:', packet)