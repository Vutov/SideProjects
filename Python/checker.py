import requests
from bs4 import BeautifulSoup
import re

def getMinsLeft(username, password):
    # Login
    with requests.Session() as c:
        url = 'https://www.mtel.bg/login'
        USERNAME = username
        PASSWORD = password
        c.get(url)
        login_data = dict(maccount=USERNAME, mpassword=PASSWORD)
        c.post(url, data=login_data, headers={"Referer":'https://www.mtel.bg/'})
        # Get current numbers data.
        page = c.get('https://www.mtel.bg/tekushto-potreblenie')
        # Get page
        soup = BeautifulSoup(page.content)
        progressBars = soup.find_all('div', class_='progress-holder-type-2')
        # Get data
        regex = 'Оставащи.*?\s*(\d*:\d*)\s*от\s*(\d*:\d*)'
        curData = []
        for match in progressBars:
            row = match.find('p').text
            match = re.findall(regex, row)
            if (match):
                curData.append(match)
        return curData