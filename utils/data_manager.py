import pandas as pd
import streamlit as st

@st.cache_data
def load_processed_data():
    df = pd.read_csv('Energy_Intelligence_Matrix.csv')
    return df

def calculate_cagr(start_val, end_val, periods):
    if periods <= 1 or start_val == 0 or pd.isna(start_val) or pd.isna(end_val): 
        return 0
    return (pow(end_val / start_val, 1/periods) - 1) * 100

def get_market_metrics(df):
    latest_yr = df['year'].max()
    prev_yr = latest_yr - 1
    
    current = df[df['year'] == latest_yr]
    previous = df[df['year'] == prev_yr]
    
    curr_sum = current['primary_energy_consumption'].sum()
    prev_sum = previous['primary_energy_consumption'].sum()
    
    yoy = ((curr_sum - prev_sum) / prev_sum) * 100 if prev_sum != 0 else 0
    ren_penetration = current['renewable_share'].mean()
    global_gdp = current['gdp'].sum() / 1e12
    regions_count = len(df['country'].unique())
    
    return {
        "latest_year": latest_yr,
        "consumption": curr_sum,
        "yoy": yoy,
        "renewable_share": ren_penetration,
        "gdp": global_gdp,
        "regions": regions_count
    }
