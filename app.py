import pickle
import pandas as pd

import  streamlit as st
import pandas as pd
import numpy as np
from joblib import dump, load
import pickle
st.title('IPL Win Predictor')
st.write('This app predicts the win probability of a team in IPL based on the team' )
st.write('The data used for this app is from the IPL 2008 - 2024')
teams=['Royal Challengers Bangalore',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Delhi Capitals',
 'Sunrisers Hyderabad',
 'Punjab Kings']
ciies=['Chennai', 'Rajkot', 'Ahmedabad', 'Delhi', 'Kolkata', 'Pune',
       'Bloemfontein', 'Mumbai', 'Abu Dhabi', 'Bangalore', 'Bengaluru',
       'Chandigarh', 'Hyderabad', 'Dharamsala', 'Jaipur', 'Durban',
       'Cape Town', 'Visakhapatnam', 'Kimberley', 'Lucknow', 'Cuttack',
       'Johannesburg', 'Navi Mumbai', 'Port Elizabeth', 'Ranchi',
       'Mohali', 'East London', 'Indore', 'Dubai', 'Nagpur', 'Centurion',
       'Sharjah', 'Raipur', 'Guwahati', 'Kanpur']
model=load('model_new.joblib.')
col1, col2 = st.columns(2)
batting_team = col1.selectbox('select the batting team',sorted(teams))
bowling_team = col2.selectbox('select the bowling team',sorted(teams))
selected_city = st.selectbox('select the city',sorted(ciies))
target = st.number_input('Enter the target runs',min_value=0, max_value=350, value=0)
col3,col4,col5=st.columns(3)
with col3:
       score=st.number_input('Enter the score',min_value=0, max_value=350, value=0)
with col4:
       wickets=st.number_input('Enter the wickets',min_value=0, max_value=10, value=0)
with col5:
       overs=st.number_input('Enter the overs',min_value=0, max_value=20, value=0)
if st.button('Predict'):
       runs_left=target-score
       balls_left=120-(overs*6)
       wickets_left=10-wickets
       crr=score/overs
       rrr=(runs_left*6)/balls_left
       input_df=pd.DataFrame({
              'batting_team':[batting_team],
              'bowling_team':[bowling_team],
              'city':[selected_city],
              'runs_left': [runs_left],
              'balls_left': [balls_left],
              'wickets': [wickets_left],
              'total_runs_x':[target],
              'crr':[crr],
              'rrr':[rrr]

       })
       result=model.predict_proba(input_df)
       loss=result[0][0]
       win=result[0][1]
       col6,col7=st.columns(2)
       with col6:
              st.header(batting_team)
              st.header(str(round(win*100) )+ '%')
       with col7:
              st.header(bowling_team)
              st.header(str(round(loss*100) )+ '%')
       st.text('The model is trained on the IPL data from 2008-2024')






