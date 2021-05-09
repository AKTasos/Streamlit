#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:38:47 2021

@author: aktasos
"""

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover stremalit possibilities")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df = pd.read_csv(link)

conti = st.selectbox('Select continent', df['continent'].unique())

st.write(df[df['continent']==conti])

st.header("Look at that MPG !!!")
fig1, ax1 = plt.subplots()
ax1 = sns.regplot(data = df[df['continent']==conti],
            x ='year', 
            y = 'mpg')

st.pyplot(fig1)


st.header("How much in kilograms ?")
fig2, ax2 = plt.subplots()
ax2 = sns.regplot(data = df[df['continent']==conti],
            x ='cylinders', 
            y = 'weightlbs')

st.pyplot(fig2)

st.header("Better bye some carrots to feed the horse (power)")
fig3, ax3 = plt.subplots()

ax3 = sns.regplot(data = df[df['continent']==conti],
            x ='cubicinches', 
            y = 'hp')

st.pyplot(fig3)

st.header("Check the diagonal")
viz_correlation = sns.heatmap(df[df['continent']==conti].corr(), 

								center=0,

								cmap = sns.color_palette("vlag", as_cmap=True)

								)


st.pyplot(viz_correlation.figure)