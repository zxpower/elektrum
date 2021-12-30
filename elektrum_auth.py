import utils
    
def get_auth_token(session):
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    }

#     session.cookies.set("CookieControl",'{"necessaryCookies":["lv_production","sso_token_lve_sso","sso_token_next_sso","X-Mobile-App","X-Mobile-App-"],"optionalCookies":{"Statistika":"accepted","Marketings":"accepted"},"statement":{"shown":true,"updated":"15/03/2021"},"consentDate":1640251180721,"consentExpiry":365,"interactedWith":true,"user":"AA42C565-0BEB-41AC-81A8-8463EF9114E9"}' )
    r1 = session.get('https://www.elektrum.lv/lv/autorizacija', headers=headers, allow_redirects=True)
    lv_p = session.cookies.get('lv_production')

#     print('HTTP Status',r1.status_code)
    if r1.status_code == 200:
        tokens = utils.extract_all(r1.text, 'data-token="','"',inclusive=False)
#         print(tokens)
        return tokens[1]
    else:
        print('Something went wrong!', r1.status_code)
        




    
def authenticate(username, password ,token, session):
    login_params = {'email' :  username, 'password' :password, "captcha":""}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,lv;q=0.8',
        'Access-Control-Request-Headers': 'authorization,content-type',
        'Access-Control-Request-Method': 'POST',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'id.elektrum.lv',
        'Origin': 'https://www.elektrum.lv',
        'Pragma': 'no-cache',
        'Referer': 'https://www.elektrum.lv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',    
        'Authorization':  'Bearer '+ token
    }
    r3 = session.post('https://id.elektrum.lv/api/v1/authentication/credentials/authenticate', data=login_params,headers=headers)
    return r3.status_code == 200
#     print(r3.json())


