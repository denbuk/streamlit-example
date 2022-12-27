from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

with st.echo(code_location='below'):

    st.title('CMS for o2.cz campaigns')

    bannerTypes = ["VelkePromo", "PageImage", "MalePromo"]
    
    url = "https://api-exponea.o2.sk/data/v2/projects/5851ab46-b9d8-11e9-beef-92ec88286fd6/catalogs/63aae549778d423d3db4e841/items"
 
    headers = {"Authorization": "Basic azdsd2NlcXAxMm8wb3B5bHRwa29hd2J0emRqMHhzc2xjN3VkdHBjcmozcHA4dXI3YzJvYTEwcDJvbGdlamVnYjo5amdpc3ZobWtjaHRsNGJha2xiNXlya3VyOTRoN2MxOHplMnd5bGYxdGpwamJuYzRoenBoMmR5aDhudGxib3Vl","Content-Type": "application/json"}
 
    data = {"properties": 
	  {
	  	
	  }
    }
 
    #response = requests.put(url, headers=headers, json=data)
    response = requests.get(url, headers=headers)

    resp = response.json()
    items_list = resp.get("data")
    items_ids = []
    st.write(items_list)

    for x in items_list:
        items_ids.append(x['item_id'])

    campaign_option = st.selectbox("Campaign Code (campaign_id)", pd.Series(items_ids))

    index = items_ids.index(campaign_option)
    item_id = items_ids[index]
    item_properties = items_list[index]['properties']
    campaignId = item_properties['campaignId']
    urlRegex = item_properties['urlRegex']
    tempateId = item_properties['templateId']
    templateIdIndex = bannerTypes.index(tempateId)

    st.subheader('Campaign definition')

    newCampaignId = st.text_input('Campaign Name', campaignId)

    newUrlRegex = st.text_input("Targeted URIs, regex representation. [I need help.](%s)" % "https://regexr.com/", urlRegex)

    newTempateId = st.selectbox("Banner type", pd.Series(bannerTypes), templateIdIndex)
