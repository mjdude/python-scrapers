# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://www.linkedin.com/in/kevinsdick/')
# c = r.content
# print(c)

import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, 'html.parser')
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'',
    'session_password':'',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

res = client.get('https://www.linkedin.com/in/kevinsdick/RL')

print(res.content)
