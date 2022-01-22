from .utils import extract_all
    
def get_auth_token(session):
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    }
    response = session.get('https://www.elektrum.lv/lv/autorizacija', headers=headers, allow_redirects=True)
    if response.status_code == 200:
        tokens = extract_all(response.text, 'data-token="', '"', inclusive=False)
        return tokens[1]
    else:
        print('Something went wrong!', response.status_code)

   
def authenticate(username, password ,token, session):
    login_params = {
        'email':  username,
        'password': password,
        'captcha': ''
    }
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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
        'Authorization':  'Bearer '+ token
    }
    response = session.post('https://id.elektrum.lv/api/v1/authentication/credentials/authenticate', data=login_params, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print('Something went wrong!', response.status_code)
