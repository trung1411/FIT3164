#Importing streamlit
import streamlit as st
import altair as alt
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
# from st_pages import hide_pages

st.title("FIT3164: Pricing Optimisation and Analysis")
st.header("Project Overview")
st.markdown("In the highly competitive world of retail, determining the proper price for products is a vital factor for manufacturers to ensure they are maximising their sales whilst also guaranteeing their profits. Pricing strategy is the core of a company's marketing strategy. The right pricing strategy not only has an impact on sales volume, but also plays a pivotal role in allowing companies to maximise profits, grow market share and further enhance their brand loyalty. There are multiple factors that can affect the pricing strategy of a product or service, including supply and demand of the products, pricing of competitors or whether the product itself is a necessity or not. ")


st.header("Team Member Introduction")
st.markdown("Working together as a group of four (Thanh Trung Tran, Zejinyi Liu, Shuen Y'ng Tan, Yun Gu), our group project aimed to explore the relative responsiveness of change in quantity demanded to different changes in unit price of multiple products,using  the datasets containing unit sales of different products of Walmart from Jan 2011 to April 2016. The objective is to recalibrate pricing strategies in resonance with market dynamics, thereby stimulating customer inclination to pay and enhancing overall company profitability. Thanh Trung Tran, the web developer and team leader, oversaw the project's direction and ensured seamless collaboration among team members. Zejinyi Liu, the data scientist and side project manager, focused on data analysis and modelling while also supporting project management tasks. Shuen Y'ng Tan, the project manager and side web developer, spearheaded the overall project management efforts and contributed to the web development aspects. Yun Gu, the admin and side data analyst, handled administrative tasks and supported data analysis activities alongside Zejinyi Liu.")

st.header("Dataset Introduction")
st.markdown("Our project makes use of the M5 dataset provided by Walmart,  which constitutes a comprehensive collection of data related to the unit sales of various retail products of Walmart in the United States. It is organized into a grouped time series, encompasses a total of 3,049 unique products, further classified into three overarching product categories: Hobbies, Foods, and Household. Within these categories, there are seven product departments that provide a more granular breakdown. These products are sold across ten distinct stores situated in three different states: California (CA), Texas (TX), and Wisconsin (WI). The dataset's hierarchical structure allows for a flexible analysis, as unit sales can be aggregated at various levels, spanning from all products aggregated for all stores/states to individual product-level data. The historical data spans from January 29, 2011, to June 19, 2016, providing a maximum selling history of 1,941 days or approximately 5.4 years, with a 28-day test data period excluded.")
st.image('m5.png', caption = 'An overview of how the M5 series are organized')



# hide_pages(["login"])
if st.button("Next page"):
    st.switch_page("pages/1_📈individual_price_analysis.py")

#Adding a log out button
if st.button("Logout"):
    st.session_state["authentication_status"] = False
    st.success("Logged out!")
    sleep(0.5)
    st.switch_page("app.py")

