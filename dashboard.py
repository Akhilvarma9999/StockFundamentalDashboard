import streamlit as st
import requests
import config


symbol = st.sidebar.text_input("Symbol",value="MSFT")

screen = st.sidebar.selectbox("view",('Overview','Fundamentals','News','Ownership','Technicals'))
st.title(screen)



if screen == "Overview":
    url=f"https://api.iex.cloud/v1/stock/{symbol}/logo?token={config.IEX_API_TOKEN}"
    r=requests.get(url)
    logo=r.json()
    

    url=f"https://api.iex.cloud/v1/data/core/company/{symbol}?token={config.IEX_API_TOKEN}"
    r=requests.get(url)
    response_json=r.json()
    

    col1 ,col2 =st.columns([1,4])
    with col1:
        st.image(logo['url'])
    with col2:
        
        st.subheader("Description")
        st.write(response_json['description'])
        st.subheader("Industry")
        st.write(response_json['industry'])
        st.subheader("CEO")
        st.write(response_json['CEO'])


    
  
if screen == "Fundamentals":
    pass
    