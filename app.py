import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(page_title="Disease Spread / COVID Analysis", layout="wide")

# 2. Sidebar UI/UX
with st.sidebar:
    st.header("Project Submission")
    st.markdown("---")
    st.subheader("Disease Spread / COVID Analysis")
    st.write("**Name:** Barsha Das")
    st.write("**Domain:** AI in Healthcare")
    st.markdown("---")
    
    # Key Terms for Convenience
    st.subheader("Key Terms")
    st.info("""
    - **Actual Data**: Historical confirmed cases reported by WHO.
    - **Forecast Trend**: The predicted path of spread calculated by AI.
    - **Confidence Interval**: The range (shaded area) where future cases are statistically likely to fall.
    - **Cumulative Cases**: Total infections recorded from the start of the pandemic.
    """)

# 3. Data Loader (Using your uploaded WHO CSV)
@st.cache_data
def load_local_data():
    # Reading the file you provided
    df = pd.read_csv('WHO-COVID-19-global-daily-data.csv')
    # Prophet requires 'ds' (datestamp) and 'y' (value) columns
    df = df.rename(columns={'Date_reported': 'ds', 'Cumulative_cases': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    return df

# 4. Main Page Title
st.title("Disease Spread / COVID Analysis ")
st.markdown("##### Bayesian Time-Series Forecasting for Epidemiological Trends")
st.divider()

try:
    df = load_local_data()
    
    # Country Selection
    countries = df['Country'].unique()
    selected_country = st.selectbox("Select a Country for Analysis", countries)
    country_df = df[df['Country'] == selected_country].sort_values('ds')

    # 5. Prediction Logic (90-Day Forecast)
    if st.button("Generate Diagnostic Report"):
        with st.spinner('Calculating Forecast...'):
            model = Prophet(interval_width=0.95, daily_seasonality=False)
            model.fit(country_df[['ds', 'y']])
            
            future = model.make_future_dataframe(periods=90)
            forecast = model.predict(future)
            
            # Sidebar Analytics
            with st.sidebar:
                st.divider()
                st.subheader("📊 Live Analytics")
                latest_actual = country_df.iloc[-1]
                latest_forecast = forecast.iloc[-1]
                
                st.metric("Actual Cases (Latest)", f"{int(latest_actual['y']):,}")
                st.metric("Forecasted (90 Days)", f"{int(latest_forecast['yhat']):,}")
                st.write(f"Confidence Range: {int(latest_forecast['yhat_lower']):,} - {int(latest_forecast['yhat_upper']):,}")

            # 6. Professional Visualization
            st.subheader(f"Pandemic Progression & Prediction: {selected_country}")
            fig = go.Figure()

            # Confidence Shading
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', line=dict(width=0), showlegend=False))
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill='tonexty', fillcolor='rgba(0,176,246,0.1)', line=dict(width=0), name='95% Confidence Interval'))

            # Forecast Line
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecasted Trend', line=dict(color='red', width=2)))

            # ACTUAL DATA DOTS
            fig.add_trace(go.Scatter(
                x=country_df['ds'], 
                y=country_df['y'], 
                mode='markers', 
                name='Actual Reported Data',
                marker=dict(size=5, color='black', symbol='circle')
            ))

            st.plotly_chart(fig, use_container_width=True)
            
            # 7. Detailed Summary Section (Simplified for Users)
            st.divider()
            st.subheader("📋 Simplified Summary of Analysis")
            
            # Calculations for the summary
            total_actual = int(latest_actual['y'])
            projected_cases = int(latest_forecast['yhat'])
            increase_percentage = ((projected_cases - total_actual) / total_actual) * 100
            target_date = latest_forecast['ds'].strftime('%d %B %Y')
            
            summary_col1, summary_col2 = st.columns(2)
            
            with summary_col1:
                st.markdown(f"**Current Status:** {selected_country} currently has **{total_actual:,}** total confirmed cases recorded in the WHO database.")
                st.markdown(f"**Future Outlook:** Our AI model predicts that by **{target_date}**, the total count is likely to reach approximately **{projected_cases:,}**.")

            with summary_col2:
                st.markdown(f"**Growth Velocity:** The spread is projected to increase by **{increase_percentage:.2f}%** over the next 90 days based on historical trends.")
                if increase_percentage < 5:
                    st.success("Analysis: The infection curve appears to be stabilizing (flattening).")
                else:
                    st.warning("Analysis: The model indicates a continuing upward trend in infection spread.")

            st.info("**Data Note:** This summary is generated using Bayesian Curve Fitting. Actual results may vary based on public health interventions and vaccination rates.")

except Exception as e:
    st.error(f"Error: {e}. Please ensure 'WHO-COVID-19-global-daily-data.csv' is in your folder.")
