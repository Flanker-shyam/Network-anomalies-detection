import os
import pandas as pd
import numpy as np
import pyarrow as pa
from getLocation import get_geolocation
from extract_Ip import extract_ip_addresses
import streamlit as st

# Streamlit app
def main():
    st.title("Network Anomalies")
    IP_data = []

    uploaded_file = st.file_uploader("Upload a .pcap file", type=".pcap")

    if uploaded_file is not None:
        pcap_contents = uploaded_file.read()

        with open("uploaded.pcap", "wb") as f:
            f.write(pcap_contents)

        ip_addresses = extract_ip_addresses("uploaded.pcap")

        for ip_src, ip_dst in ip_addresses:
            new_entry = {
                "sourceIp": f"{ip_src}",
                "destinationIp": f"{ip_dst}"
            }
            is_present = any(entry["sourceIp"] == new_entry["sourceIp"] and entry["destinationIp"] == new_entry["destinationIp"] for entry in IP_data)

            if not is_present:
                IP_data.append(new_entry)

        st.subheader("Add Blacklisted IP Addresses")
        new_value = st.text_input('Type an IP')

        if st.button('Add'):
            blackListed = [new_value]
            Location_df = pd.DataFrame(IP_data)
            Location_df[["city", "region_code", "country", "Latitude", "Longitude", "blacklisted"]] = Location_df.apply(lambda row: pd.Series(get_geolocation(row["sourceIp"], row["destinationIp"], blackListed)), axis=1)

            Location_df["Latitude"] = pd.to_numeric(Location_df["Latitude"], errors="coerce")  # Convert Latitude to float, handle invalid values as NaN
            Location_df["Longitude"] = pd.to_numeric(Location_df["Longitude"], errors="coerce")  # Convert Longitude to float, handle invalid values as NaN

            # Serialize DataFrame to Arrow table
            table = pa.Table.from_pandas(Location_df)

            st.dataframe(Location_df)

        os.remove("uploaded.pcap")

if __name__ == "__main__":
    main()
