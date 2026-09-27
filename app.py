import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Brand
company = st.selectbox(
    'Brand',
    df['Company'].unique()
)

# Type of laptop
type = st.selectbox(
    'Type',
    df['TypeName'].unique()
)

# RAM
ram = st.selectbox(
    'RAM(in GB)',
    [2, 4, 6, 8, 12, 16, 24, 32, 64]
)

# Weight
weight = st.number_input(
    'Weight of the Laptop'
)

# Touchscreen
touchscreen = st.selectbox(
    'Touchscreen',
    ['No', 'Yes']
)

# IPS
ips = st.selectbox(
    'IPS',
    ['No', 'Yes']
)

# Screen size
screen_size = st.slider(
    'Screen size in inches',
    10.0,
    18.0,
    13.0
)

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    [
        '1920x1080',
        '1366x768',
        '1600x900',
        '3840x2160',
        '3200x1800',
        '2880x1800',
        '2560x1600',
        '2560x1440',
        '2304x1440'
    ]
)

# CPU
cpu = st.selectbox(
    'CPU',
    df['Cpu brand'].unique()
)

# HDD
hdd = st.selectbox(
    'HDD(in GB)',
    [0, 128, 256, 512, 1024, 2048]
)

# SSD
ssd = st.selectbox(
    'SSD(in GB)',
    [0, 8, 128, 256, 512, 1024]
)

# GPU
gpu = st.selectbox(
    'GPU',
    df['Gpu brand'].unique()
)

# OS
os = st.selectbox(
    'OS',
    df['os'].unique()
)


if st.button('Predict Price'):

    # Touchscreen
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    # IPS
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    # Resolution ko X aur Y mein divide karna
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])

    # PPI calculate karna
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # Query DataFrame
    query = pd.DataFrame({
        'Company': [company],
        'TypeName': [type],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'Cpu brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu brand': [gpu],
        'os': [os]
    })

    # Prediction
    prediction = pipe.predict(query)[0]

    # Original price because model was trained on log price
    prediction = np.exp(prediction)

    st.title(
        "The predicted price of this configuration is "
        + str(int(prediction))
    )