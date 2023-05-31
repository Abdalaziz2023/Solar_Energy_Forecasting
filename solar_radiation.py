import streamlit as st
from streamlit_timeline import timeline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def main_page():
    st.image("img2.jpg")
    st.markdown("# About The project")
    st.markdown("Predict radiation intensity under certain atmospheric conditions.\nAnd predict the output of solar panels in a certain period of time")

def page2():
    st.markdown("# Solar energy ❄️")
    st.image("img1.jpg")

    # uploaded_files = st.file_uploader("Choose a CSV file")
    # st.write(uploaded_files)
    
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        from datetime import time
        
        appointment = st.slider("Schedule your appointment:",value=(time(0,0), time(23, 59)))

        starth = str(appointment[0])[:2]
        st.write("start Time",starth)
        endh = str(appointment[-1])[:2]
        st.write("End Time",endh)
      
        
        option = st.selectbox('Select month',('5','6'))
        
        

        btn1 = st.button("Read_Data")
        if btn1:
            df = pd.read_csv(uploaded_file)
            df.groupby(['MONTH'])
            
            df = df[df['MONTH'] == int(option)]
            df = df[df['HOURS'].between(endh,starth,inclusive=False)]
            
            st.table(df.drop(df[["AC_POWER","DATE_TIME",'Unnamed: 0','DC_POWER','DAILY_YIELD','TOTAL_YIELD','TIME','DATE_STRING','SOURCE_KEY_NUMBER','DATE','DAY','WEEK','MINUTES','TOTAL MINUTES PASS']],axis=1))
            
            
    else:
        st.error("Pleas load file first")

    btn = st.button("Forcasting")

    if btn:
        
        if uploaded_file:
            df2 = pd.read_csv(uploaded_file)
            
            df2 = df2[df2['MONTH'] == int(option)]
            df2 = df2[df2['HOURS'] == int(starth)]
            
            X = df2[['DAILY_YIELD','TOTAL_YIELD','AMBIENT_TEMPERATURE','MODULE_TEMPERATURE','IRRADIATION','DC_POWER']]
            y = df2['AC_POWER']
            from sklearn.model_selection import train_test_split
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=21)
            import joblib
            loaded_model = joblib.load("DecisionTreeRegressorModel_solar.joblib")
            st.subheader("AC power")
            st.table(loaded_model.predict(X_test))
        else:
            st.error("Pleas load file first")
            
            
        


    
def page3():
    st.markdown("""
    <style>
    div.stButton > button:first-child {
    background-color: #0099ff;
    color:#000000;
    }
    div.stButton > button:hover {
    background-color: #A9A9A9;
    color:#00008B;
    }
    </style>
    
    
    """,unsafe_allow_html= True)

    st.image("img3.png")
    st.markdown("# Solar Raditaion")
    option = st.selectbox('Month',[9,10,11,12])
    day = st.slider("Start Date",value=(0,30),max_value=30)
    start = day[0]
    End = day[-1]
    
    st.write(str(start))
    st.write(str(End))
    
    df9 = pd.read_csv("Meandatasetofmonth9.csv").drop("Radiation",axis=1)
    df10 = pd.read_csv("Meandatasetofmonth10.csv").drop("Radiation",axis=1)
    df11 = pd.read_csv("Meandatasetofmonth11.csv").drop("Radiation",axis=1)
    df12 = pd.read_csv("Meandatasetofmonth12.csv").drop("Radiation",axis=1)
    
    #======================================================================
    df9 = df9[df9['Day'].between(start, End, inclusive=False)]
    df10 = df10[df10['Day'].between(start, End, inclusive=False)]
    df11 = df11[df11['Day'].between(start, End, inclusive=False)]
    df12 = df12[df12['Day'].between(start, End, inclusive=False)]


    

    def prediction():
        import numpy as np
        import pandas as pd
        import re
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import train_test_split
        import optuna
        import xgboost as xgb
        import joblib

        data = pd.read_csv("SolarPrediction.csv")
        data['Month'] = data['Data'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
        data['Day'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\/)', x).group(0)).astype(np.int)
        data['Year'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\s)', x).group(0)).astype(np.int)
        data = data.drop('Data', axis=1)

        data['Hour'] = data['Time'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
        data['Minute'] = data['Time'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)
        data['Second'] = data['Time'].apply(lambda x: re.search(r'\d+$', x).group(0)).astype(np.int)

        data = data.drop('Time', axis=1)

        data['SunriseHour'] = data['TimeSunRise'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
        data['SunriseMinute'] = data['TimeSunRise'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

        data['SunsetHour'] = data['TimeSunSet'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
        data['SunsetMinute'] = data['TimeSunSet'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

        data = data.drop(['TimeSunRise', 'TimeSunSet'], axis=1)

        data = data.drop(['Year', 'SunriseHour'], axis=1)
        data = data[data["Month"] == option]
        data = data[data["Day"].between(start,End,inclusive=False)]

        y = data['Radiation'].copy()
        X = data.drop('Radiation', axis=1).copy()
        x = X
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
     

        dtest = xgb.DMatrix(X,label = y)

        loaded_model = joblib.load("complite_model.joblib")
        predicted = loaded_model.predict(dtest)
        x['Predicted_Radiation'] = predicted
        x = x.drop(['UNIXTime','SunriseMinute','SunsetHour','SunsetMinute'], axis=1)
        st.table(x.reset_index(drop=True))

    bt = st.button("Show Data")
    if bt:
        if option == 9:
            st.table(df9)
        elif option == 10:
            st.table(df10)
        elif option == 11:
            st.table(df11)
        elif option == 12:
            st.table(df10)

    btchart = st.button("Show plot Radiation and Temperature")

    if btchart:
        if option == 9:
            fig = plt.figure()
            plt.stem(df9["Day"],df9["Temperature"])
            plt.xlabel("Days")
            plt.ylabel("Temperature")
            st.pyplot(fig)
            
        elif option == 10:
            fig = plt.figure()
            plt.stem(df10["Day"],df10["Temperature"])
            plt.xlabel("Days")
            plt.ylabel("Temperature")
            st.pyplot(fig)
        elif option == 11:
            fig = plt.figure()
            plt.stem(df11["Day"],df11["Temperature"])
            plt.xlabel("Days")
            plt.ylabel("Temperature")
            st.pyplot(fig)
        elif option == 12:
            fig = plt.figure()
            plt.stem(df12["Day"],df12["Temperature"])
            plt.xlabel("Days")
            plt.ylabel("Temperature")
            st.pyplot(fig)
    
    

    predict = st.button('Forcasting')
    if predict:
        prediction()

def new_func(day):
    st.write(day)





        



def sidebar():    
    page_names_to_funcs = {
        "Main Page": main_page,
        "Solar energy Prediction": page2,
        "Solar Radiation Forcasting": page3,
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()


sidebar()