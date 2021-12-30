
def fetch_daily_consumption(y,m,d, session):

    # url = "https://mans.elektrum.lv/lv/majai/mani-parskati/viedo-skaititaju-paterinu-parskats/consumption.json?step=D&fromDate=2021-01-02&tillDate=&compareFromDate=2021-12-21&compareTillDate=&chartType=bar"
    fromDate = f'{y}-{m}-{d}'
    url = f"https://mans.elektrum.lv/lv/majai/mani-parskati/viedo-skaititaju-paterinu-parskats/consumption.json?step=D&fromDate={fromDate}"
    headers = {
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,lv;q=0.8",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }
    response = session.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()
    else:
        print('Something went wrong! HTTP', response.status_code)
        return None
