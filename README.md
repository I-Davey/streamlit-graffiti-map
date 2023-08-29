

# Streamlit Graffiti Map 🗺️✍️

![Demo Image of the Streamlit App](path_to_demo_image.png) 
> Replace `path_to_demo_image.png` with an actual image path for a demo/screenshot of your app for a better visual appeal.

Visualize graffiti inspections along the Eastern Fwy as of 09/02/2023 with an interactive Streamlit application. Toggle between inbound and outbound views and get detailed views of graffiti spots including images and videos.

## 🌟 Features

- 🛣️ **Interactive Map**: Switch between inbound and outbound views of the Eastern Fwy.
- 🎨 **Spot Details**: Click to see details like location, sqm, and job type (day/night).
- 📸 **Media Playback**: Supports both images and videos for clearer graffiti insights.
- 🖌️ **Data-Driven**: Reads from CSV to reflect the latest inspection updates.
- 🌐 **Polished UI**: Optimized for wide screens with company logos and sleek elements.

## 🚀 Getting Started

### Prerequisites

- Ensure you have all the required libraries installed, like Streamlit, Pandas, Folium, etc.

### Installation & Setup

1. Clone this repo:
```bash
git clone https://github.com/I-Davey/streamlit-graffiti-map.git
cd streamlit-graffiti-map
```
2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Replace the `maps_api_key` placeholder with your Google Maps API key.
4. Run the Streamlit application:
```bash
streamlit run app.py
```

## 🚫 Safety Notice

The `maps_api_key` in the sample code is a placeholder. Always keep your API keys confidential to prevent misuse. Use environment variables or other methods to secure them.
