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
    buttonStyles = ["primary", "secondary", "neutral"]
    buttonActions = ["url", "none"]
    
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
    buttons = json.loads(item_properties['buttons'])
    buttonsNumber = str(len(buttons))
    button1Text = buttons[0]['buttonText']
    button1Style = buttons[0]['buttonStyle']
    button1StyleIndex = buttonStyles.index(button1Style)
    button1Action = buttons[0]['buttonAction']
    button1ActionIndex = buttonActions.index(button1Action)
    button1Url = buttons[0]['buttonUrl']
    button1Tag = buttons[0]['buttonTag']
    if len(buttons) == 2:
        button2Text = buttons[1]['buttonText']
        button2Style = buttons[1]['buttonStyle']
        button2StyleIndex = buttonStyles.index(button2Style)
        button2Action = buttons[1]['buttonAction']
        button2ActionIndex = buttonActions.index(button2Action)
        button2Url = buttons[1]['buttonUrl']
        button2Tag = buttons[1]['buttonTag']
    else:
        button2Text = ""
        button2Style = ""
        button2StyleIndex = "primary"
        button2Action = buttons[1]['buttonAction']
        button2ActionIndex = "url"
        button2Url = ""
        button2Tag = "_ic="

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
        newHeadlineStyle = st.selectbox('Headline Style', pd.Series(headlineStyles), headlineStyleIndex)

    col31, col32 = st.columns(2)

    with col31:
        newSubHeadline = st.text_input('Subheadline Text', subHeadlineText)
    
    with col32:
        newSubHeadlineStyle = st.selectbox('Subheadline Style', pd.Series(subHeadlineStyles), subHeadlineStyleIndex)
    
    st.subheader('Buttons')

    newButtonNumber = st.select_slider('Number of buttons',["1", "2"], buttonsNumber)

    col41, col42 = st.columns(2)

    with col41:
        st.text("Button 1")
        newButton1Text = st.text_input('Button Text', button1Text)
        newButton1Style = st.selectbox('Button Style', pd.Series(buttonStyles), button1StyleIndex)
        newButton1Action = st.selectbox('Button Action', pd.Series(buttonActions), button1ActionIndex)
        newButton1Url = st.text_input('Button URL', button1Url)
        newButton1Tag = st.text_input('Button Tag', button1Tag)

    with col42:
        if newButtonNumber == "2":
            st.text("Button 2")
            newButton2Text = st.text_input('Button Text', button2Text)
            newButton2Style = st.selectbox('Button Style', pd.Series(buttonStyles), button2StyleIndex)
            newButton2Action = st.selectbox('Button Action', pd.Series(buttonActions), button2ActionIndex)
            newButton2Url = st.text_input('Button URL', button2Url)
            newButton2Tag = st.text_input('Button Tag', button2Tag)
