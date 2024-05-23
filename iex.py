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
        