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

    # Initialize SessionState
    session_state = get_session_state()

    st.subheader("Add Blacklisted IP Addresses")
    new_string = st.text_input("Enter multiple IP addresses (separated by comma)")

    # Button to add the strings to the list
    if st.button("Add"):
        new_strings = new_string.split(",")
        new_strings = [s.strip() for s in new_strings]
        session_state.blackListed.extend(new_strings)
        new_string = ""

    st.write(session_state.blackListed)

    file_uploaded = st.file_uploader("Upload a .pcap file", type=".pcap")
    button_clicked = st.button("Process")

    if file_uploaded is not None and button_clicked:
        # Progress bar for file upload
        progress_bar_upload = st.progress(0)

        # Read file contents
        pcap_contents = file_uploaded.read()

        # Write file to disk
        with open("uploaded.pcap", "wb") as f:
            f.write(pcap_contents)

        # Update progress bar for file upload
        progress_bar_upload.progress(1.0)

        ip_addresses = extract_ip_addresses("uploaded.pcap")
        if len(ip_addresses) == 0:
            st.write("No packet found in the file")
            return

        for ip_src, ip_dst in ip_addresses:
            new_entry = {
                "sourceIp": f"{ip_src}",
                "destinationIp": f"{ip_dst}"
            }
            is_present = any(
                entry["sourceIp"] == new_entry["sourceIp"] and entry["destinationIp"] == new_entry["destinationIp"]
                for entry in IP_data
            )

            if not is_present:
                IP_data.append(new_entry)

        Location_df = pd.DataFrame(IP_data)
        Location_df[["ipType","blacklisted","city", "region_code", "country", "Latitude", "Longitude"]] = Location_df.apply(
            lambda row: pd.Series(get_geolocation(row["destinationIp"], session_state.blackListed)), axis=1
        )

        Location_df["Latitude"] = pd.to_numeric(Location_df["Latitude"], errors="coerce")  # Convert Latitude to float, handle invalid values as NaN
        Location_df["Longitude"] = pd.to_numeric(Location_df["Longitude"], errors="coerce")  # Convert Longitude to float, handle invalid values as NaN

        # Progress bar for processing
        progress_bar_processing = st.progress(0)

        # Serialize DataFrame to Arrow table
        table = pa.Table.from_pandas(Location_df)

        # Update progress bar for processing
        progress_bar_processing.progress(1.0)

        pd.set_option('display.max_columns', None)
        selected_rows4 = Location_df.loc[Location_df['blacklisted'] == 'Yes']
        st.header("Detected Anomalies (These Source IPs are going on blacklisted websites)")
        st.dataframe(selected_rows4)
        st.header("Summary of all the packets")
        st.dataframe(Location_df)

        os.remove("uploaded.pcap")


# Function to create or get the SessionState
def get_session_state():
    if "blackListed" not in st.session_state:
        st.session_state.blackListed = []
    return st.session_state


if __name__ == "__main__":
    main()
