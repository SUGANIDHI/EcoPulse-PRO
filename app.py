import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Modular Imports
from utils.styles import apply_styles
from utils.data_manager import load_processed_data, calculate_cagr, get_market_metrics
from utils.ml_engine import ForecastingEngine

# --- INITIALIZATION ---
st.set_page_config(
    page_title="EcoPulse Pro | Energy Intelligence",
    page_icon="💹",
    layout="wide",
)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:#60a5fa;'>EcoPulse <span style='color:white;'>PRO</span></h2>", unsafe_allow_html=True)
    st.markdown("`Enterprise Intelligence v2.0`")
    st.write("")
    
    # Professional Styling
    current_theme = "Dark"
    apply_styles(current_theme)
    px_template = "plotly_dark"
    
    module = st.radio("Intelligence Modules", 
                       ["Market Overview", "Regional Deep-Dive", "Forecasting Engine", "Multi-Market Comparison", "Historical Audit"])
    
    st.markdown("---")
    st.caption("Developed for Professional Policy Analysis & Market Research.")
    if st.button("Refresh Infrastructure"):
        st.cache_data.clear()
        st.rerun()

df = load_processed_data()

# --- MODULES ---

if module == "Market Overview":
    st.markdown("<h1 class='main-header'>Global Energy Matrix</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>A multi-dimensional view of production, consumption, and efficiency.</p>", unsafe_allow_html=True)
    
    metrics = get_market_metrics(df)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Consumption", f"{metrics['consumption']/1000:.1f} PWh", f"{metrics['yoy']:.2f}% YoY")
    col2.metric("Renewable Penetration", f"{metrics['renewable_share']:.1f}%", "+0.8% Target")
    col3.metric("Global GDP (Est)", f"${metrics['gdp']:.1f}T")
    col4.metric("Active Regions", metrics['regions'])

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Global Energy Intensity Map")
    fig = px.choropleth(df[df['year'] == metrics['latest_year']], 
                        locations="iso_code",
                        color="primary_energy_consumption",
                        hover_name="country",
                        color_continuous_scale="Viridis",
                        template=px_template,
                        height=600)
    fig.update_layout(margin=dict(l=0, r=0, t=10, b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Regional Consumption Distribution")
        # Treemap for visual diversity
        fig = px.treemap(df[df['year'] == metrics['latest_year']], 
                         path=['country'], 
                         values='primary_energy_consumption',
                         color='renewable_share',
                         color_continuous_scale='RdYlGn',
                         template=px_template)
        fig.update_layout(margin=dict(t=30, l=10, r=10, b=10), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Top 10 Energy Consumers")
        top_10 = df[df['year'] == metrics['latest_year']].nlargest(10, 'primary_energy_consumption')
        fig = px.bar(top_10, x='primary_energy_consumption', y='country', orientation='h',
                     color='primary_energy_consumption', color_continuous_scale='Blues',
                     template=px_template)
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif module == "Regional Deep-Dive":
    st.markdown("<h1 class='main-header'>Regional Intelligence</h1>", unsafe_allow_html=True)
    
    country = st.selectbox("Market Selection", sorted(df['country'].unique()))
    c_df = df[df['country'] == country].sort_values('year')
    
    # Regional Stats
    cagr = calculate_cagr(c_df['primary_energy_consumption'].iloc[0], 
                           c_df['primary_energy_consumption'].iloc[-1], 
                           len(c_df))
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Demand", f"{c_df['primary_energy_consumption'].iloc[-1]:,.1f} TWh")
    col2.metric("Long-term CAGR", f"{cagr:.2f}%")
    col3.metric("GDP correlation", f"{c_df['primary_energy_consumption'].corr(c_df['gdp']):.3f}")

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader(f"Strategic Growth Trajectory: {country}")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=c_df['year'], y=c_df['primary_energy_consumption'], name='Energy', marker_color='#3b82f6', opacity=0.7))
    fig.add_trace(go.Scatter(x=c_df['year'], y=c_df['gdp']/1e9, name='GDP ($B)', yaxis='y2', line=dict(color='#fbbf24', width=3)))
    
    fig.update_layout(
        template=px_template,
        yaxis=dict(title="Energy (TWh)"),
        yaxis2=dict(title="GDP ($B)", overlaying='y', side='right'),
        legend=dict(orientation="h", x=0.5, xanchor="center", y=1.1),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Energy Mix Transition")
        fig = px.area(c_df, x='year', y=['renewables_consumption', 'fossil_fuel_consumption'],
                      labels={'value': 'Consumption (TWh)', 'variable': 'Source'},
                      color_discrete_map={'renewables_consumption': '#10b981', 'fossil_fuel_consumption': '#ef4444'},
                      template=px_template)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Current Energy Profile")
        latest_c = c_df.iloc[-1]
        mix_data = pd.DataFrame({
            'Source': ['Renewables', 'Fossil Fuels'],
            'Consumption': [latest_c['renewables_consumption'], latest_c['fossil_fuel_consumption']]
        })
        fig = px.pie(mix_data, values='Consumption', names='Source', hole=0.4,
                     color_discrete_map={'Renewables': '#10b981', 'Fossil Fuels': '#ef4444'},
                     template=px_template)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif module == "Multi-Market Comparison":
    st.markdown("<h1 class='main-header'>Market Comparison</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Inter-regional benchmarking of energy penetration and economic correlation.</p>", unsafe_allow_html=True)
    
    selected_countries = st.multiselect("Select Markets to Compare", 
                                        options=sorted(df['country'].unique()), 
                                        default=["Afghanistan", "Albania", "Algeria"])
    
    if not selected_countries:
        st.warning("Please select at least one market for analysis.")
    else:
        comp_df = df[df['country'].isin(selected_countries)]
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("Renewable Adoption Benchmark")
            fig = px.line(comp_df, x='year', y='renewable_share', color='country', 
                          template=px_template, line_shape="spline")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with c2:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.subheader("GDP vs Energy intensity (Log Scale)")
            fig = px.scatter(comp_df, x='gdp', y='primary_energy_consumption', 
                             color='country', size='population', hover_name='year',
                             log_x=True, log_y=True, template=px_template)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Comparative Data Grid")
        pivoted = comp_df.pivot_table(index='year', columns='country', values='primary_energy_consumption')
        st.dataframe(pivoted.transpose(), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif module == "Forecasting Engine":
    st.markdown("<h1 class='main-header'>Predictive Modelling</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Neural-enhanced forecasting using industrial-grade regression models.</p>", unsafe_allow_html=True)
    
    # Model Selection
    with st.sidebar:
        st.markdown("---")
        st.subheader("Model Configuration")
        model_choice = st.selectbox("Preferred Algorithm", ["Random Forest", "XGBoost"])
    
    engine = ForecastingEngine(df)
    engine = engine.train(model_type="RF" if model_choice == "Random Forest" else "XGBoost")
    
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Simulation Parameters")
        target_year = st.slider("Forecast Year", 2024, 2050, 2030)
        pop_growth = st.slider("Pop. Growth Factor (%)", -2.0, 5.0, 1.1)
        gdp_growth = st.slider("GDP Growth Factor (%)", -1.0, 10.0, 3.2)
        
        latest_avg_pop = df[df['year'] == df['year'].max()]['population'].mean()
        latest_avg_gdp = df[df['year'] == df['year'].max()]['gdp'].mean()
        
        sim_pop = latest_avg_pop * (pow(1 + pop_growth/100, target_year - df['year'].max()))
        sim_gdp = latest_avg_gdp * (pow(1 + gdp_growth/100, target_year - df['year'].max()))
        
        if st.button("Execute Simulation"):
            prediction = engine.predict(target_year, sim_pop, sim_gdp)
            st.write(f"### Forecast: {prediction:,.2f} TWh")
            st.write(f"*Algorithm: {model_choice}*")
            st.progress(min(max(prediction/100000, 0.0), 1.0))
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader(f"{model_choice} Analytics")
        
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("Coefficient R²", f"{engine.metrics['r2']*100:.2f}%")
        m_col2.metric("Mean Absolute Error", f"{engine.metrics['mae']:.2f}")
        
        st.write("**Feature Importance Weighting**")
        fig = px.bar(engine.metrics['importance'], x='Feature', y='Value', color='Value', 
                     color_continuous_scale='Magma', template=px_template)
        fig.update_layout(height=280, margin=dict(t=20, b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif module == "Historical Audit":
    st.markdown("<h1 class='main-header'>Raw Archive Audit</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Data Explorer")
    st.dataframe(df.head(100), use_container_width=True)
    
    st.download_button(
        label="Export Intelligence Report (CSV)",
        data=df.to_csv().encode('utf-8'),
        file_name='energy_intelligence_export.csv',
        mime='text/csv',
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.9rem;'>EcoPulse Intelligence Matrix v2.0 • Enterprise Grade Analytics Solution</div>", unsafe_allow_html=True)
