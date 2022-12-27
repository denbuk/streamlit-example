from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

with st.echo(code_location='below'):
    
    url = "https://api-exponea.o2.sk/data/v2/projects/5851ab46-b9d8-11e9-beef-92ec88286fd6/catalogs/63aae549778d423d3db4e841/items/XXXXX"
 
    headers = {"Authorization": "Basic azdsd2NlcXAxMm8wb3B5bHRwa29hd2J0emRqMHhzc2xjN3VkdHBjcmozcHA4dXI3YzJvYTEwcDJvbGdlamVnYjo5amdpc3ZobWtjaHRsNGJha2xiNXlya3VyOTRoN2MxOHplMnd5bGYxdGpwamJuYzRoenBoMmR5aDhudGxib3Vl","Content-Type": "application/json"}
 
    data = {"properties": 
	  {
	  	"b": '[{"template":"Eshop","template_variant":"half_image_desktop","scenario_id":"samsung_cerven","position":"1","cta_img":"https://www.o2.cz/servis/exponea-images/2022-01-q1/1200x224-samsung?field=data&_linka=a336439","product_image1":"https://storage.googleapis.com/otu-app-storage/5851ab46-b9d8-11e9-beef-92ec88286fd6/media/original/ffaaa35a-e1be-11ec-8f0f-9a6487c53521","product_position1":"LEFT","product_image2":"","product_position2":"","tab_text":"Samsung se slevou 1 000 Kč","headline":"Sleva 1 000 Kč na Samsung","description":"<b>Pořiďte si třeba Samsung Galaxy A33 5G</b>","price":"","crossedPrice":"","headline_color":"LIGHT","cta_text1":"Chci telefon","landing1":"https://www.o2.cz/telefony-a-zarizeni/produkt/samsung-galaxy-a33-5g-128gb-cerna?_ic=exp-pi-o2cz-ohw-hw_cerven-2022/06/01-zkp","landing1_new_tab":false,"cta_color1":"GREEN","cta_text2":"","landing2":"","cta_color2":""}]',
	  }
    }
 
    response = requests.put(url, headers=headers, json=data)

    st.write("JSON Response ", response.json())
