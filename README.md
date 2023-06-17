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

[Demo Video](https://github.com/Flanker-shyam/Network-anomalies-detection/assets/85950516/b2ca210d-539a-4d9f-a42f-949e5e3a1fff)

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
