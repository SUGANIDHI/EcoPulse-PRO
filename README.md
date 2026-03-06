# EcoPulse PRO: Energy Intelligence Matrix v2.0

EcoPulse PRO is a data-driven energy analytics and predictive intelligence platform designed to analyze global energy consumption patterns and forecast future demand. The system integrates data engineering, machine learning, and interactive visualization to deliver actionable insights into energy trends, renewable adoption, and economic drivers of global energy demand.

---

## Project Overview

EcoPulse PRO enables analysts, researchers, and policymakers to explore global energy trends across multiple dimensions, including production, efficiency, and economic correlations.

**Key capabilities include:**
* Global energy consumption analysis
* Renewable vs fossil energy transition insights
* Country and regional benchmarking
* Machine learning–based forecasting up to 2050
* Interactive web-based analytics dashboard

---

## Core Intelligence Modules

### Global Energy Matrix
* **Interactive Choropleth Mapping**: Visualize global energy consumption patterns.
* **TreeMap Micro-Analysis**: Regional distribution of energy demand.
* **Consumption KPIs**: Total global PWh, year-over-year momentum, and renewable penetration metrics.

### Regional Deep-Dive
* **CAGR Indicators**: Analyze 50-year energy demand growth trajectories.
* **Energy Mix Transition Analysis**: Compare fossil and renewable adoption.
* **Economic Correlation Engine**: Evaluate relationships between energy demand and GDP growth.

### Predictive Forecasting Engine
* **Dual Machine Learning Models**:
    * Random Forest (R² ≈ 98.9%)
    * XGBoost (R² ≈ 92.8%)
* **Simulation Sandbox**:
    * Adjust GDP and population growth factors.
    * Forecast global energy demand through 2050.
* **Feature Importance Dashboard**: Real-time visualization of economic drivers influencing energy consumption.

### Multi-Market Comparison
* **Inter-Regional Benchmarking**: Compare energy adoption patterns across selected countries.
* **Logarithmic Scaling**: Normalize energy demand relative to economic scale for fair comparisons.

---

## Technology Stack

| Layer | Technology |
| :--- | :--- |
| Dashboard Framework | Streamlit |
| Data Processing | Pandas + NumPy |
| Visualization | Plotly |
| Machine Learning | scikit-learn + XGBoost |
| UI Styling | Custom Glassmorphism CSS with Inter Typography |

---

## Getting Started

### Prerequisites
* Python 3.8 or higher
* Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SUGANIDHI/EcoPulse-PRO.git
   cd EcoPulse-PRO
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

Open the dashboard in your browser: `http://localhost:8501`

---

## Project Architecture

```text
EcoPulse-PRO
│
├── utils/
│   ├── data_manager.py      # Data ingestion and transformation
│   ├── ml_engine.py         # Machine learning models and evaluation
│   └── styles.py            # UI/UX styling and theme configuration
│
├── app.py                   # Streamlit application entry point
├── Energy_Intelligence_Matrix.csv # Processed analytical data
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## Use Cases

EcoPulse PRO supports several analytical scenarios:
* Global energy demand forecasting
* Renewable energy transition analysis
* Policy research and economic impact studies
* Data science portfolio demonstrations

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
**Suganidhi Baskar**  
[GitHub Profile](https://github.com/SUGANIDHI)
