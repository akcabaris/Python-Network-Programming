import requests

url = "https://github.com/"
headers = {'user-agent' : 'btk-akademi/1.1.1'}

# r = requests.get(url)
# r = requests.get(url, allow_redirects=False)
# r = requests.get(url, headers=headers, allow_redirects=False)
# r = requests.get(url, headers=headers, allow_redirects=True,timeout=0.001)
r = requests.get(url, headers=headers, allow_redirects=True,timeout=2)

print(r.status_code)
# print(r.text)
#print(r.headers)
#print(r.headers.get('X-XSS-Protection'))
#print(r.headers.get('Date'))


# status_code
# text
# headers, headers values