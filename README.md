# Disease Spread / COVID Analysis 

### **Project Title**
**Advanced Epidemiological Trend Analysis and 90-Day Spread Prediction using Bayesian Time-Series Modeling**

---

### **Problem Statement**
The volatile nature of infectious disease spread, characterized by sudden waves and seasonal fluctuations, makes standard linear forecasting models inaccurate. Traditional models often fail to capture complex, non-linear patterns, leading to unreliable forecasts. There is a critical need for AI-driven systems that can analyze seasonal spikes and historical data to help healthcare providers prepare for future surges.

### **Objective**
* **Analyze Historical Trends**: Process and visualize global infection data to identify past growth patterns and pandemic waves.
* **Implement Bayesian Forecasting**: Utilize the **Facebook Prophet** algorithm to project future case counts with high mathematical precision.
* **Predict Future Spread**: Generate a reliable 90-day predictive horizon to assist in healthcare resource planning and risk assessment.
* **Quantify Uncertainty**: Provide 95% statistical confidence intervals (uncertainty bands) to show the reliability of every prediction.
* **Interactive Monitoring**: Develop a dynamic dashboard for real-time epidemiological monitoring across different countries.

### **Dataset Description**
This project utilizes the official **WHO COVID-19 Global Daily Data**.
* **Source**: World Health Organization (WHO) Public Data Portal.
* **Key Features**: Includes `Date_reported`, `Country`, `New_cases`, `Cumulative_cases`, `New_deaths`, and `Cumulative_deaths`.
* **Scope**: Daily historical tracking from January 2020 through late November 2025.

### **Methodology / Approach**
1. **Data Preprocessing**: Converting raw WHO CSV data into a time-series format (`ds` and `y` columns) required for AI modeling.
2. **Feature Engineering**: Focusing on `Cumulative_cases` as the target variable to track the total progression of the pandemic.
3. **Algorithm Implementation**: Using **Facebook Prophet**, an additive model that handles seasonal effects, holidays, and missing data points more robustly than standard regression.
4. **Forecasting**: Training the AI on ground-truth historical data to forecast the next 90 days of spread.
5. **Validation & Visualization**: Displaying "Actual Reported Data" against "Forecasted Trends" to verify accuracy and visualize the 95% confidence interval.



### **Tools & Technologies Used**
* **Language**: Python 3.12
* **AI Engine**: Facebook Prophet (Bayesian Time-Series)
* **Frontend**: Streamlit (Web Dashboard)
* **Visualization**: Plotly Graph Objects
* **Data Handling**: Pandas & NumPy

### **Steps to Run the Project**
1. **Download Files**: Save `app.py`, `requirements.txt`, and the `WHO-COVID-19-global-daily-data.csv` file into one folder on your computer.
2. **Install Libraries**: Open your terminal in that folder and run:
   ```bash
   pip install -r requirements.txt
3. **To Launch the Website**: Open your terminal in that folder and run:
    ```bash
   streamlit run app.py
4.**Interact**:Select a country from the dropdown and click *"Generate Diagnostic Report"* to view the trends and AI predictions.

<img width="1074" height="734" alt="Screenshot 2026-01-04 at 4 40 19 PM" src="https://github.com/user-attachments/assets/47ddf92f-6669-4aa2-b21d-52bb4ebbd543" />

### **Project Link**
🚀 **Live Web App:** [https://covid-analysis-ai.streamlit.app/](https://covid-analysis-ai.streamlit.app/)
