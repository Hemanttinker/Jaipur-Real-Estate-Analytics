import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

# 1. INITIAL SYSTEM FRAMEWORK
st.set_page_config(
    page_title="GeoPulse Jaipur | Corporate Real Estate AI",
    layout="wide"
)

# 2. HIGH-CONTRAST BALANCED THEME PIPELINE (IVORY CORPORATE COMFORT)
st.markdown("""
    <style>
        /* Base Page Framework Setup */
        .stApp {
            background-color: #F1F5F9 !important;
        }
        .main { 
            background-color: #F1F5F9 !important; 
            color: #0F172A !important; 
        }
        
        /* Sidebar Navigation Grid Control Panel */
        [data-testid="stSidebar"] {
            background-color: #0B0F19 !important;
            border-right: 2px solid #E2E8F0 !important;
        }
        div[data-testid="stSidebarUserContent"] { 
            background-color: #0B0F19 !important; 
            padding: 20px 10px !important;
        }
        
        /* CONTROL DASHBOARD - MAXIMUM IMPACT SIZE OVERRIDE */
        .sidebar-main-title {
            font-size: 42px !important;
            font-weight: 900 !important;
            color: #FFFFFF !important;
            font-family: 'Arial Black', Gadget, sans-serif !important;
            margin-top: 15px !important;
            margin-bottom: 35px !important;
            display: block;
            line-height: 1.1 !important;
            letter-spacing: -1px !important;
        }
        
        /* Force Sidebar Texts, Headings, and Radio Options to remain White/High-Contrast */
        div[data-testid="stSidebarUserContent"] h2, 
        div[data-testid="stSidebarUserContent"] label,
        div[data-testid="stSidebarUserContent"] p,
        div[data-testid="stSidebarUserContent"] span,
        div[data-testid="stSidebarUserContent"] div,
        div[data-testid="stSidebarUserContent"] label p { 
            color: #FFFFFF !important; 
            font-weight: 800 !important;
            font-size: 16px !important;
        }
        
        /* Metric Summary Showcase Grid Cards */
        .stMetric { 
            background-color: #FFFFFF !important; 
            border-radius: 12px !important; 
            padding: 20px !important; 
            border-top: 6px solid #2563EB !important;
            box-shadow: 0px 4px 12px rgba(15, 23, 42, 0.05) !important;
            margin-bottom: 15px !important;
        }
        
        /* Metrics Text Formatting */
        div[data-testid="stMetricLabel"] > div {
            color: #334155 !important;
            font-weight: 800 !important;
            font-size: 13px !important;
            text-transform: uppercase !important;
        }
        div[data-testid="stMetricValue"] { 
            color: #1E3A8A !important; 
            font-size: 26px !important; 
            font-weight: 800 !important;
        }
        
        /* STICKY PURE DARK TEXT OVER SLIDERS AND SELECTION FIELDS */
        label[data-testid="stWidgetLabel"] p,
        .stSlider p, 
        .stSelectbox p, 
        div[data-testid="stMarkdownContainer"] p,
        span[data-testid="stWidgetLabel"] {
            color: #0F172A !important;
            font-weight: 800 !important;
            font-size: 15px !important;
        }
        
        /* Form Box Input Field Control Wrappers */
        div[role="slider"], 
        div[data-testid="stWidgetLabel"], 
        .stSelectbox div[role="button"] {
            color: #0F172A !important;
            font-weight: 800 !important;
        }
        
        /* Clear Row Padding gaps */
        div[data-testid="stVerticalBlock"] > div {
            margin-bottom: 24px !important;
        }
        
        /* Clean Headers */
        h1 { color: #1E3A8A !important; font-weight: 800 !important; font-size: 36px !important; }
        h2 { color: #2563EB !important; font-weight: 800 !important; margin-top: 15px !important; }
        h3 { color: #0F172A !important; font-weight: 800 !important; }
        
        /* Action Framework Button */
        div.stButton > button:first-child { 
            background-color: #2563EB !important; 
            color: #FFFFFF !important; 
            border-radius: 8px !important; 
            width: 100% !important; 
            font-weight: 800 !important; 
            font-size: 16px !important;
            height: 50px !important; 
            box-shadow: 0px 4px 12px rgba(37, 99, 235, 0.2) !important;
            margin-top: 15px !important;
        }
        div.stButton > button:first-child:hover { 
            background-color: #1E3A8A !important; 
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_assets():
    df = pd.read_csv('jaipur_real_estate_data.csv')
    model = joblib.load('jaipur_real_estate_model.pkl')
    return df, model

try:
    df, model = load_assets()
except Exception as e:
    st.error("Assets matching validation criteria missing! Please compile database architecture first.")
    st.stop()

# 14 EXPLICIT, HIGHLY DISTINCT SOLID DARK/RICH COLORS (NO SHADE OVERLAPS OR LIGHT VARIATIONS)
location_color_palette = [
    '#800000',  # Maroon
    '#000080',  # Navy Blue
    '#1E4D2B',  # Deep Forest Green
    '#704214',  # Sepia Brown
    '#4B0082',  # Indigo Purple
    '#D96B27',  # Burnt Orange
    '#008080',  # Dark Teal
    '#A020F0',  # Bold Purple
    '#2F4F4F',  # Dark Slate Charcoal
    '#C5A059',  # Dark Matte Gold
    '#C71585',  # Medium Violet Red
    '#4169E1',  # Royal Blue
    '#8B4513',  # Saddle Chocolate
    '#32CD32'   # Lime Solid
]

# PAGE HEADER TITLE INDEX
st.title("GeoPulse Jaipur™ — Real Estate AI & Valuation Platform")
st.markdown("### *Enterprise Predictive Analytics & Market Concentration Engine for 14 Jaipur Neighborhoods*")
st.write("---")

# INSANELY BOLD LARGE CONTROL DASHBOARD SIDEBAR INJECTION
st.sidebar.markdown('<span class="sidebar-main-title">Control Dashboard</span>', unsafe_allow_html=True)

app_mode = st.sidebar.radio(
    "Select System Module",
    ["Executive Overview", "AI Price Prediction Engine", "Market Dynamic Core", "3D ROI Clustering Hub", "Area Wise Comparison"]
)

# HELPER FUNCTION FOR GRAPH STYLING CONTRAST OVERRIDE
def apply_high_contrast_graph_theme(fig, title_text):
    fig.update_layout(
        title={'text': title_text, 'font': {'size': 18, 'color': '#0F172A', 'weight': 'bold'}},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='#FFFFFF',
        font=dict(color='#0F172A', size=13, family="Arial, sans-serif"),
        xaxis=dict(
            title=dict(font=dict(size=14, color='#0F172A', weight='bold')),
            tickfont=dict(size=12, color='#0F172A', weight='bold'),
            gridcolor='#E2E8F0',
            linecolor='#0F172A',
            linewidth=2
        ),
        yaxis=dict(
            title=dict(font=dict(size=14, color='#0F172A', weight='bold')),
            tickfont=dict(size=12, color='#0F172A', weight='bold'),
            gridcolor='#E2E8F0',
            linecolor='#0F172A',
            linewidth=2
        ),
        legend=dict(
            font=dict(size=12, color='#0F172A', weight='bold'),
            bgcolor='rgba(255,255,255,0.8)'
        )
    )
    return fig

# MODULE 1: EXECUTIVE OVERVIEW
if app_mode == "Executive Overview":
    st.header("Jaipur Real Estate Executive Command Center")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric(label="Total Properties Tracked", value=f"{len(df):,} Units")
    with m2: st.metric(label="Avg Price Index", value=f"₹{(df['Price'].mean()/100000):.2f} Lakhs")
    with m3: st.metric(label="Peak Return On Capital (ROI)", value=f"{df['ROI_Pct'].max()}%")
    with m4: st.metric(label="Highest Demand Vector Zone", value="Raja Park")
        
    st.write("###")
    c1, c2 = st.columns([3, 2])
    with c1:
        fig_bar = px.bar(
            df.groupby('Location')['Price'].mean().reset_index().sort_values(by='Price', ascending=False),
            x='Location', y='Price', color='Location', color_discrete_sequence=location_color_palette, template='plotly_white'
        )
        fig_bar = apply_high_contrast_graph_theme(fig_bar, "Market Capital Concentration Across 14 Jaipur Neighborhoods")
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        fig_pie = px.pie(df, names='Property_Type', values='Price', hole=0.4, color_discrete_sequence=px.colors.qualitative.Bold, template='plotly_white')
        fig_pie.update_layout(
            title={'text': "Structural Inventory Allocation", 'font': {'size': 18, 'color': '#0F172A', 'weight': 'bold'}},
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#0F172A', size=13, weight='bold')
        )
        st.plotly_chart(fig_pie, use_container_width=True)

# MODULE 2: AI PRICE PREDICTION ENGINE
elif app_mode == "AI Price Prediction Engine":
    st.header("Advanced Random Forest Price Forecast Terminal")
    st.markdown("Fill out the structural configurations below to compute live valuations.")
    st.write("###")
    
    col_in1, col_in2, col_in3 = st.columns(3)
    
    with col_in1:
        selected_loc = st.selectbox("Target Jaipur Neighborhood", sorted(df['Location'].unique()))
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        selected_type = st.selectbox("Property Typology Category", sorted(df['Property_Type'].unique()))
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        sqft_val = st.slider("Built-up Area Size (Sqft)", int(df['Sqft'].min()), int(df['Sqft'].max()), 1500, step=50)
        
    with col_in2:
        bhk_val = st.slider("Total Room Configuration (BHK)", 0, 5, 3) if selected_type != 'Residential Plot' else 0
        st.markdown("<div style='height: 45px;'></div>", unsafe_allow_html=True)
        age_val = st.slider("Structural Asset Age (Years)", int(df['Age'].min()), int(df['Age'].max()), 2)
        
    with col_in3:
        metro_val = st.slider("Distance to Nearest Metro Link (KM)", 0.1, 15.0, 2.5, step=0.1)
        st.markdown("<div style='height: 45px;'></div>", unsafe_allow_html=True)
        amenities_val = st.slider("Premium Amenities Rating (1-10)", 1, 10, 5)

    st.write("###")
    if st.button("RUN MACHINE LEARNING ENGINE VALUATION"):
        loc_cols = [f'Location_{x}' for x in sorted(df['Location'].unique())]
        type_cols = [f'Property_Type_{x}' for x in sorted(df['Property_Type'].unique())]
        feature_order = ['Sqft', 'BHK', 'Age', 'Metro_Dist', 'Amenities_Score'] + loc_cols + type_cols
        
        input_dict = {col: 0 for col in feature_order}
        input_dict['Sqft'] = sqft_val
        input_dict['BHK'] = bhk_val
        input_dict['Age'] = age_val
        input_dict['Metro_Dist'] = metro_val
        input_dict['Amenities_Score'] = amenities_val
        
        if f'Location_{selected_loc}' in input_dict: input_dict[f'Location_{selected_loc}'] = 1
        if f'Property_Type_{selected_type}' in input_dict: input_dict[f'Property_Type_{selected_type}'] = 1
        
        input_df = pd.DataFrame([input_dict])[feature_order]
        pred_raw = model.predict(input_df)[0]
        
        st.write("---")
        res_col1, res_col2 = st.columns([2, 1])
        with res_col1:
            st.success(f"### Algorithmic Market Value Vector: ₹ {pred_raw:,.2f} INR")
            st.info(f"**Target Micro-market pricing index verified:** {selected_loc} Zone Framework.")
        with res_col2:
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number", value = pred_raw / 100000,
                title = {'text': "Valuation (Lakhs INR)", 'font': {'color': "#1E3A8A", 'size': 18, 'weight': 'bold'}},
                gauge = {'axis': {'range': [None, df['Price'].max()/100000]}, 'bar': {'color': "#2563EB"}}
            ))
            fig_gauge.update_layout(paper_bgcolor='#FFFFFF', font={'color': "#0F172A", 'weight': 'bold'}, height=220, margin=dict(l=15,r=15,t=40,b=15))
            st.plotly_chart(fig_gauge, use_container_width=True)

# MODULE 3: MARKET DYNAMIC CORE
elif app_mode == "Market Dynamic Core":
    st.header("Transit Infrastructure Elasticity Analytics")
    fig_trend = px.scatter(
        df, x='Metro_Dist', y='Price', color='Location', size='Sqft',
        color_discrete_sequence=location_color_palette, template='plotly_white', 
        labels={'Metro_Dist': 'Distance to Jaipur Metro Link (KM)', 'Price': 'Price (INR)'}
    )
    fig_trend = apply_high_contrast_graph_theme(fig_trend, "Impact of Metro Proximity Transit Networks on Valuation Scales")
    st.plotly_chart(fig_trend, use_container_width=True)

# MODULE 4: 3D ROI CLUSTERING HUB
elif app_mode == "3D ROI Clustering Hub":
    st.header("3D Multi-Dimensional Capital ROI Engine Matrix")
    st.markdown("Interactive 3D Grid Engine. **Ghumao, zoom karo aur interact karo!**")
    fig_3d = px.scatter_3d(
        df, x='Sqft', y='ROI_Pct', z='Price', color='Location', size='Demand_Index',
        symbol='Property_Type', opacity=0.85, color_discrete_sequence=location_color_palette, 
        template='plotly_white', height=700
    )
    fig_3d.update_layout(
        font=dict(color='#0F172A', size=12, weight='bold'),
        scene=dict(
            xaxis=dict(title=dict(font=dict(color='#0F172A', weight='bold')), tickfont=dict(color='#0F172A', weight='bold')),
            yaxis=dict(title=dict(font=dict(color='#0F172A', weight='bold')), tickfont=dict(color='#0F172A', weight='bold')),
            zaxis=dict(title=dict(font=dict(color='#0F172A', weight='bold')), tickfont=dict(color='#0F172A', weight='bold'))
        )
    )
    st.plotly_chart(fig_3d, use_container_width=True)

# MODULE 5: AREA WISE COMPARISON
else:
    st.header("Inter-Zone Side-by-Side Area Performance Matrix")
    c1, c2 = st.columns(2)
    with c1: loc_1 = st.selectbox("Select Location Alpha", sorted(df['Location'].unique()), index=0)
    with c2: loc_2 = st.selectbox("Select Location Beta", sorted(df['Location'].unique()), index=1)
    
    df_loc1 = df[df['Location'] == loc_1]
    df_loc2 = df[df['Location'] == loc_2]
    
    st.write("### Matrix Performance Overview")
    metric_c1, metric_c2 = st.columns(2)
    with metric_c1:
        st.markdown(f"#### {loc_1} Metrics Summary")
        st.dataframe(df_loc1.describe()[['Price', 'ROI_Pct', 'Sqft']])
    with metric_c2:
        st.markdown(f"#### {loc_2} Metrics Summary")
        st.dataframe(df_loc2.describe()[['Price', 'ROI_Pct', 'Sqft']])
        
    compare_df = df[df['Location'].isin([loc_1, loc_2])]
    fig_comp = px.histogram(compare_df, x='Price', color='Location', barmode='overlay', color_discrete_sequence=['#2563EB', '#10B981'], template='plotly_white')
    fig_comp = apply_high_contrast_graph_theme(fig_comp, "Price Distribution Comparison Matrix")
    st.plotly_chart(fig_comp, use_container_width=True)