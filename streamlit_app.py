from collections import namedtuple
from datetime import datetime
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import json

with st.echo(code_location='below'):

    st.title('CMS for o2.cz campaigns')

    bannerTypes = ["VelkePromo", "PageImage", "MalePromo"]
    templateTypes = ["full-image", "gradient"]
    headlineStyles = ["primary", "secondary"]
    subHeadlineStyles = ["primary", "secondary"]
    
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
    templateId = item_properties['tempateId']
    templateType = item_properties['templateType']
    templateIdIndex = bannerTypes.index(templateId)
    templateTypeIndex = templateTypes.index(templateType)
    StartDate = datetime.fromtimestamp(item_properties['validFrom'])
    EndDate = datetime.fromtimestamp(item_properties['validTill'])
    texts = json.loads(item_properties['texts'])
    headlineText = texts['headlineText']
    headlineStyle = texts['headlineStyle']
    subHeadlineText = texts['subHeadlineText']
    subHeadlineStyle = texts['subHeadlineStyle']
    headlineStyleIndex = headlineStyles.index(headlineStyle)
    subHeadlineStyleIndex = subHeadlineStyles.index(subHeadlineStyle)

    st.subheader('Campaign definition')

    newCampaignId = st.text_input('Campaign Name', campaignId)

    col11, col12 = st.columns(2)
    
    with col11:
        newTempateId = st.selectbox("Banner type", pd.Series(bannerTypes), templateIdIndex)

    with col12:
        if newTempateId in ["VelkePromo", "PageImage"]:
            newTempateType = st.selectbox("Template type", pd.Series(templateTypes), templateTypeIndex)
        else:
            newTempateType = ""

    newUrlRegex = st.text_input("Targeted URIs, regex representation. [I need help.](%s)" % "https://regexr.com/", urlRegex)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        newStartDate = st.date_input("Start date", StartDate)

    with col2:
        newStartTime = st.time_input("Start time", StartDate)

    with col3:
        newEndDate = st.date_input("End date", EndDate)

    with col4:
        newEndTime = st.time_input("End time", EndDate)

    st.subheader('Texts')

    col21, col22 = st.columns(2)

    with col21:
        newHeadlineText = st.text_input('Headline Text', headlineText)
    
    with col22:
        newHeadlineStyle = st.text_input('Headline Text', pd.Series(headlineStyles), headlineStyleIndex)

    col31, col32 = st.columns(2)

    with col31:
        newSubHeadline = st.text_input('Subheadline Text', subHeadlineText)
    
    with col32:
        newSubHeadlineStyle = st.text_input('Subheadline Style', pd.Series(subHeadlineStyles), subHeadlineStyleIndex)
