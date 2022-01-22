import elektrum
import requests
import sys

# python3 main.py username 'password' 2021 3 1 meterID

# arguments
#   username
#   password
#   year
#   month
#   day
#   meterID

args = sys.argv
session = requests.session()
token = elektrum.get_auth_token(session)
elektrum.authenticate(args[1], args[2], token, session)
meter = ''
if len(args) > 6:
    meter = args[6]
result = elektrum.fetch_daily_consumption(args[3], args[4], args[5], session, meter)
print(result)
