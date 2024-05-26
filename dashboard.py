import streamlit as st
import requests, redis
import config, json
from iex import IEXStock
from helper import format_number
from datetime import timedelta,datetime

redis_client = redis.Redis(host='localhost', port=6379, db=0)

symbol = st.sidebar.text_input("Symbol",value="MSFT")
stock=IEXStock(config.IEX_API_TOKEN,symbol)

screen = st.sidebar.selectbox("view",('Overview','Fundamentals','News','Ownership','Technicals'))
st.title(screen)



if screen == "Overview":
    logo_key=f"{symbol}_logo"
    logo = redis_client.get(logo_key)
    if logo is None:
        print("could not find logo in cache,retreving from IEX cloud")
        logo =stock.get_logo()
        redis_client.set(logo_key,json.dumps(logo))
    else:
        print("Found logo in Cache,serving from redis")
        logo=json.loads(logo)
    

    company_key = f"{symbol}_compnay"
    company = redis_client.get(company_key)
    if company is None:
        print("getting info from IEX Cloud")
        company=stock.get_company_info()
        if company:
            redis_client.set(company_key,json.dumps(company))
            redis_client.expire(company_key,timedelta(seconds=30))
        else :
            print("Error retrieving company info from IEX Cloud")
            company = []
    else:    
        print("getting info from cache")
        company = json.loads(company)
    
    
    
        
    if company and isinstance(company, list) and len(company) > 0:
        # Access the first item in the list
            info = company[0]

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

    