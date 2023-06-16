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
   a. extract its location from GeoLite2-city database
   b. output location of the blacklisted Ip addresses, with label of source or destination
```

How to run:
1. Fork this repository and clone in your local environment
2. Cd into this project repository
3. install Required packages, check requirements.txt
  ```bash
  pip install <package-name>
  ```
4. to run
 ```bash
 streamlit run main.py
 ```
Future aspects : Include Live packet capturing rather then reading .pcap files.
