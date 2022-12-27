from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

with st.echo(code_location='below'):
    
    url = "https://httpbin.org/post"
 
    headers = {"Content-Type": "application/json; charset=utf-8"}
 
    data = {
        "id": 1001,
        "name": "geek",
        "passion": "coding",
    }
 
    response = requests.post(url, headers=headers, json=data)

    st.write("JSON Response ", response.json())
