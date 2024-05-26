import requests

class IEXStock:
    def __init__(self,token,symbol):
        self.BASE_URL = 'https://api.iex.cloud/v1/data/core'
        self.token = token
        self.symbol = symbol
    def get_logo(self):
        url=f"https://api.iex.cloud/v1/stock/{self.symbol}/logo?token={self.token}"
        r=requests.get(url)
        return r.json()
    def get_company_info(self):
        url=f"{self.BASE_URL}/company/{self.symbol}?token={self.token}"
        r=requests.get(url)
        return r.json()
    def get_stats(self):
        url=f"{self.BASE_URL}/balance_sheet/{self.symbol}?token={self.token}"
        r=requests.get(url)
        return r.json()
    def get_company_news(self, last=10):
        url = f"{self.BASE_URL}/news/{self.symbol}?range=last-week&token={self.token}"
        r = requests.get(url)
        
        return r.json()
    def get_fundamentals(self, period='quarterly', last=4):
        url = f"{self.BASE_URL}/fundamentals/{self.symbol}/{period}?last={last}&token={self.token}"
        r = requests.get(url)
        
        return r.json()
    def get_dividends(self, last=4):
        url = f"{self.BASE_URL}/advanced_dividends/{self.symbol}?last={last}&token={self.token}"
        r = requests.get(url)
        
        return r.json()
        