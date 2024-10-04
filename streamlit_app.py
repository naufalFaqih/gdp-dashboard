import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

data = pd.read_csv("https://raw.githubusercontent.com/naufalFaqih/dashboard/refs/heads/master/day.csv")

st.title("Bike Rental Dashboard :sparkles:")
st.subheader('Daily Rental')

col1,col2 = st.columns(2)
with col1:
    working_day_rent = data[data['workingday'] == 1]
    total_rent = working_day_rent['cnt'].sum()
    st.metric("total rental at working day", value=total_rent)
    
with col2:
    holiday_rent = data[data['holiday'] == 1]
    total_rent_holiday = holiday_rent['cnt'].sum()
    st.metric("total rental at holiday", value = total_rent_holiday)

data_ten_day = data.head(10)
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
    data_ten_day['dteday'],
    data_ten_day['cnt'],
    marker='o',
    linewidth = 2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

st.subheader("Casual vs Registered at working day")
col1,col2 = st.columns(2)
with col1:
    working_day_casual = data[data['workingday'] == 1]
    total_rent = working_day_casual['casual'].sum()
    st.metric("total casual at working day", value=total_rent)
    
with col2:
    working_day_registered = data[data['workingday'] == 1]
    total_rent_registered = working_day_registered['registered'].sum()
    st.metric("total registered at working day", value = total_rent_registered)

workingday_data = data[data['workingday'] == 1]

# Hitung total penyewaan casual dan registered pada hari kerja
total_casual = workingday_data['casual'].sum()
total_registered = workingday_data['registered'].sum()

# Data untuk visualisasi
categories = ['Casual', 'Registered']
values = [total_casual, total_registered]

# Membuat plot bar
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, values, color=["#D3D3D3", '#FFB74D'])

# Menambahkan label dan judul
ax.set_title("Total Rent At Working day", fontsize=18)
ax.set_ylabel(None)

# Menampilkan plot pada Streamlit
st.pyplot(fig)

st.subheader("Casual vs Registered at holiday")
col1,col2 = st.columns(2)
with col1:
    working_day_casual = data[data['holiday'] == 1]
    total_rent = working_day_casual['casual'].sum()
    st.metric("total casual at holiday", value=total_rent)
    
with col2:
    working_day_registered = data[data['holiday'] == 1]
    total_rent_registered = working_day_registered['registered'].sum()
    st.metric("total registered at holiday", value = total_rent_registered)

holiday_data = data[data['holiday'] == 1]

# Hitung total penyewaan casual dan registered pada hari kerja
total_casual = holiday_data['casual'].sum()
total_registered = holiday_data['registered'].sum()

# Data untuk visualisasi
categories = ['Casual', 'Registered']
values = [total_casual, total_registered]

# Membuat plot bar
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(categories, values, color=["#D3D3D3", '#FFB74D'])

# Menambahkan label dan judul
ax.set_title("Total Rent At Holiday", fontsize=18)
ax.set_ylabel(None)

# Menampilkan plot pada Streamlit
st.pyplot(fig)

st.subheader('Effect of Weather Conditions on Bike Rentals')
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, ax=ax)
st.pyplot(fig)