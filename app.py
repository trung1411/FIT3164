#Importing streamlit
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as slt
import pandas as pd
import time

#Reading the modified_price csv files
df = pd.read_csv('modified_price.csv')
#Transposing the csv files so that we can perform the data analysis
df = df.transpose()
#Changing the names of the columns
df.columns = df.iloc[0,]


@st.cache_data
def get_data():
    calendar = pd.read_csv('calendar.csv')
    calendar.head()
    st.line_chart(calendar)


@st.experimental_fragment
def show_specific_products(data):
    time.sleep(1)

st.set_page_config(layout = 'wide')




# df.head()
# new_df = df.drop(['item_id', 'dept_id'], axis = "index")
# new_df.head()
# new_df.plot()
# plt.show()





# a = 0
# item = df.iloc[0,:].to_frame()
# item.head()

# item.drop(['dept_id'])
# # Change data point in the data frame to float to draw visualisaitons
# print(item)
# item.iloc[[2:],].plot()




