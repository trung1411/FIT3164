#Importing streamlit
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
import pandas as pd
import time
import altair as alt


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
def get_modified_sales_data(experimental_allow_widgets = True):
    df = pd.read_csv('modified_price.csv')
    df.head()
    # df = df.transpose()
    # df.columns = df.iloc[0,]
    # df = df.drop(['dept_id'], axis = 'index')
    # df = df.drop(['item_id', 'dept_id'], axis = "index")
    return df


st.header("Team Member Introduction")
st.markdown("Working together as a group of four (Thanh Trung Tran, Zejinyi Liu, Shuen Y'ng Tan, Yun Gu), our group project aimed to explore the relative responsiveness of change in quantity demanded to different changes in unit price of multiple products,using  the datasets containing unit sales of different products of Walmart from Jan 2011 to April 2016. The objective is to recalibrate pricing strategies in resonance with market dynamics, thereby stimulating customer inclination to pay and enhancing overall company profitability. Thanh Trung Tran, the web developer and team leader, oversaw the project's direction and ensured seamless collaboration among team members. Zejinyi Liu, the data scientist and side project manager, focused on data analysis and modelling while also supporting project management tasks. Shuen Y'ng Tan, the project manager and side web developer, spearheaded the overall project management efforts and contributed to the web development aspects. Yun Gu, the admin and side data analyst, handled administrative tasks and supported data analysis activities alongside Zejinyi Liu.")

#Creating a text element to show we are reading the data
data_load_state = st.text('Loading data')
#Read the data
dataset = get_modified_sales_data()
#Notify that the data was sucessfully loaded
data_load_state.text("Done! (using st.cache_data)")


st.subheader("Data analysis")
st.write("And here is the raw data")
st.dataframe(dataset)
# st.line_chart(dataset)

# Create a selection of products without the duplicates
item = dataset['item_id'].drop_duplicates()
departments = dataset['dept_id'].drop_duplicates()

# Create the sidebar to select products from 

product_choice = st.sidebar.selectbox('Choose the item_Id', item)
departments_choice = st.sidebar.selectbox('Choose the department_id', departments)


#Filtering the dataset based on the input from the users.
st.header("Individual item analysis")
st.markdown("Something something. On the left are select box where users can choose their specific item_id in which they want to choose from. They can also choose their expected iem price change and then below will show a line graph")


# Select the rows containing the item_id of the selected item in the select box and manipulate the new rows to create a new data fram suitable to create a line graph to visualise
new_df = dataset.loc[dataset['item_id'] == product_choice]
new_df = new_df.transpose().replace(np.nan,0)
new_df.columns = new_df.iloc[0,]
# new_df = df.drop(['dept_id'], axis = 'index')
new_df = new_df.drop(['item_id', 'dept_id'], axis = "index")
#Changing the first column name to weeks

st.dataframe(new_df)

# st.vega_lite_chart(new_df,{
#     "mark": {"type:" "line"},
#             "enconding":{

#             "y": {"field": product_choice, "type": "quantitative"}
#     } },)
# st.line_chart(new_df)

chart = (alt.Chart(
    data = new_df,
    title = "Percent change in price of different products over the weeks",
    ).mark_line(

    ))

st.altair_chart(chart)

# st.altair_chart(c, use_container_width= True)


#graphs = st.line_chart(dataset[,products])











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




