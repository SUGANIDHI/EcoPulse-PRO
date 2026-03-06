import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

class ForecastingEngine:
    def __init__(self, df):
        self.df = df
        self.features = ['year', 'population', 'gdp']
        self.target = 'primary_energy_consumption'
        self.model = None
        self.metrics = {}

    @st.cache_resource()
    def train(_self, model_type="RF"):
        # Prepare data
        data = _self.df.dropna(subset=_self.features + [_self.target])
        X = data[_self.features]
        y = data[_self.target]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        if model_type == "XGBoost":
            _self.model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
        else:
            _self.model = RandomForestRegressor(n_estimators=150, max_depth=15, min_samples_split=5, random_state=42, n_jobs=-1)
            
        _self.model.fit(X_train, y_train)
        
        # Audit
        preds = _self.model.predict(X_test)
        _self.metrics = {
            "model_name": model_type,
            "r2": r2_score(y_test, preds),
            "mae": mean_absolute_error(y_test, preds),
            "importance": pd.DataFrame({'Feature': _self.features, 'Value': _self.model.feature_importances_})
        }
        return _self

    def predict(self, year, pop, gdp):
        # Ensure model is ready (though app logic usually handles this via train call)
        if self.model is None:
             self.train()
        input_data = pd.DataFrame([[year, pop, gdp]], columns=self.features)
        return self.model.predict(input_data)[0]
