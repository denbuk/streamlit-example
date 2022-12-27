from collections import namedtuple
from datetime import datetime
from PIL import Image
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
    backgroundGradientStyles = ["primary", "secondary"]
    
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
    #st.write(items_list)

    for x in items_list:
        items_ids.append(x['item_id'])

    campaign_option = st.selectbox("Campaign Code (campaign_id)", pd.Series(items_ids))

    index = items_ids.index(campaign_option)
    item_id = items_ids[index]
    item_properties = items_list[index]['properties']
    campaignId = item_properties['campaignId']
    urlRegex = item_properties['urlRegex']
    internalUsers = item_properties['userInternal']
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
        button2Style = "primary"
        button2StyleIndex = buttonStyles.index(button2Style)
        button2Action = "url"
        button2ActionIndex = buttonActions.index(button2Action)
        button2Url = ""
        button2Tag = "_ic="
    images = json.loads(item_properties['images'])
    backgroundImageS = images['backgroundImageS']
    backgroundImageM = images['backgroundImageM']
    backgroundImageL = images['backgroundImageL']
    backgroundImageXL = images['backgroundImageXL']
    backgroundGradient = images['backgroundGradient']
    backgroundGradientIndex = backgroundGradientStyles.index(backgroundGradient)
    imageGradient = images['imageGradient']
    imageAlt = images['imageAlt']

    st.subheader('Campaign definition')

    newCampaignId = st.text_input('Campaign Name', campaignId)

    col11, col12, col13 = st.columns(3)
    
    with col11:
        newTempateId = st.selectbox("Banner type", pd.Series(bannerTypes), templateIdIndex)

    with col12:
        if newTempateId in ["VelkePromo", "PageImage"]:
            newTempateType = st.selectbox("Template type", pd.Series(templateTypes), templateTypeIndex)
        else:
            newTempateType = ""
    
    with col13:
        newInternalUsers = st.checkbox('Seen by internal users', internalUsers)

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
        newButton1Text = st.text_input('Button 1 Text', button1Text)
        newButton1Style = st.selectbox('Button 1 Style', pd.Series(buttonStyles), button1StyleIndex)
        newButton1Action = st.selectbox('Button 1 Action', pd.Series(buttonActions), button1ActionIndex)
        newButton1Url = st.text_input('Button 1 URL', button1Url)
        newButton1Tag = st.text_input("Button 1 Tag [I need to create a tag.](%s)" % "https://regexr.com/", button1Tag)

    with col42:
        if newButtonNumber == "2":
            st.text("Button 2")
            newButton2Text = st.text_input('Button 2 Text', button2Text)
            newButton2Style = st.selectbox('Button 2 Style', pd.Series(buttonStyles), button2StyleIndex)
            newButton2Action = st.selectbox('Button 2 Action', pd.Series(buttonActions), button2ActionIndex)
            newButton2Url = st.text_input('Button 2 URL', button2Url)
            newButton2Tag = st.text_input("Button 2 Tag [I need to create a tag.](%s)" % "https://regexr.com/", button2Tag)
    
    st.subheader('Images')

    if newTempateType == "gradient":
        newImageAlt = st.text_input('Image Alt', imageAlt)
        showImages = st.checkbox('Show images', False)
        col51, col52 = st.columns(2)
        with col51:
            newBackgroundGradient = st.selectbox('Background Gradient', pd.Series(backgroundGradientStyles), backgroundGradientIndex)
        with col52:
            newImageGradient = st.text_input('Image Gradient', imageGradient)
            if showImages == True:
                st.image(newImageGradient, caption='Image Gradient')
    elif newTempateType == "full-image":
        newImageAlt = st.text_input('Image Alt', imageAlt)
        showImages = st.checkbox('Show images', False)
        col51, col52, col53, col54 = st.columns(4)
        with col51:
            newbackgroundImageS = st.text_input('Background Image S', backgroundImageS)
            if showImages == True:
                st.image(newbackgroundImageS, caption='Image S')
        with col52:
            newbackgroundImageM = st.text_input('Background Image M', backgroundImageM)
            if showImages == True:
                st.image(newbackgroundImageM, caption='Image M')
        with col53:
            newbackgroundImageL = st.text_input('Background Image L', backgroundImageL)
            if showImages == True:
                st.image(newbackgroundImageL, caption='Image L')
        with col54:
            newbackgroundImageXL = st.text_input('Background Image XL', backgroundImageXL)
            if showImages == True:
                st.image(newbackgroundImageXL, caption='Image XL')
    else:
        newImageAlt = st.text_input('Image Alt', imageAlt)
        showImages = st.checkbox('Show images', False)
        newbackgroundImageS = st.text_input('Background Image S', backgroundImageS)
        if showImages == True:
                st.image(newbackgroundImageS, caption='Image S')


