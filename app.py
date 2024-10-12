import streamlit as st
import pandas as pd
import joblib

# Load your logistic regression model
model = joblib.load('logistic_regression.joblib')

# Streamlit app title
st.title('NBA Rookie Career Longevity Prediction App')

# Create form for user input
with st.form("prediction_form"):
    st.write("Enter the NBA Rookie's Season Statistics:")

    # Input fields for all relevant features
    gp = st.number_input('Games Played', min_value=0)
    min = st.number_input('Minutes Played', min_value=0.0, format="%.2f")
    pts = st.number_input('Points Per Game', min_value=0.0, format="%.2f")
    fgm = st.number_input('Field Goals Made', min_value=0.0, format="%.2f")
    fga = st.number_input('Field Goals Attempted', min_value=0.0, format="%.2f")
    fg_percent = st.number_input('Field Goal Percentage', min_value=0.0, max_value=100.0, format="%.2f")
    threep_made = st.number_input('3-Point Field Goals Made', min_value=0.0, format="%.2f")
    threepa = st.number_input('3-Point Field Goals Attempted', min_value=0.0, format="%.2f")
    threep_percent = st.number_input('3-Point Field Goal Percentage', min_value=0.0, max_value=100.0, format="%.2f")
    ftm = st.number_input('Free Throws Made', min_value=0.0, format="%.2f")
    fta = st.number_input('Free Throws Attempted', min_value=0.0, format="%.2f")
    ft_percent = st.number_input('Free Throw Percentage', min_value=0.0, max_value=100.0, format="%.2f")
    oreb = st.number_input('Offensive Rebounds', min_value=0.0, format="%.2f")
    dreb = st.number_input('Defensive Rebounds', min_value=0.0, format="%.2f")
    reb = st.number_input('Total Rebounds', min_value=0.0, format="%.2f")
    ast = st.number_input('Assists', min_value=0.0, format="%.2f")
    stl = st.number_input('Steals', min_value=0.0, format="%.2f")
    blk = st.number_input('Blocks', min_value=0.0, format="%.2f")
    tov = st.number_input('Turnovers', min_value=0.0, format="%.2f")

    # Form submission button
    submitted = st.form_submit_button("Predict")

    if submitted:
        # Create the DataFrame without considering the index as a feature
        input_df = pd.DataFrame([[
            gp, min, pts, fgm, fga, fg_percent, threep_made, threepa, threep_percent,
            ftm, fta, ft_percent, oreb, dreb, reb, ast, stl, blk, tov
        ]], columns=[
            'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3P Made', '3PA', '3P%', 
            'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV'
        ])


        # Attempt prediction
        try:
            prediction = model.predict(input_df)[0]
            
            if prediction == 1:
                st.success('The rookie is likely to have a successful career spanning at least 5 years!')
            else:
                st.error('The rookie might not have a very successful career lasting at least 5 years.')
        except ValueError as e:
            st.error(f'Error making prediction: {e}')