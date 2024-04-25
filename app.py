#Importing streamlit
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from datetime import date, timedelta
import pandas as pd
import time

# #Reading the modified_price csv files
# df = pd.read_csv('modified_price.csv')
# #Transposing the csv files so that we can perform the data analysis
# df = df.transpose()
# #Changing the names of the columns
# df.columns = df.iloc[0,]

st.title("FIT3164: Pricing Optimisation and Analysis")
st.header("Project Overview")
st.write("In the highly competitive world of retail, determining the proper price for products is a vital factor for manufacturers to ensure they are maximising their sales whilst also guaranteeing their profits. Pricing strategy is the core of a company's marketing strategy. The right pricing strategy not only has an impact on sales volume, but also plays a pivotal role in allowing companies to maximise profits, grow market share and further enhance their brand loyalty. There are multiple factors that can affect the pricing strategy of a product or service, including supply and demand of the products, pricing of competitors or whether the product itself is a necessity or not. ")
@st.cache_data
def get_data(experimental_allow_widgets = True):
    df = pd.read_csv('modified_price.csv')
    df.head()
    df.transpose()
    df.columns = df.iloc[0,]
    return df


#Creating a text element to show we are reading the data
data_load_state = st.text('Loading data')
#Read the data
dataset = get_data()
#Notify that the data was sucessfully loaded
data_load_state.text("Done! (using st.cache_data)")


st.subheader("Data analysis")
st.write("And here is the raw data")
st.dataframe(dataset)


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




