from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

Ahoj O2.

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    
    url = "https://httpbin.org/post"
 
    headers = {"Content-Type": "application/json; charset=utf-8"}
 
    data = {
        "id": 1001,
        "name": "geek",
        "passion": "coding",
    }
 
    response = requests.post(url, headers=headers, json=data)
    
    st.write(response)
