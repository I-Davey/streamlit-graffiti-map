import pandas as pd
import streamlit as st
import folium
import numpy as np
from streamlit_folium import st_folium

# Setting up the Streamlit page configuration
st.set_page_config(layout="wide", page_title="Eastern Fwy Graffiti Inspection - 09/02/2023")

# Displaying the title and logo
cc1, cc2 = st.columns((1, 1))
with cc1:
    st.title("Eastern Fwy Graffiti Inspection - 09/02/2023")

with cc2:
    with open("gw_logo.jpg", "rb") as gw_logo:
        gw_logo_bytes = gw_logo.read()

        st.image(gw_logo_bytes, width=200, caption="")

# Function to load the graffiti inspection data
@st.cache_resource
def load_data():
    """
    Load the graffiti inspection data from the CSV.
    Process the coordinates and return the cleaned dataframe.
    """
    data = pd.read_csv("data.csv")
    
    # Cleaning up the coordinate data
    data["physical_coordinate"] = data["physical_coordinate"].str.replace("(", "").str.replace(")", "")
    data[["lat", "lon"]] = data["physical_coordinate"].str.split(",", expand=True).astype(float)

    return data

# Function to calculate the midpoint of the given set of coordinates
def mpoint(lat, lon):
    """
    Calculate the midpoint of the given set of coordinates.
    """
    return (np.nanmean(lat), np.nanmean(lon))

# Function to create the map
@st.cache_resource
def create_map(data):
    """
    Create a folium map centered at the midpoint of the given data.
    Add markers for each graffiti inspection location.
    """
    midpoint = mpoint(data["lat"], data["lon"])
    m = folium.Map(location=[midpoint[0], midpoint[1]], zoom_start=12)
    featuregroup = folium.FeatureGroup(name="Jobs")
    for _, row in data.iterrows():
        featuregroup.add_child(folium.Marker(location=[row["lat"], row["lon"]]))

    return m, featuregroup

# Function to display the selected video
def show_vid(data):
    """
    Display the video of the selected graffiti inspection location.
    """
    data = data.to_dict("records")[0]
    with c4:
        st.write(f"""**{data['loc_name']}** | **{"Day Job" if data['is_day_job'] else "Night Job"}** """)

    if data["type"] == "video":
        with open('./clips/' + data["path"], "rb") as video_file:
            st.video(video_file.read())

# Main execution
data = load_data()

c3, c4 = st.columns((1, 1))
# User selection for Inbound or Outbound
with c3:
    switch = st.selectbox("Select Inbound or Outbound", ["Inbound", "Outbound"])

# Filter the data based on user selection
filtered_data = data[data["direction"] == switch.lower()]

# Create the map with filtered data
m, featuregroup = create_map(filtered_data)

c1, c2 = st.columns(2)

with c1:
    output = st_folium(m, feature_group_to_add=featuregroup, width=1000, height=500)
    st.session_state["clicked_object"] = output.get("last_object_clicked", None)

# Display the video of the selected location
with c2:
    if st.session_state.get("clicked_object"):
        lat = st.session_state["clicked_object"]['lat']
        lon = st.session_state["clicked_object"]["lng"]
        cur_job = filtered_data[(filtered_data["lat"] == lat) & (filtered_data["lon"] == lon)]
        show_vid(cur_job)
