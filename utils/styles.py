import streamlit as st

def apply_styles(theme="Dark"):
    colors = {
        "Dark": {
            "background": "#0f172a",
            "card_bg": "rgba(30, 41, 59, 0.7)",
            "text": "#f8fafc",
            "sub_text": "#94a3b8",
            "border": "rgba(255, 255, 255, 0.1)",
            "sidebar": "#1e293b"
        },
        "Light": {
            "background": "#f1f5f9",
            "card_bg": "rgba(255, 255, 255, 0.8)",
            "text": "#0f172a",
            "sub_text": "#475569",
            "border": "rgba(0, 0, 0, 0.1)",
            "sidebar": "#ffffff"
        }
    }[theme]

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        :root {{
            --primary: #3b82f6;
            --secondary: #10b981;
            --background: {colors['background']};
            --card-bg: {colors['card_bg']};
            --text: {colors['text']};
        }}

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            color: var(--text);
        }}
        
        .stApp {{
            background-color: var(--background);
        }}

        /* Glass Panels */
        .glass-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 12px;
            border: 1px solid {colors['border']};
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
            color: var(--text) !important;
        }}

        /* Professional Sidebar */
        section[data-testid="stSidebar"] {{
            background-color: {colors['sidebar']} !important;
            border-right: 1px solid {colors['border']};
        }}

        /* Headers */
        .main-header {{
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(to right, #60a5fa, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        
        .sub-header {{
            color: {colors['sub_text']};
            font-size: 1.1rem;
            margin-top: -1rem;
            margin-bottom: 2rem;
        }}

        /* Metrics Refinement */
        [data-testid="stMetricValue"] {{
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            color: var(--primary) !important;
        }}
        
        /* Input beautification */
        .stNumberInput input, .stSelectbox select, .stMultiSelect div {{
            background-color: {colors['card_bg']} !important;
            color: var(--text) !important;
        }}
        </style>
        """, unsafe_allow_html=True)
