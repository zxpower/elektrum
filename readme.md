# Elektrum Electricity Consumption Scraper

Script to srape your 

## Preparation

Start with installing necessary packages:

```
$ pip install -r requirements.txt
```

## Running 

```
$ python3 main.py username 'password' 2022 1 1
```

Will give you data for 2022-01-01

that looks like this:

```
{'data': {'A+': [{'date': '01:00', 'Patēriņš 01.01.2022': 0.81, 'NP biržas cena 01.01.2022': 0.05005}, {'date': '02:00', 'Patēriņš 01.01.2022': 1.298, 'NP biržas cena 01.01.2022': 0.04133}, {'date': '03:00', 'Patēriņš 01.01.2022': 0.758, 'NP biržas cena 01.01.2022': 0.04218}, {'date': '04:00', 'Patēriņš 01.01.2022': 1.371, 'NP biržas cena 01.01.2022': 0.04437}, {'date': '05:00', 'Patēriņš 01.01.2022': 0.592, 'NP biržas cena 01.01.2022': 0.03767}, {'date': '06:00', 'Patēriņš 01.01.2022': 0.534, 'NP biržas cena 01.01.2022': 0.0397}, {'date': '07:00', 'Patēriņš 01.01.2022': 0.476, 'NP biržas cena 01.01.2022': 0.04059}, {'date': '08:00', 'Patēriņš 01.01.2022': 0.503, 'NP biržas cena 01.01.2022': 0.04326}, {'date': '09:00', 'Patēriņš 01.01.2022': 0.592, 'NP biržas cena 01.01.2022': 0.04966}, {'date': '10:00', 'Patēriņš 01.01.2022': 0.999, 'NP biržas cena 01.01.2022': 0.07005}, {'date': '11:00', 'Patēriņš 01.01.2022': 0.511, 'NP biržas cena 01.01.2022': 0.07679}, {'date': '12:00', 'Patēriņš 01.01.2022': 2.614, 'NP biržas cena 01.01.2022': 0.0841}, {'date': '13:00', 'Patēriņš 01.01.2022': 2.037, 'NP biržas cena 01.01.2022': 0.09474}, {'date': '14:00', 'Patēriņš 01.01.2022': 2.048, 'NP biržas cena 01.01.2022': 0.0968}, {'date': '15:00', 'Patēriņš 01.01.2022': 2.086, 'NP biržas cena 01.01.2022': 0.09717}, {'date': '16:00', 'Patēriņš 01.01.2022': 2.182, 'NP biržas cena 01.01.2022': 0.10127}, {'date': '17:00', 'Patēriņš 01.01.2022': 2.227, 'NP biržas cena 01.01.2022': 0.1266}, {'date': '18:00', 'Patēriņš 01.01.2022': 1.424, 'NP biržas cena 01.01.2022': 0.14997}, {'date': '19:00', 'Patēriņš 01.01.2022': 0.86, 'NP biržas cena 01.01.2022': 0.14633}, {'date': '20:00', 'Patēriņš 01.01.2022': 0.875, 'NP biržas cena 01.01.2022': 0.14028}, {'date': '21:00', 'Patēriņš 01.01.2022': 1.299, 'NP biržas cena 01.01.2022': 0.12188}, {'date': '22:00', 'Patēriņš 01.01.2022': 1.479, 'NP biržas cena 01.01.2022': 0.10261}, {'date': '23:00', 'Patēriņš 01.01.2022': 1.028, 'NP biržas cena 01.01.2022': 0.09746}, {'date': '00:00', 'Patēriņš 01.01.2022': 0.744, 'NP biržas cena 01.01.2022': 0.08516}]}, 'statuses': {'balancedBill': {'A+': {'Patēriņš 01.01.2022': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}}, 'modified': {'A+': {'Patēriņš 01.01.2022': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}}}, 'texts': {'consumptionText': 'Patēriņš', 'dataPeriod': '01.01.2022', 'averageValuesTooltipText': 'Vidējais patēriņš', 'budgetBillTooltipText': 'Izlīdzinātais maksājums', 'modifiedDataTooltipText': '*Koriģēts patēriņš', 'componentTooltips': {'A+': 'A+'}, 'maximumAllowedLoadLine': 'Atļautā slodze (16.09 kWh)', 'tooltips': {'A+': {'Patēriņš 01.01.2022': ['01.01.2022. 01:00', '01.01.2022. 02:00', '01.01.2022. 03:00', '01.01.2022. 04:00', '01.01.2022. 05:00', '01.01.2022. 06:00', '01.01.2022. 07:00', '01.01.2022. 08:00', '01.01.2022. 09:00', '01.01.2022. 10:00', '01.01.2022. 11:00', '01.01.2022. 12:00', '01.01.2022. 13:00', '01.01.2022. 14:00', '01.01.2022. 15:00', '01.01.2022. 16:00', '01.01.2022. 17:00', '01.01.2022. 18:00', '01.01.2022. 19:00', '01.01.2022. 20:00', '01.01.2022. 21:00', '01.01.2022. 22:00', '01.01.2022. 23:00', '02.01.2022. 00:00'], 'NP biržas cena 01.01.2022': 'NP biržas cena 01.01.2022'}}, 'noDataError': '<div class="notification error" data-notification="error">    <p>Diemžēl šobrīd dati par izvēlēto periodu nav pieejami</p>\n</div>'}, 'labels': {'y': {'A+': 'kWh'}, 'y2': {'A+': 'EUR/kWh'}}, 'regions': {'weekends': {'ranges': [['01', '02'], ['08', '09'], ['15', '16'], ['22', '23'], ['29', '30']], 'aliases': ['S/Sv', 'S/Sv', 'S/Sv', 'S/Sv', 'S/Sv']}}, 'legend': {'A+': {'01.01.2022,': 'Patēriņš 01.01.2022', 'NP biržas cena 01.01.2022': 'NP biržas cena 01.01.2022'}}, 'groups': [], 'maximumAllowedLoad': None}
```
