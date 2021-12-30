import requests
import sys
import elektrum_auth
import elektrum_fetch


# python3 main.py username 'password' 2021 3 1

# arguments
#   username
#   password
#   year
#   month
#   day


args = sys.argv
session = requests.session()
token = elektrum_auth.get_auth_token(session)
elektrum_auth.authenticate(args[1], args[2],token, session)
result = elektrum_fetch.fetch_daily_consumption(args[3],args[4],args[5], session)
print(result)