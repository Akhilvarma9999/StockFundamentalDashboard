import streamlit as st
import requests
import config
from iex import IEXStock
from helper import format_number

symbol = st.sidebar.text_input("Symbol",value="MSFT")
stock=IEXStock(config.IEX_API_TOKEN,symbol)

screen = st.sidebar.selectbox("view",('Overview','Fundamentals','News','Ownership','Technicals'))
st.title(screen)



if screen == "Overview":
    logo =stock.get_logo()
    company_info=stock.get_company_info()
    print(company_info)
    

    if company_info and isinstance(company_info, list) and len(company_info) > 0:
    # Access the first item in the list
        info = company_info[0]

        col1, col2 = st.columns([1, 4])
        with col1:
            # Assuming 'logo' contains 'url' directly
            if 'url' in logo:
                st.image(logo['url'])
            else:
                st.error("Logo URL not found")
        with col2:
            st.subheader("Description")
            st.write(info.get('longDescription', 'Description not available'))

            st.subheader("Industry")
            st.write(info.get('industry', 'Industry not available'))

            st.subheader("CEO")
            st.write(info.get('ceo', 'CEO not available'))
    else:
        st.error("company_info is not a list or it's empty")


    
  
if screen == "Fundamentals":
    stats=stock.get_stats()
    if stats and isinstance(stats, list):
        # Find the dictionary that contains 'currentCash' and 'reportDate' keys
        stats_info = stats[0] if stats and isinstance(stats[0], dict) else {}

        st.subheader("CurrentCash")
        st.write(format_number(stats_info.get("currentCash", "CurrentCash not available")))

        st.subheader("ReportedDate")
        st.write(stats_info.get("reportDate", "ReportedDate not available"))
        st.write(stats_info)
    else:
        st.error("stats is not a list or it's empty")

    