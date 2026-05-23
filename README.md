# Jaipur Real Estate Analytics and Price Prediction Dashboard

A professional, enterprise-grade data analytics and predictive machine learning application focused entirely on the real estate market of Jaipur, Rajasthan. This project processes local spatial data, applies multidimensional clustering for Return on Investment (ROI) analysis, and delivers accurate property valuation insights through a clean, corporate-styled interactive user interface.

## Project Architecture & Directory Layout

The repository maps directly to the local development environment structural layout:
* **`app.py`** (15 KB): Core Streamlit web application. Contains the professional user interface layout, System Navigation configuration, Control Dashboard workspace, dynamic filters, 3D ROI clustering charts, and interactive geospatial mapping modules.
* **`data_train.py`** (4 KB): Dedicated Machine Learning model training pipeline. Handles data ingestion, feature scaling, geographic parameter parsing, model fitting (Scikit-Learn), and serialization functions.
* **`jaipur_real_estate_data.csv`** (610 KB): Main structured data repository containing granular records of residential properties, commercial sectors, spatial coordinates, and micro-market parameters across Jaipur.
* **`requirements.txt`**: Package dependency manifesto specifying precise version controls for deployment stability.

*Note: The serialized model file (`jaipur_real_estate_model.pkl`, ~49 MB) is excluded from version control to optimize repository performance. It can be dynamically compiled locally using the provided training pipeline script.*

## Key Functional Modules

### 1. Control Dashboard & System Navigation
* Fully configured administrative control console optimized for hierarchical data querying.
* Structured layout built without any consumer-grade emoticons to maintain strict alignment with corporate production standards.
* Themed with a professional light blue accent system designed specifically to highlight regional micro-market fluctuations.

### 2. Interactive Spatial Analytics & Mapping
* Dedicated geographical processing layout focused entirely on major zones and premium development corridors within Jaipur (e.g., Mansarovar, Malviya Nagar, Vaishali Nagar, Jagatpura, Agra Road, Ajmer Road, Tonk Road, C-Scheme).
* Integrated geospatial visualization pinpointing property clusters, average square-footage valuations, and neighborhood infrastructure metrics.

### 3. 3D ROI Clustering & Classification
* Advanced statistical clustering separating real estate options into risk-reward tiers.
* Rendered via high-fidelity 3D scatter configurations using carefully selected, distinctive color palettes to evaluate performance metrics without light/dark rendering conflicts.

## Technology Stack & Frameworks
* **Language Platform**: Python 3.10+
* **Interface Engineering**: Streamlit Framework
* **Geospatial Mapping Engine**: Folium / Streamlit-Folium / Plotly Mapbox
* **Data Visualizations**: Plotly Comprehensive (3D Engine, Analytics Charts)
* **Predictive Pipeline**: Scikit-Learn Ecosystem
* **Core Analytics**: Pandas Dataframe Engine, NumPy Scientific Vector Arrays

## Installation, Setup and Deployment

Follow these sequential instructions to initialize the application environment:

1. **Extract/Clone Project Environment**: Ensure all core files from your local environment path (`C:\Users\heman\Jaipur_Real_Estate_Project`) are consolidated.
2. **Install Dependencies**: Execute the pip package manager command to download and map the mandatory system components:
   ```bash
   git clone https://github.com/Hemanttinker/Jaipur-Real-Estate-Analytics.git
   pip install -r requirements.txt
   python data_train.py
   streamlit run app.py
