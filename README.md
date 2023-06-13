# Network-anomalies-detection

Under development:
Feel free to contribute

Aim: To capture network packets and extract information
out of packets and detect anomalies in traffic using Machine learning.

Features at present:
```bash
1. Read .pcap files
2. extract source and destination Ip addresses
3. If Ip address belongs to blacklisted category:
   a. extract its location from GeoLiteCity.dat database
   b. print on console or generate .kml file for Google maps
```

How to run:
1. Fork this repository and clone in your local environment
2. install Required packages, check requirements.txt
  ```bash
  pip install <package-name>
  ```
3. to run
 ```bash
 python3 main.py
 ```
