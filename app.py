#Importing streamlit
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
import pandas as pd
import time
import altair as alt
from vega_datasets import data


# #Reading the modified_price csv files
# df = pd.read_csv('modified_price.csv')
# #Transposing the csv files so that we can perform the data analysis
# df = df.transpose()
# #Changing the names of the columns
# df.columns = df.iloc[0,]

@st.experimental_fragment
def show_specific_products(data):
    time.sleep(1)

st.set_page_config(layout = 'wide')


st.title("FIT3164: Pricing Optimisation and Analysis")
st.header("Project Overview")
st.markdown("In the highly competitive world of retail, determining the proper price for products is a vital factor for manufacturers to ensure they are maximising their sales whilst also guaranteeing their profits. Pricing strategy is the core of a company's marketing strategy. The right pricing strategy not only has an impact on sales volume, but also plays a pivotal role in allowing companies to maximise profits, grow market share and further enhance their brand loyalty. There are multiple factors that can affect the pricing strategy of a product or service, including supply and demand of the products, pricing of competitors or whether the product itself is a necessity or not. ")
@st.cache_data
def get_modified_price_data(allow_output_mutation = True):
    df = pd.read_csv('modified_price.csv')
    df.head()
    # df = df.transpose()
    # df.columns = df.iloc[0,]
    # df = df.drop(['dept_id'], axis = 'index')
    # df = df.drop(['item_id', 'dept_id'], axis = "index")
    return df


@st.cache_data
def get_modified_sales_data(allow_output_mutation = True):
    df2 = pd.read_csv('modified_sales.csv')
    return df2


st.header("Team Member Introduction")
st.markdown("Working together as a group of four (Thanh Trung Tran, Zejinyi Liu, Shuen Y'ng Tan, Yun Gu), our group project aimed to explore the relative responsiveness of change in quantity demanded to different changes in unit price of multiple products,using  the datasets containing unit sales of different products of Walmart from Jan 2011 to April 2016. The objective is to recalibrate pricing strategies in resonance with market dynamics, thereby stimulating customer inclination to pay and enhancing overall company profitability. Thanh Trung Tran, the web developer and team leader, oversaw the project's direction and ensured seamless collaboration among team members. Zejinyi Liu, the data scientist and side project manager, focused on data analysis and modelling while also supporting project management tasks. Shuen Y'ng Tan, the project manager and side web developer, spearheaded the overall project management efforts and contributed to the web development aspects. Yun Gu, the admin and side data analyst, handled administrative tasks and supported data analysis activities alongside Zejinyi Liu.")

#Creating a text element to show we are reading the data
data_load_state = st.text('Loading data')
#Read the data
dataset = get_modified_price_data()
#Notify that the data was sucessfully loaded
data_load_state.text("Done! (using st.cache_data)")


st.subheader("Data analysis")
# st.line_chart(dataset)

# Create a selection of products without the duplicates
item = dataset['item_id'].drop_duplicates()
departments = dataset['dept_id'].drop_duplicates()

# Create the sidebar to select products from 

product_choice = st.sidebar.selectbox('Choose the item_id for price change', item)
departments_choice = st.sidebar.selectbox('Choose the department_id for price change', departments)


##################################################################
#Filtering the dataset based on the input from the users.
st.header("Individual item price analysis")
st.markdown("Something something. On the left are select box where users can choose their specific item_id in which they want to choose from. They can also choose their expected iem price change and then below will show a line graph")
# Select the rows containing the item_id of the selected item in the select box and manipulate the new rows to create a new data fram suitable to create a line graph to visualise
dataset = dataset.transpose().replace(np.nan,0)
dataset.columns = dataset.iloc[0,]
dataset = dataset.drop(['item_id', 'dept_id'], axis = "index")
#Select the row with the user selected product_id
new_df = dataset[product_choice]
#Display the dataframe in a line chart
st.line_chart(new_df)

st.markdown("Each of the line chart here display the change in price of each product in percentage in comparison to their previous week, with the first week being labeled 11101 which starts counting from Saturday 29/01/2011")

# new_df = dataset.loc[dataset['item_id'] == product_choice]
# new_df2 = new_df.transpose().replace(np.nan,0)
# a = len(new_df2.columns)

st.header("Individual item sales analysis")
st.markdown("In a similar manner, we manipulate the given datasets and aggregrate their sales based on each individual item_id and based on their respective department, and hence produce the graph showcase the percent change in sales of each product over their respective weeks")





dataset2 = get_modified_sales_data()
# Create a selection of products without the duplicates
item2 = dataset2['item_id'].drop_duplicates()
departments2 = dataset2['dept_id'].drop_duplicates()
#Create new sidebar
product_choice2 = st.sidebar.selectbox('Choose the item_id for sales change', item2)
departments_choice2 = st.sidebar.selectbox('Choose the department_id for sales change', departments2)


new_df2 = dataset2.loc[dataset2['item_id'] == product_choice2]
new_df3 = new_df2.transpose().replace(np.nan,0)
# new_df3 = new_df3[0]
#Dropping the item_id and dept_id row
new_df3 = new_df3.drop(['item_id', 'dept_id'], axis = "index")
new_df3 = new_df3.iloc[:, :1]

#Generating a linechart
st.line_chart(new_df3)

st.markdown("Each of the line chart here display the change in sales of each product in percentage in comparison to their previous week, with the first week being labeled 11101 which starts counting from Saturday 29/01/2011")


st.header()


# dataset.columns = dataset2.iloc[0,]
# dataset2 = dataset2.drop(['item_id', 'dept_id'], axis = "index")
# st.dataframe(dataset2)

# #Select the row with the user selected product_id
# new_df2 = dataset2[product_choice]
# #Create a new data frame
# st.dataframe(new_df2)
# #Display the dataframe in a line chart
# st.line_chart(new_df2)













