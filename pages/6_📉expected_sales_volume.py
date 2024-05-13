#Importing streamlit
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
from tensorflow import keras
from tensorflow.keras.models import load_model
from keras.models import Model
from keras.layers import Input, GRU, LSTM, SimpleRNN, Dense, Concatenate
from keras import backend as K

# from keras.model import Model
# from keras.layers import Input, GRU, LSTM, SimpleRNN, Dense, Concatenate
from keras import backend as K
import h5py



@st.cache_data
def get_modified_sales_data(allow_output_mutation = True):
    df2 = pd.read_csv('modified_sales.csv')
    return df2

dataset2 = get_modified_sales_data()

st.header("Expected sales volume")
st.markdown("By implementing machine learning using the base RNN model, we are lookikng to predict the potential sales made when user get to choose their expected change in price (discount) and the model would product the expected sales")

current_price = st.sidebar.number_input("Please enter the current price of your product that you want to apply to")
discount = st.sidebar.number_input("Please enter the percent discount you want to apply to the product")

# st.write("The current discount applied is {a}%".format(a = discount))

# Create a selection of products without the duplicates
item = dataset2['item_id'].drop_duplicates()
item = item[0: len(item.index) -7, ]

# Create the sidebar to select products from 
product_choice = st.sidebar.selectbox('Choose the item_id', item)
# Create a selection of departments without the duplicates
departments = dataset2['dept_id'].drop_duplicates()

# Create a sidebar to select departments from
department_choice = st.sidebar.selectbox('Choose the department_id', departments)


# price_elasticity_model_ind = percent_price_ind2[]

# dataset.columns = dataset2.iloc[0,]
# dataset2 = dataset2.drop(['item_id', 'dept_id'], axis = "index")
# st.dataframe(dataset2)

# #Select the row with the user selected product_id
# new_df2 = dataset2[product_choice]
# #Create a new data frame
# st.dataframe(new_df2)
# #Display the dataframe in a line chart
# st.line_chart(new_df2)
#Reading h5 file
food1 = h5py.File("FOODS_1_rnn_model.h5", 'r')

st.header("Expected sales volume")
st.markdown(" We decide to implement base RNN as our main method of machine learning. Upon inputting the expected price discount cohange on the left select box, our model will output the expected percent change in sales volume ")


#user input current change of price
#user input current price

model_to_use = '{dept_id}_rnn_model.h5'.format(dept_id = department_choice)
st.write(model_to_use)
#Input the model
rnn_model = load_model(model_to_use)

new_df = dataset2.loc[(dataset2['item_id'] == product_choice)]
st.dataframe(new_df)

#Show the model architecture
# rnn_model.summary()

#Making 2 groups
# group1 = food1['model_weights']
# group2 = food1['optimizer_weights']

# st.write(group1.keys())
# st.write(group2.keys())
# group3 = group1['top_level_model_weights']


# st.write(group3.keys())
